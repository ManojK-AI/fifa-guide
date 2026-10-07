from common import *
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx, pg, errs = open_clock(b, 320, 640, pause=True, dark=True)
    pg.click('#mt-replays'); pg.clock.run_for(50)
    i = TIDS.index('A4')
    pg.evaluate(f"window.__lrrShow({i},'right',20,'board')"); pg.evaluate("document.querySelector('#playBtn').click()"); pg.clock.run_for(200)
    pg.locator('#p-replays .stage').screenshot(path=str(SHOTS / 'endcard_A4_320_dark.png'))
    pg.locator('#p-replays .layout').screenshot(path=str(SHOTS / 'replays_layout_320_dark.png'))
    ctx.close()
    b.close()
