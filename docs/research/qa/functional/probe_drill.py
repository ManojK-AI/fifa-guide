from common import *
from playwright.sync_api import sync_playwright
T = lambda pg, sel: pg.evaluate(f"document.querySelector('{sel}').textContent")
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx, pg, errs = open_clock(b, 1280, 900, game='fc26', pause=True)
    pg.click('#mt-ai'); pg.clock.run_for(50)
    btn = pg.locator('#p-ai [data-drill="def"]:visible'); btn.click(); pg.clock.run_for(50)
    for k in range(12):
        pg.clock.run_for(250)
        print(k, T(pg, '#twho'), T(pg, '#tbCode'), T(pg, '#tsay')[:60], pg.evaluate("window.__lrrAnsPt()"))
    print(errs)
    b.close()
