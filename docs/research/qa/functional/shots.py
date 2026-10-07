"""Screenshots for visual review."""
from common import *
from playwright.sync_api import sync_playwright
S = SHOTS
def el(pg, sel, name):
    pg.locator(sel).first.screenshot(path=str(S / name))
with sync_playwright() as p:
    b = p.chromium.launch()
    # 1. phone masthead + trainer
    for w, h, dark, game in ((390, 844, False, 'fc26'), (320, 640, False, 'fc26'), (390, 844, True, 'fc26'), (390, 844, False, 'fc23')):
        t = f'{w}_{"dark" if dark else "light"}_{game}'
        ctx, pg, errs = open_page(b, w, h, dark=dark, game=game)
        pg.screenshot(path=str(S / f'm_top_{t}.png'))
        pg.evaluate("window.__lrrTrain(12,false,'ask',null,'board')"); pg.wait_for_timeout(200)
        el(pg, '#p-trainer .stage', f'm_trainer_ask_choice_{t}.png')
        pg.evaluate("window.__lrrTrain(16,false,'ask',null,'cam')"); pg.wait_for_timeout(200)
        el(pg, '#p-trainer .stage', f'm_trainer_ask_tap_cam_{t}.png')
        pg.evaluate("window.__lrrTrain(22,false,'reveal',null,'board')"); pg.wait_for_timeout(300)
        el(pg, '#p-trainer .stage', f'm_trainer_reveal_{t}.png')
        pg.evaluate("window.__lrrTrain(9,false,'reveal','timeout','board')"); pg.wait_for_timeout(200); pg.click('#tnext'); pg.wait_for_timeout(300)
        el(pg, '#p-trainer .tmain', f'm_trainer_summary_{t}.png')
        ctx.close()
    # 2. AI header + first cards
    for w, h, dark, game in ((390, 844, False, 'fc26'), (390, 844, False, 'fc23'), (320, 640, True, 'fc26'), (820, 1180, False, 'fc26')):
        t = f'{w}_{"dark" if dark else "light"}_{game}'
        ctx, pg, errs = open_page(b, w, h, dark=dark, game=game)
        pg.evaluate("window.__lrrMode('ai')"); pg.wait_for_timeout(200)
        sel = '#p-ai .g26' if game == 'fc26' else '#p-ai .g23'
        el(pg, f'{sel} .ai-head', f'm_ai_head_{t}.png')
        pg.locator(f'{sel} .ai-sec').first.screenshot(path=str(S / f'm_ai_sec1_{t}.png'))
        ctx.close()
    # 3. coach cards + screen with key chip
    for w, h, dark, game in ((390, 844, False, 'fc26'), (390, 844, False, 'fc23'), (320, 640, False, 'fc26'), (320, 640, True, 'fc23')):
        t = f'{w}_{"dark" if dark else "light"}_{game}'
        ctx, pg, errs = open_page(b, w, h, dark=dark, game=game)
        for cid in ('U1', 'U4', 'U6', 'D2', 'A6'):
            i = TIDS.index(cid)
            k = TAC[cid]['right']['key'][0][0] if TAC[cid]['right']['key'] else 1.0
            pg.evaluate(f"window.__lrrShow({i},'right',{k + 0.2},'board')"); pg.wait_for_timeout(250)
            el(pg, '#coach', f'm_coach_{cid}_{t}.png')
            el(pg, '#p-replays .stage', f'm_screen_{cid}_{t}.png')
        ctx.close()
    # 4. Plan checklist
    for w, h, dark, game in ((390, 844, False, 'fc26'), (390, 844, False, 'fc23'), (320, 640, True, 'fc26')):
        t = f'{w}_{"dark" if dark else "light"}_{game}'
        ctx, pg, errs = open_page(b, w, h, dark=dark, game=game)
        pg.evaluate("window.__lrrMode('plan')"); pg.wait_for_timeout(200)
        pg.click('[data-chk="f26-cam"]' if game == 'fc26' else '[data-chk="cam"]')
        el(pg, '#p-plan .pcard.pwide', f'm_plan_checks_{t}.png')
        ctx.close()
    # 5. desktop dark AI and Plan (full page) + light replays
    for game in ('fc26', 'fc23'):
        ctx, pg, errs = open_page(b, 1280, 900, dark=True, game=game)
        pg.evaluate("window.__lrrMode('ai')"); pg.wait_for_timeout(250)
        pg.screenshot(path=str(S / f'd_dark_ai_{game}.png'), full_page=True)
        pg.evaluate("window.__lrrMode('plan')"); pg.wait_for_timeout(250)
        pg.screenshot(path=str(S / f'd_dark_plan_{game}.png'), full_page=True)
        pg.evaluate("window.__lrrMode('replays')"); pg.evaluate(f"window.__lrrShow({TIDS.index('U6')},'right',1.0,'cam')"); pg.wait_for_timeout(250)
        pg.screenshot(path=str(S / f'd_dark_replays_{game}.png'))
        pg.evaluate("window.__lrrMode('trainer')"); pg.wait_for_timeout(250)
        pg.screenshot(path=str(S / f'd_dark_trainer_{game}.png'))
        ctx.close()
    for w in (820, 1280):
        ctx, pg, errs = open_page(b, w, 1000, game='fc26')
        pg.evaluate("window.__lrrMode('replays')"); pg.evaluate(f"window.__lrrShow({TIDS.index('C4')},'right',1.8,'board')"); pg.wait_for_timeout(250)
        pg.screenshot(path=str(S / f'replays_C4_{w}.png'), full_page=True)
        pg.evaluate("window.__lrrMode('plan')"); pg.wait_for_timeout(200)
        pg.screenshot(path=str(S / f'plan_{w}_fc26.png'), full_page=True)
        ctx.close()
    b.close()
print('done')
