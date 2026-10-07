from common import *
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    for game in ('fc26', 'fc23'):
        for w, h in ((390, 844), (320, 640), (820, 1180), (1280, 900)):
            for focus in ('def', 'att'):
                for prior in ('intro', 'summary'):
                    ctx, pg, errs = open_page(b, w, h, game=game)
                    if prior == 'summary':
                        # put the trainer in summary state first
                        pg.evaluate("window.__lrrTrain(0,false,'reveal',null,'board')"); pg.click('#tnext'); pg.wait_for_timeout(100)
                    pg.click('#mt-ai'); pg.wait_for_timeout(100)
                    btn = pg.locator(f'#p-ai [data-drill="{focus}"]:visible'); btn.scroll_into_view_if_needed()
                    y0 = pg.evaluate('scrollY')
                    btn.click(); pg.wait_for_timeout(1500)
                    r = pg.evaluate("(()=>{const s=document.querySelector('#p-trainer .stage').getBoundingClientRect();return [Math.round(s.top),Math.round(s.bottom),innerHeight,Math.round(scrollY),document.documentElement.scrollHeight]})()")
                    ok = r[0] >= -2 and r[0] < r[2]
                    print(game, w, focus, prior, 'scrollY before', y0, 'stage top/bottom', r[:2], 'vh', r[2], 'scrollY', r[3], 'docH', r[4], 'OK' if ok else 'STAGE OFF-SCREEN')
                    ctx.close()
    b.close()
