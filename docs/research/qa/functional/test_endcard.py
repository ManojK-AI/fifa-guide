"""End card / title card fit inside the replay screen at every width, for every clip (long names)."""
from common import *
from playwright.sync_api import sync_playwright
L = Log('endcard')
with sync_playwright() as p:
    b = p.chromium.launch()
    for w, h in ((320, 640), (390, 844), (820, 1180), (1280, 900)):
        ctx, pg, errs = open_clock(b, w, h, pause=True)
        pg.click('#mt-replays'); pg.clock.run_for(50)
        worst = []
        for i, tid in enumerate(TIDS):
            pg.evaluate(f"window.__lrrShow({i},'right',20,'board')")
            pg.evaluate("document.querySelector('#playBtn').click()")  # play from the end -> tick sets ended -> end card
            pg.clock.run_for(100)
            if not pg.is_visible('#endcard'):
                # force via the real loop: jump near the end and play
                pass
            r = pg.evaluate("""()=>{const e=document.getElementById('endcard'),s=document.getElementById('screen');
              const kids=[...e.children].map(k=>k.getBoundingClientRect());const sr=s.getBoundingClientRect();
              const top=Math.min(...kids.map(k=>k.top)),bot=Math.max(...kids.map(k=>k.bottom));
              return {vis:!e.hidden,top:Math.round(top-sr.top),bot:Math.round(bot-sr.top),h:Math.round(sr.height),
                btns:[...e.querySelectorAll('button')].map(b=>{const r=b.getBoundingClientRect();return [b.textContent,Math.round(r.width),Math.round(r.height),b.scrollWidth>b.clientWidth+1]})}}""")
            if r['vis'] and (r['top'] < 0 or r['bot'] > r['h']):
                worst.append((tid, r['top'], r['bot'], r['h']))
            if not r['vis']:
                L.check(False, f'{w}: end card visible for {tid}')
        L.check(not worst, f'{w}x{h}: end card content fits the screen for all clips', worst[:6])
        L.note(f'{w}: sample end card {r}')
        # title card fits (right-way card) for every clip
        bad = []
        for i, tid in enumerate(TIDS):
            pg.evaluate(f"window.__lrrShow({i},'wrong',0,'board')")
            pg.evaluate(f"document.querySelector('#jumpW').click()")
            # place playhead inside the card segment
            pg.evaluate(f"window.__lrrShow({i},'wrong',{TAC[tid]['wrong']['dur']},'board')")
            pg.evaluate("document.querySelector('#playBtn').click()"); pg.clock.run_for(400)
            r = pg.evaluate("""()=>{const c=document.getElementById('card'),s=document.getElementById('screen');if(c.hidden)return null;
              const t=document.getElementById('cardT').getBoundingClientRect(),k=document.getElementById('cardK').getBoundingClientRect(),sr=s.getBoundingClientRect();
              return {top:Math.round(k.top-sr.top),bot:Math.round(t.bottom-sr.top),h:Math.round(sr.height),right:Math.round(t.right-sr.left),w:Math.round(sr.width)}}""")
            if r and (r['top'] < 0 or r['bot'] > r['h'] or r['right'] > r['w']): bad.append((tid, r))
        L.check(not bad, f'{w}x{h}: title cards fit', bad[:4])
        L.check(not errs, f'{w}: no console errors', errs[:3])
        ctx.close()
    b.close()
L.dump()
