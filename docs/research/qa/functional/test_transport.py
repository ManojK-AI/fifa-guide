"""3b. Replays transport: play/pause, prev/next, restart, scrubber (click, drag, keys), jump wrong/right, speed, persistence, picker groups."""
from common import *
from playwright.sync_api import sync_playwright
L = Log('transport')
PROG_JS = """()=>{const h=document.getElementById('head'),t=document.getElementById('track');
  return {left:parseFloat(h.style.left)||0,tw:t.getBoundingClientRect().width,now:+document.getElementById('scrub').getAttribute('aria-valuenow'),
  text:document.getElementById('scrub').getAttribute('aria-valuetext'),play:document.getElementById('playBtn').getAttribute('aria-label'),
  icon:document.getElementById('playIco').innerHTML.includes('M4 2h3')?'pause-icon':'play-icon',
  st:document.getElementById('bugState').textContent,bug:document.getElementById('bugCode').textContent,card:!document.getElementById('card').hidden,
  end:!document.getElementById('endcard').hidden}}"""
def moving(pg, ms=1500):
    pg.clock.run_for(40)   # let the click render first
    a = pg.evaluate(PROG_JS); pg.clock.run_for(ms); c = pg.evaluate(PROG_JS)
    return c['left'] != a['left'] or c['bug'] != a['bug'], a, c

with sync_playwright() as p:
    b = p.chromium.launch()
    for game in ('fc26', 'fc23'):
        ctx, pg, errs = open_clock(b, 1280, 900, game=game, pause=True)
        pg.click('#mt-replays'); pg.clock.run_for(100)
        mv, a, c = moving(pg)
        L.check(mv and c['play'] == 'Pause' and c['icon'] == 'pause-icon', f'{game}: autoplays on open with Pause button', c)
        # play/pause
        pg.click('#playBtn'); pg.clock.run_for(50)
        mv, a, c = moving(pg)
        L.check(not mv and c['play'] == 'Play' and c['icon'] == 'play-icon', f'{game}: pause stops and button shows Play', c)
        pg.click('#playBtn'); mv, a, c = moving(pg)
        L.check(mv and c['play'] == 'Pause', f'{game}: play resumes and button shows Pause', c)
        # icon consistency after selecting another clip while paused
        pg.click('#playBtn'); pg.clock.run_for(50)
        u3 = TIDS.index('U3')
        pg.click(f'.titem[data-i="{u3}"]'); mv, a, c = moving(pg)
        L.check(c['bug'] == 'U3', f'{game}: picker selects U3', c['bug'])
        L.check((c['play'] == 'Pause') == mv, f'{game}: play button state matches playback after picking a clip while paused', {'moving': mv, 'button': c['play'], 'icon': c['icon']})
        # next from the end card while button says Play
        pg.clock.run_for(20000); s = pg.evaluate(PROG_JS)
        L.check(s['end'], f'{game}: U3 end card', s)
        pg.click('#endRow button[data-act="next"]'); mv, a, c = moving(pg)
        L.check(c['bug'] == 'U4', f'{game}: end card Next goes to U4', c['bug'])
        L.check((c['play'] == 'Pause') == mv, f'{game}: play button state matches playback after end-card Next', {'moving': mv, 'button': c['play']})
        # what happens if the user now presses the (Play-looking) button
        pg.click('#playBtn'); mv2, a2, c2 = moving(pg)
        L.note(f'{game}: after end-card Next, clip moving={mv} with button "{c["play"]}"; one click on it -> moving={mv2}, button "{c2["play"]}"')
        if not mv2: pg.click('#playBtn'); pg.clock.run_for(50)
        # end card Replay / Right way again
        pg.clock.run_for(20000)
        pg.click('#endRow button[data-act="right"]'); pg.clock.run_for(100); s = pg.evaluate(PROG_JS)
        L.check(s['st'] == 'Right' and not s['end'] and not s['card'], f'{game}: end card Right way again starts right clip', s)
        pg.clock.run_for(20000)
        pg.click('#endRow button[data-act="replay"]'); pg.clock.run_for(100); s = pg.evaluate(PROG_JS)
        L.check(s['st'] == 'Wrong' and s['now'] <= 2 and not s['end'], f'{game}: end card Replay restarts', s)
        # prev / next, wrap-around
        u1 = TIDS.index('U1'); pg.click(f'.titem[data-i="{u1}"]'); pg.clock.run_for(50)
        pg.click('#prevBtn'); pg.clock.run_for(50); s = pg.evaluate(PROG_JS)
        L.check(s['bug'] == TIDS[-1], f'{game}: prev from U1 wraps to {TIDS[-1]}', s['bug'])
        pg.click('#nextBtn'); pg.clock.run_for(50); pg.click('#nextBtn'); pg.clock.run_for(50); s = pg.evaluate(PROG_JS)
        L.check(s['bug'] == 'U2', f'{game}: next twice -> U2', s['bug'])
        L.check(pg.get_attribute('.titem[aria-current="true"]', 'data-i') == str(TIDS.index('U2')), f'{game}: picker highlights U2')
        L.check(pg.inner_text('#coachT').lower() == TAC['U2']['name'].lower(), f'{game}: coach card follows next')
        # restart
        pg.clock.run_for(4000); pg.click('#restartBtn'); pg.clock.run_for(30); s = pg.evaluate(PROG_JS)
        L.check(s['st'] == 'Wrong' and s['now'] <= 1, f'{game}: restart goes back to 0', s)
        # scrubber clicks
        box = pg.locator('#track').bounding_box()
        for frac in (0.1, 0.5, 0.95):
            pg.click('#playBtn') if pg.evaluate(PROG_JS)['play'] == 'Pause' else None
            pg.mouse.click(box['x'] + box['width'] * frac, box['y'] + box['height'] / 2); pg.clock.run_for(50)
            s = pg.evaluate(PROG_JS)
            L.check(abs(s['left'] / s['tw'] - frac) < 0.03, f'{game}: scrub click at {frac:.0%} moves head', (round(s['left'] / s['tw'], 3)))
        s = pg.evaluate(PROG_JS)
        L.check(s['st'] == 'Right' and 'Right way' in s['text'], f'{game}: scrub to 95% is right way', s['text'])
        # drag
        pg.mouse.move(box['x'] + box['width'] * 0.2, box['y'] + 4); pg.mouse.down()
        for fx in (0.3, 0.4, 0.6):
            pg.mouse.move(box['x'] + box['width'] * fx, box['y'] + 4); pg.clock.run_for(30)
        pg.mouse.up(); s = pg.evaluate(PROG_JS)
        L.check(abs(s['left'] / s['tw'] - 0.6) < 0.03, f'{game}: scrub drag to 60%', round(s['left'] / s['tw'], 3))
        # scrub keyboard
        pg.focus('#scrub'); pg.keyboard.press('Home'); pg.clock.run_for(50); s0 = pg.evaluate(PROG_JS)
        L.check(s0['left'] < 3 and s0['bug'] == 'U2', f'{game}: scrub Home -> start, stays on clip', s0)
        for _ in range(4): pg.keyboard.press('ArrowRight')
        pg.clock.run_for(50); s1 = pg.evaluate(PROG_JS)
        L.check(s1['bug'] == 'U2' and s1['left'] > s0['left'], f'{game}: scrub ArrowRight moves within clip (not next clip)', s1)
        pg.keyboard.press('End'); pg.clock.run_for(50); s2 = pg.evaluate(PROG_JS)
        L.check(s2['now'] >= 99, f'{game}: scrub End -> end', s2['now'])
        # jump wrong/right while playing and paused
        pg.click('#jumpR'); pg.clock.run_for(60); s = pg.evaluate(PROG_JS)
        L.check(s['st'] == 'Right' and s['play'] == 'Pause', f'{game}: jump Right starts right clip and plays', s)
        pg.click('#jumpW'); mv, a, c = moving(pg, 500)
        L.check(c['st'] == 'Wrong' and mv, f'{game}: jump Wrong while playing restarts wrong way, keeps playing', c)
        pg.click('#playBtn'); pg.clock.run_for(50)
        pg.click('#jumpR'); mv, a, c = moving(pg, 500)
        L.note(f'{game}: jump Right while paused -> moving={mv}, button "{c["play"]}"')
        pg.click('#playBtn') if c['play'] == 'Pause' else None; pg.clock.run_for(50)
        pg.click('#jumpW'); mv, a, c = moving(pg, 500)
        L.note(f'{game}: jump Wrong while paused -> moving={mv}, button "{c["play"]}", state {c["st"]}')
        L.check(pg.get_attribute('#jumpW', 'aria-pressed') == 'true' and pg.get_attribute('#jumpR', 'aria-pressed') == 'false', f'{game}: jump toggles aria-pressed')
        # speeds: measure progress over 3 s of U1 (total 14.15 s)
        pg.click(f'.titem[data-i="{u1}"]'); pg.clock.run_for(50)
        if pg.evaluate(PROG_JS)['play'] == 'Play' and not moving(pg, 200)[0]: pg.click('#playBtn')
        rates = {}
        for sel, x in (('#spdHalf', 0.5), ('#spdOne', 1), ('#spdFast', 1.5)):
            pg.click(f'.titem[data-i="{u1}"]'); pg.click(sel); pg.clock.run_for(50)
            a = pg.evaluate(PROG_JS); pg.clock.run_for(3000); c = pg.evaluate(PROG_JS)
            rates[x] = (c['left'] - a['left']) / c['tw'] * 14.15 / 3
            L.check(pg.get_attribute(sel, 'aria-pressed') == 'true', f'{game}: {sel} aria-pressed')
        L.check(abs(rates[0.5] - 0.5) < 0.08 and abs(rates[1] - 1) < 0.08 and abs(rates[1.5] - 1.5) < 0.1, f'{game}: speed rates', {k: round(v, 2) for k, v in rates.items()})
        L.check(pg.evaluate("localStorage.getItem('lrr:speed')") == '1.5', f'{game}: speed stored')
        pg.click('#viewCam'); pg.clock.run_for(50)
        L.check(pg.evaluate("localStorage.getItem('lrr:view')") == 'cam' and pg.get_attribute('#viewCam', 'aria-pressed') == 'true', f'{game}: view stored')
        L.check(not errs, f'{game}: no console errors', errs[:4])
        ctx.close()

    # persistence of speed/view/clip in a clean context
    ctx, pg, errs = open_page(b, 1280, 900)
    pg.click('#mt-replays'); c4 = TIDS.index('C4'); pg.click(f'.titem[data-i="{c4}"]'); pg.click('#spdHalf'); pg.click('#viewCam')
    pg.reload(); pg.wait_for_timeout(400)
    L.check(pg.evaluate("document.querySelector('.mtab[aria-selected=true]').dataset.m") == 'replays', 'last tab restored after reload')
    L.check(pg.text_content('#bugCode') == 'C4', 'last clip restored after reload', pg.text_content('#bugCode'))
    L.check(pg.get_attribute('#spdHalf', 'aria-pressed') == 'true' and pg.get_attribute('#viewCam', 'aria-pressed') == 'true', 'speed and camera restored after reload')
    ctx.close()

    # phone: picker group tabs
    for w in (390, 320):
        ctx, pg, errs = open_page(b, w, 844)
        pg.click('#mt-replays'); pg.wait_for_timeout(100)
        tabs = pg.eval_on_selector_all('#tabs .tab', 'els=>els.map(e=>[e.textContent,e.getAttribute("aria-selected"),e.checkVisibility()])')
        L.note(f'{w}px group tabs: {tabs}')
        pg.click('#tab-stop'); pg.wait_for_timeout(100)
        vis = pg.eval_on_selector_all('.titem', 'els=>els.filter(e=>e.checkVisibility()).map(e=>e.querySelector(".code").textContent)')
        L.check(vis == ['A1', 'A2', 'A3', 'A4', 'A5', 'A6'], f'{w}px: Stop it tab shows A clips', vis)
        pg.click('.titem[data-i="10"]'); pg.wait_for_timeout(100)
        L.check(pg.text_content('#bugCode') == 'A4', f'{w}px: tapping A4 selects it', pg.text_content('#bugCode'))
        # every group tab reachable (not clipped)?
        clip = pg.evaluate("""()=>{const t=document.getElementById('tabs');return {sw:t.scrollWidth,cw:t.clientWidth,
            items:[...t.children].map(b=>{const r=b.getBoundingClientRect();return [b.textContent,Math.round(r.left),Math.round(r.right),b.scrollWidth>b.clientWidth]})}}""")
        L.note(f'{w}px tabs bar: {clip}')
        pg.click('#nextBtn'); pg.wait_for_timeout(100)
        L.check(pg.text_content('#bugCode') == 'A5', f'{w}px: next -> A5')
        for _ in range(3): pg.click('#nextBtn'); pg.wait_for_timeout(60)
        L.check(pg.get_attribute('#tab-build', 'aria-selected') == 'true', f'{w}px: group tab follows clip into Build-up')
        L.check(not errs, f'{w}px: no console errors', errs[:4])
        ctx.close()
    b.close()
L.dump()
