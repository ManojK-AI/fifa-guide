"""7. Keyboard: arrow keys across the four tabs, trainer Space/1-3/V, replays Space/arrows/V, visible focus on every Tab stop."""
from common import *
from playwright.sync_api import sync_playwright
L = Log('keyboard')
T = lambda pg, sel: pg.evaluate(f"document.querySelector('{sel}').textContent")
ACT = "(()=>{const a=document.activeElement;return a?(a.id||a.className||a.tagName)+'|'+a.tagName:'none'})()"
FOCUS_STYLE = """()=>{const a=document.activeElement;if(!a||a===document.body)return null;const cs=getComputedStyle(a);
  const r=a.getBoundingClientRect();
  return {el:(a.id?'#'+a.id:a.tagName.toLowerCase()+'.'+(a.className||'').toString().split(' ')[0])+(a.dataset&&a.dataset.clip?'['+a.dataset.clip+']':'')+' '+(a.textContent||'').trim().slice(0,24),
   os:cs.outlineStyle,ow:parseFloat(cs.outlineWidth),oc:cs.outlineColor,bs:cs.boxShadow,fv:a.matches(':focus-visible'),
   vis:a.checkVisibility(),onscreen:r.right>0&&r.left<innerWidth&&r.width>0,ar:[Math.round(r.left),Math.round(r.top),Math.round(r.width),Math.round(r.height)]}}"""
with sync_playwright() as p:
    b = p.chromium.launch()
    for game in ('fc26', 'fc23'):
        ctx, pg, errs = open_clock(b, 1280, 900, game=game, pause=True)
        # Tab from the start of the page to the tab list
        pg.keyboard.press('Tab'); stops = []
        for _ in range(8):
            a = pg.evaluate(ACT); stops.append(a)
            if a.startswith('mt-'): break
            pg.keyboard.press('Tab')
        L.check(pg.evaluate(ACT).startswith('mt-trainer'), f'{game}: Tab reaches the Trainer tab', stops)
        L.note(f'{game}: Tab stops before tabs: {stops}')
        seq = []
        for key in ['ArrowRight'] * 4 + ['ArrowLeft'] * 2:
            pg.keyboard.press(key); pg.clock.run_for(30)
            m = pg.evaluate("document.querySelector('.mtab[aria-selected=true]').dataset.m")
            fs = pg.evaluate(FOCUS_STYLE)
            seq.append(m)
            L.check(pg.evaluate(ACT).startswith('mt-' + m), f'{game}: focus follows selected tab {m}', pg.evaluate(ACT))
            L.check(pg.is_visible(f'#p-{m}') and sum(pg.is_visible(f'#p-{x}') for x in ('trainer', 'ai', 'replays', 'plan')) == 1, f'{game}: only panel {m} visible')
            L.check(fs and fs['fv'] and fs['os'] != 'none' and fs['ow'] >= 2, f'{game}: tab {m} shows a focus ring', fs)
        L.check(seq == ['ai', 'replays', 'plan', 'trainer', 'plan', 'replays'], f'{game}: arrow order wraps', seq)
        tabidx = pg.evaluate("[...document.querySelectorAll('.mtab')].map(b=>b.tabIndex)")
        L.check(tabidx.count(0) == 1, f'{game}: roving tabindex on tabs', tabidx)
        # ---- Replays keyboard ----
        # focus is on the Replays tab now; Space there?
        pg.clock.run_for(500)
        st0 = pg.evaluate(STATE_JS)
        pg.keyboard.press('Space'); pg.clock.run_for(600); st1 = pg.evaluate(STATE_JS)
        L.note(f"{game}: Space with focus on the Replays tab -> play button before '{st0['play']}' after '{st1['play']}'")
        # move focus to the body (click the caption) and use Space/arrows/V
        pg.click('#say'); pg.clock.run_for(50)
        a = pg.evaluate(STATE_JS)['play']
        pg.keyboard.press('Space'); pg.clock.run_for(50); b1 = pg.evaluate(STATE_JS)['play']
        pg.keyboard.press('Space'); pg.clock.run_for(50); c1 = pg.evaluate(STATE_JS)['play']
        L.check(a != b1 and c1 == a, f'{game}: Space toggles play/pause in Replays (focus on page)', (a, b1, c1))
        bug0 = pg.evaluate(STATE_JS)['bug']
        pg.keyboard.press('ArrowRight'); pg.clock.run_for(50); bug1 = pg.evaluate(STATE_JS)['bug']
        pg.keyboard.press('ArrowLeft'); pg.clock.run_for(50); bug2 = pg.evaluate(STATE_JS)['bug']
        L.check(TIDS.index(bug1) == (TIDS.index(bug0) + 1) % len(TIDS) and bug2 == bug0, f'{game}: arrows change clip', (bug0, bug1, bug2))
        v0 = pg.get_attribute('#viewCam', 'aria-pressed'); pg.keyboard.press('v'); pg.clock.run_for(30); v1 = pg.get_attribute('#viewCam', 'aria-pressed')
        pg.keyboard.press('V'); pg.clock.run_for(30); v2 = pg.get_attribute('#viewCam', 'aria-pressed')
        L.check(v0 != v1 and v2 == v0, f'{game}: V toggles camera in Replays', (v0, v1, v2))
        # Space after mouse-picking a clip (focus stays on the picker button)
        pg.click(f'.titem[data-i="{TIDS.index("U5")}"]'); pg.clock.run_for(2500)
        g0 = pg.evaluate(STATE_JS)
        pg.keyboard.press('Space'); pg.clock.run_for(1000); g1 = pg.evaluate(STATE_JS)
        L.check(g1['scrub'] == g0['scrub'] or g1['play'] != g0['play'], f'{game}: Space after clicking a clip in the picker pauses (instead of restarting the clip)', {'before': (g0['scrub'], g0['play'], g0['clock']), 'after': (g1['scrub'], g1['play'], g1['clock'])})
        # Space after clicking Match cam / speed buttons
        pg.click('#spdOne'); pg.clock.run_for(500); h0 = pg.evaluate(STATE_JS)
        pg.keyboard.press('Space'); pg.clock.run_for(800); h1 = pg.evaluate(STATE_JS)
        L.check(h1['play'] != h0['play'], f'{game}: Space after clicking the 1x speed button toggles play', (h0['play'], h1['play'], h0['scrub'], h1['scrub']))
        # ---- Trainer keyboard ----
        pg.click('#mt-trainer'); pg.clock.run_for(50)
        L.check(pg.is_visible('#tintro'), f'{game}: trainer intro visible')
        pg.keyboard.press('Space'); pg.clock.run_for(50)
        started_from_tab = not pg.is_visible('#tintro')
        L.note(f'{game}: Space with focus on the Trainer tab starts a round: {started_from_tab}')
        if not started_from_tab:
            pg.click('.scard h2'); pg.keyboard.press('Space'); pg.clock.run_for(50)
        L.check(not pg.is_visible('#tintro') and T(pg, '#twho') == 'Read', f'{game}: Space starts the round (focus on page)')
        got_choice = got_tap = False
        for n in range(10):
            for _ in range(200):
                if T(pg, '#twho') == 'Your call': break
                pg.clock.run_for(25)
            if pg.is_visible('#tchoices'):
                pg.keyboard.press('2'); pg.clock.run_for(30)
                L.check(T(pg, '#twho') in ('Right', 'Wrong') and pg.evaluate("document.querySelectorAll('.tchoice:disabled').length") == 3, f'{game}: key 2 answers a choice scene', T(pg, '#twho'))
                picked = pg.evaluate("[...document.querySelectorAll('.tchoice')].findIndex(b=>b.classList.contains('ok')||b.classList.contains('bad'))")
                got_choice = True
            else:
                pg.keyboard.press('2'); pg.clock.run_for(30)
                L.check(T(pg, '#twho') == 'Your call', f'{game}: number key ignored on a tap scene')
                a = pg.evaluate("window.__lrrAnsPt()"); pg.mouse.click(a[0], a[1]); pg.clock.run_for(30); got_tap = True
            v0 = pg.get_attribute('[data-tv="cam"]', 'aria-pressed'); pg.keyboard.press('v'); pg.clock.run_for(30)
            L.check(pg.get_attribute('[data-tv="cam"]', 'aria-pressed') != v0, f'{game}: V toggles trainer camera')
            act = pg.evaluate(ACT)
            pg.keyboard.press('Space'); pg.clock.run_for(30)
            moved = T(pg, '#twho') in ('Read', 'Done')
            if not moved:
                L.check(False, f'{game}: Space moves on after an answer (focus was {act})', T(pg, '#twho'))
                pg.click('#tnext'); pg.clock.run_for(30)
        L.check(got_choice, f'{game}: round included a choice scene')
        L.check(pg.is_visible('#tsum'), f'{game}: Space through to the summary')
        pg.keyboard.press('Space'); pg.clock.run_for(30)
        L.check(not pg.is_visible('#tsum') and T(pg, '#tbCode') == '1/10', f'{game}: Space on the summary starts another round', T(pg, '#tbCode'))
        # number keys on choice scenes with 3 options: key 4 ignored
        L.check(not errs, f'{game}: no console errors', errs[:4])
        ctx.close()

    # ---- visible focus on every Tab stop, every tab panel, light + dark ----
    for dark in (False, True):
        for game in ('fc26', 'fc23'):
            ctx, pg, errs = open_clock(b, 1280, 900, dark=dark, game=game, pause=True)
            for m in ('trainer', 'ai', 'replays', 'plan'):
                pg.evaluate(f"window.__lrrMode('{m}')"); pg.clock.run_for(50)
                pg.evaluate("document.activeElement&&document.activeElement.blur();window.scrollTo(0,0)")
                pg.keyboard.press('Tab')
                seen, bad = 0, []
                for _ in range(260):
                    fs = pg.evaluate(FOCUS_STYLE)
                    if fs is None: break
                    seen += 1
                    ring = (fs['os'] not in ('none', '') and fs['ow'] >= 1.5) or (fs['bs'] and fs['bs'] != 'none')
                    if not ring or not fs['vis']:
                        bad.append(fs)
                    if fs['el'].startswith('a') and 'Legendary Playbook' in fs['el']: break
                    pg.keyboard.press('Tab')
                    if pg.evaluate(ACT).startswith('BODY'): break
                L.check(not bad, f'{"dark" if dark else "light"}/{game}/{m}: every Tab stop has a visible focus indicator ({seen} stops)', bad[:6])
            ctx.close()
    b.close()
L.dump()
