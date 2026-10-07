from common import *
from playwright.sync_api import sync_playwright
T = lambda pg, sel: pg.evaluate(f"document.querySelector('{sel}').textContent")
with sync_playwright() as p:
    b = p.chromium.launch()
    for step in (16, 17, 25, 33, 50, 100, 250):
        ctx, pg, errs = open_clock(b, 1280, 900, game='fc26', pause=True)
        pg.click('#tstart'); pg.clock.run_for(50)
        p0 = pg.evaluate('performance.now()')
        k = 0
        while T(pg, '#twho') != 'Your call' and k < 4000 // step:
            pg.clock.run_for(step); k += 1
        p1 = pg.evaluate('performance.now()')
        print('step', step, 'reached ask:', T(pg, '#twho') == 'Your call', 'after', round(p1 - p0), 'ms fake time')
        ctx.close()
    b.close()
