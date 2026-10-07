from common import *
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx, pg, errs = open_clock(b, 1280, 900)
    pg.evaluate("window.__lrrMode('replays')")
    pg.clock.run_for(100)
    s0 = pg.evaluate(STATE_JS)
    t0 = time.time()
    pg.clock.run_for(3000)
    s1 = pg.evaluate(STATE_JS)
    print('real secs for 3s sim', round(time.time()-t0,2))
    print(s0); print(s1)
    print(errs)
    b.close()
