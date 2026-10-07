from common import *
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx, pg, errs = open_clock(b, 1280, 900)
    pg.click('#mt-replays'); pg.clock.run_for(50)
    for cid in ('B3', 'U1', 'N2'):
        i = TIDS.index(cid)
        pg.click(f'.titem[data-i="{i}"]'); pg.clock.run_for(16)
        t0 = pg.evaluate('performance.now()')
        rows = []
        for k in range(400):
            pg.clock.run_for(50)
            s = pg.evaluate("""()=>({end:!document.getElementById('endcard').hidden,now:document.getElementById('scrub').getAttribute('aria-valuenow'),st:document.getElementById('bugState').textContent,clk:document.getElementById('bugClock').textContent,card:!document.getElementById('card').hidden})""")
            rows.append(((k+1)*0.05, s))
            if s['end']: break
        t1 = pg.evaluate('performance.now()')
        t = TAC[cid]
        print(cid, 'ended at', rows[-1][0], 'perf elapsed', round((t1-t0)/1000,2), 'expected', round(t['wrong']['real']+1.25+t['right']['real'],2))
        # print transitions
        prev=None
        for tt,s in rows:
            key=(s['st'],s['card'])
            if key!=prev: print('   ', round(tt,2), s); prev=key
    b.close()
