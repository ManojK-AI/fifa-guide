from common import *
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx, pg, errs = open_page(b, 1280, 900, game='fc26')
    pg.click('#reelBtn'); pg.wait_for_timeout(10500)
    s1 = pg.evaluate(STATE_JS)
    pg.click('#mt-plan'); pg.wait_for_timeout(300)
    lab = pg.text_content('#reelLabel'); sub = pg.text_content('#reelSub')
    pg.click('#reelBtn'); pg.wait_for_timeout(400)
    s2 = pg.evaluate(STATE_JS)
    print('before leaving:', s1['bug'], s1['reelSub'], '| on Plan the button reads:', lab, '/', sub)
    print('after clicking it from Plan:', s2['active'], s2['bug'], s2['reelLabel'], s2['reelSub'], s2['cardK'], s2['card'])
    # 'Try next speed' button from the summary
    pg.click('#mt-trainer'); pg.click('[data-lv="leg"]')
    pg.evaluate("window.__lrrTrain(0,false,'reveal',null,'board')"); pg.click('#tnext'); pg.wait_for_timeout(200)
    pg.click('#tsRow button[data-ta="up"]'); pg.wait_for_timeout(200)
    print('Try next speed ->', pg.get_attribute('[data-lv="ult"]', 'aria-pressed'), pg.text_content('#tbName'), pg.text_content('#twho'), pg.text_content('#tbCode'))
    print(errs)
    b.close()
