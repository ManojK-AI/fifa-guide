from common import *
from playwright.sync_api import sync_playwright
T = lambda pg, sel: pg.evaluate(f"document.querySelector('{sel}').textContent")
def run(b, scroll, step, pause=True):
    ctx, pg, errs = open_clock(b, 1280, 900, game='fc26', pause=pause)
    pg.click('#mt-ai'); pg.clock.run_for(50)
    btn = pg.locator('#p-ai [data-drill="def"]:visible')
    if scroll: pg.evaluate("window.scrollTo(0, 600)")
    y0 = pg.evaluate('scrollY')
    btn.click(); pg.clock.run_for(50)
    k = 0
    while T(pg, '#twho') != 'Your call' and k < 3000 // step:
        pg.clock.run_for(step); k += 1
    print('scroll', scroll, 'y0', y0, 'step', step, 'reached ask:', T(pg, '#twho') == 'Your call', 'scrollY now', pg.evaluate('scrollY'), 'stage top', round(pg.evaluate("document.querySelector('#p-trainer .stage').getBoundingClientRect().top")), errs[:2])
    ctx.close()
with sync_playwright() as p:
    b = p.chromium.launch()
    for scroll in (False, True):
        for step in (25, 250):
            run(b, scroll, step)
    run(b, True, 25, pause=False)
    b.close()
