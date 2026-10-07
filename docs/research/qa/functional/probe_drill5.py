from common import *
from playwright.sync_api import sync_playwright
T = lambda pg, sel: pg.evaluate(f"document.querySelector('{sel}').textContent")
with sync_playwright() as p:
    b = p.chromium.launch()
    for variant in ('siv', 'nosiv'):
        ctx, pg, errs = open_clock(b, 1280, 900, game='fc26', pause=True)
        pg.click('#mt-ai'); pg.clock.run_for(30)
        btn = pg.locator('#p-ai [data-drill="def"]:visible')
        if variant == 'siv': btn.scroll_into_view_if_needed()
        btn.click(); pg.clock.run_for(50)
        p0 = pg.evaluate('performance.now()')
        k = 0
        while T(pg, '#twho') != 'Your call' and k < 120:
            pg.clock.run_for(25); k += 1
        p1 = pg.evaluate('performance.now()')
        print(variant, 'reached', T(pg, '#twho'), 'fake ms', round(p1 - p0), 'k', k)
        ctx.close()
    b.close()
