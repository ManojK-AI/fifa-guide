"""Read-only screenshots for visual checks: n26 note box (both themes), AI cards, Plan roles item, keychip notation."""
import sys, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent; WORK = HERE.parent.parent; sys.path.insert(0, str(WORK))
from harness import open_page
SH = HERE / 'shots'
with sync_playwright() as p:
    b = p.chromium.launch()
    for dark in (False, True):
        ctx, pg, errs = open_page(b, 390, 844, dark=dark, game='fc26')
        pg.evaluate("window.__lrrMode('replays')"); pg.wait_for_timeout(200)
        tmap = pg.evaluate("Object.fromEntries([...document.querySelectorAll('.titem')].map(b=>[b.querySelector('.code').textContent,+b.dataset.i]))")
        pg.evaluate(f"window.__lrrShow({tmap['U1']},'right',1.7,'board')"); pg.wait_for_timeout(150)
        pg.locator('#coach').screenshot(path=str(SH / f'coach_U1_{"dark" if dark else "light"}.png'))
        pg.evaluate(f"window.__lrrShow({tmap['D2']},'right',1.0,'board')"); pg.wait_for_timeout(150)
        pg.locator('#coach').screenshot(path=str(SH / f'coach_D2_{"dark" if dark else "light"}.png'))
        if not dark:
            # key chip showing double-tap
            pg.evaluate(f"window.__lrrShow({tmap['U6']},'right',0,'board')")
            # find a time when the key chip is visible
            for ct in [x/10 for x in range(0, 90)]:
                pg.evaluate(f"window.__lrrShow({tmap['U6']},'right',{ct},'board')")
                if not pg.evaluate("document.getElementById('keychip').classList.contains('off')"):
                    break
            pg.locator('#screen').screenshot(path=str(SH / 'keychip_U6.png'))
            pg.evaluate("window.__lrrMode('plan')"); pg.wait_for_timeout(150)
            pg.locator('.checks.g26 li >> nth=10').screenshot(path=str(SH / 'plan_roles_item.png'))
            pg.evaluate("window.__lrrMode('ai')"); pg.wait_for_timeout(150)
            pg.locator('#p-ai .g26 .mcard >> nth=0').screenshot(path=str(SH / 'ai_card1.png'))
            pg.locator('#p-ai .g26 .ai-nums').screenshot(path=str(SH / 'ai_nums_fc26.png'))
        ctx.close()
    b.close()
