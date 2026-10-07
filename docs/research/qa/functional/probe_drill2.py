from common import *
from playwright.sync_api import sync_playwright
T = lambda pg, sel: pg.evaluate(f"document.querySelector('{sel}').textContent")
with sync_playwright() as p:
    b = p.chromium.launch()
    for w in (1280, 390):
        ctx, pg, errs = open_clock(b, w, 900 if w > 700 else 844, game='fc26', pause=True)
        for focus in ('def', 'att'):
            pg.click('#mt-ai'); pg.clock.run_for(30)
            btn = pg.locator(f'#p-ai [data-drill="{focus}"]:visible'); btn.scroll_into_view_if_needed(); btn.click(); pg.clock.run_for(50)
            for n2 in range(10):
                for _ in range(200):
                    if T(pg, '#twho') == 'Your call': break
                    pg.clock.run_for(25)
                a = pg.evaluate("window.__lrrAnsPt()")
                if a is None:
                    print(w, focus, n2, 'NONE', T(pg, '#twho'), T(pg, '#tbCode'), T(pg, '#tsay')[:80]); break
                vh = pg.evaluate('innerHeight')
                pg.mouse.click(a[0], a[1]); pg.clock.run_for(30)
                print(w, focus, n2, [round(x) for x in a], 'vh', vh, '->', T(pg, '#twho'), T(pg, '#tbCode'))
                pg.click('#tnext'); pg.clock.run_for(30)
        ctx.close()
    b.close()
