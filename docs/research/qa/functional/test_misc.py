"""Misc: trainer settings persistence, blocked storage, reduced motion, monkey test with invariants."""
from common import *
import random
from playwright.sync_api import sync_playwright
L = Log('misc')
INV = """()=>{const panels=['trainer','ai','replays','plan'].filter(m=>!document.getElementById('p-'+m).hidden);
 const g=document.documentElement.dataset.game;const pressed=[...document.querySelectorAll('[data-gm]')].filter(b=>b.getAttribute('aria-pressed')==='true').map(b=>b.dataset.gm);
 const vis=[...document.querySelectorAll('[data-chk]')].filter(c=>c.closest(g==='fc23'?'.g23':'.g26'));const n=vis.filter(c=>c.checked).length;
 const other=[...document.querySelectorAll(g==='fc23'?'.g26':'.g23')].filter(e=>e.checkVisibility()).length;
 const sel=[...document.querySelectorAll('.mtab')].filter(b=>b.getAttribute('aria-selected')==='true').map(b=>b.dataset.m);
 return {panels,g,pressed,count:document.getElementById('chkCount').textContent,want:n+' of '+vis.length+' done',other,sel,
   sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth};}"""
with sync_playwright() as p:
    b = p.chromium.launch()
    # trainer settings persistence
    ctx, pg, errs = open_page(b, 1280, 900)
    pg.click('[data-lv="ult"]'); pg.click('[data-tf="att"]'); pg.click('[data-tv="cam"]')
    pg.reload(); pg.wait_for_timeout(300)
    L.check(pg.get_attribute('[data-lv="ult"]', 'aria-pressed') == 'true' and pg.get_attribute('[data-tf="att"]', 'aria-pressed') == 'true' and pg.get_attribute('[data-tv="cam"]', 'aria-pressed') == 'true', 'trainer level/focus/camera persist after reload')
    L.check(pg.text_content('#tiTime') == '1.4 seconds' and pg.text_content('#tiK') == 'Scan trainer · Your ball: break the AI', 'intro reflects persisted settings', (pg.text_content('#tiTime'), pg.text_content('#tiK')))
    ctx.close()
    # storage that throws
    ctx = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2)
    pg = ctx.new_page(); errs = attach(pg, page_html())
    pg.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new DOMException('denied','SecurityError')}});")
    pg.goto(URL); pg.wait_for_timeout(500)
    L.check(pg.evaluate("document.documentElement.dataset.game") == 'fc26', 'blocked storage: loads with FC 26')
    pg.click('[data-gm="fc23"]'); pg.click('#mt-plan'); pg.click('[data-chk="cam"]')
    L.check(pg.text_content('#chkCount') == '1 of 11 done', 'blocked storage: checklist still counts', pg.text_content('#chkCount'))
    pg.click('#mt-replays'); pg.wait_for_timeout(300); pg.click('#nextBtn'); pg.wait_for_timeout(200)
    L.check(pg.text_content('#bugCode') == 'U2', 'blocked storage: replays work', pg.text_content('#bugCode'))
    pg.click('#mt-trainer'); pg.click('#tstart'); pg.wait_for_timeout(1600)
    L.check(pg.text_content('#twho') == 'Your call', 'blocked storage: trainer runs', pg.text_content('#twho'))
    L.check(not errs, 'blocked storage: no console errors', errs[:3])
    ctx.close()
    # reduced motion
    ctx = b.new_context(viewport={'width': 1280, 'height': 900}, reduced_motion='reduce')
    pg = ctx.new_page(); errs = attach(pg, page_html()); pg.goto(URL); pg.wait_for_timeout(400)
    pg.click('#mt-replays'); pg.wait_for_timeout(1200)
    s = pg.evaluate(STATE_JS)
    L.check(s['play'] == 'Play' and s['clock'] == '0:00', 'reduced motion: replays wait for Play', s)
    pg.click('#playBtn'); pg.wait_for_timeout(1500); s = pg.evaluate(STATE_JS)
    L.check(s['play'] == 'Pause' and s['scrub'] > 3, 'reduced motion: plays after Play', s)
    pg.click('#reelBtn'); pg.wait_for_timeout(2500); s = pg.evaluate(STATE_JS)
    L.check(s['reelLabel'] == 'Stop reel' and not s['card'], 'reduced motion: reel runs', s)
    pg.click('#mt-trainer'); pg.click('#tstart'); pg.wait_for_timeout(1600)
    L.check(pg.text_content('#twho') == 'Your call', 'reduced motion: trainer runs')
    L.check(not errs, 'reduced motion: no console errors', errs[:3])
    ctx.close()
    # monkey test
    for seed, (w, h, dark) in enumerate(((390, 844, False), (1280, 900, True), (820, 1180, False))):
        rnd = random.Random(seed + 7)
        ctx, pg, errs = open_page(b, w, h, dark=dark)
        bad = []
        for step in range(500):
            r = rnd.random()
            try:
                if r < 0.65:
                    cands = pg.evaluate("""()=>[...document.querySelectorAll('button,input[type=checkbox],.scrub')].filter(e=>e.checkVisibility()&&!e.disabled).map((e,i)=>{e.dataset.mk=i;return i})""")
                    if cands:
                        k = rnd.choice(cands)
                        el = pg.locator(f'[data-mk="{k}"]')
                        el.scroll_into_view_if_needed(timeout=2000); el.click(timeout=2000)
                elif r < 0.8:
                    pg.keyboard.press(rnd.choice(['Space', 'ArrowLeft', 'ArrowRight', '1', '2', '3', 'v', 'Enter', 'Tab', 'Home', 'End']))
                elif r < 0.92:
                    bb = pg.locator('#tcv').bounding_box() if pg.is_visible('#tcv') else pg.locator('#cv').bounding_box() if pg.is_visible('#cv') else None
                    if bb: pg.mouse.click(bb['x'] + rnd.random() * bb['width'], bb['y'] + rnd.random() * bb['height'])
                else:
                    pg.wait_for_timeout(rnd.choice([100, 400, 900, 1600]))
            except Exception as e:
                pass
            if step % 25 == 0:
                v = pg.evaluate(INV)
                probs = []
                if len(v['panels']) != 1 or v['sel'] != v['panels']: probs.append('panel/tab mismatch')
                if v['pressed'] != [v['g']]: probs.append('switch state')
                if v['count'] != v['want']: probs.append('count ' + v['count'] + ' vs ' + v['want'])
                if v['other']: probs.append('other-game blocks visible')
                if v['sw'] > v['cw']: probs.append('h-scroll')
                if probs: bad.append((step, probs))
            # a new tab may have opened from a link click
            for extra in ctx.pages[1:]:
                extra.close()
        L.check(not bad, f'monkey {w}/{dark}: invariants held for 500 random actions', bad[:5])
        L.check(not errs, f'monkey {w}/{dark}: no console errors', errs[:5])
        ctx.close()
    b.close()
L.dump()
