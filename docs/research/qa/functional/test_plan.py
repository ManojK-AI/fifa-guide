"""6. Plan: checkbox persistence per game, count, Clear only visible game, clip buttons, links inside labels."""
from common import *
from playwright.sync_api import sync_playwright
L = Log('plan')
VIS = "[...document.querySelectorAll('[data-chk]')].filter(c=>c.checkVisibility()).map(c=>[c.dataset.chk,c.checked])"
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx, pg, errs = open_page(b, 1280, 900)
    pg.click('#mt-plan'); pg.wait_for_timeout(100)
    v26 = pg.evaluate(VIS)
    L.check(len(v26) == 12 and all(k.startswith('f26-') for k, _ in v26), 'fc26: 12 f26- boxes visible', [k for k, _ in v26])
    for k in ('f26-cam', 'f26-def', 'f26-warm'):
        pg.click(f'[data-chk="{k}"]')
    L.check(pg.text_content('#chkCount') == '3 of 12 done', 'fc26 count after 3 ticks', pg.text_content('#chkCount'))
    # clicking the label text toggles, clicking the source link inside the label does not
    pg.click('[data-chk="f26-radar"] + span b'); pg.wait_for_timeout(50)
    L.check(pg.is_checked('[data-chk="f26-radar"]'), 'clicking label text ticks the box')
    pg.click('[data-chk="f26-radar"] + span b')
    with ctx.expect_page() as newp:
        pg.click('[data-chk="f26-lock"] + span a.src >> nth=0')
    newp.value.close()
    L.check(not pg.is_checked('[data-chk="f26-lock"]'), 'clicking a source link inside a label does not tick it')
    L.check(pg.text_content('#chkCount') == '3 of 12 done', 'count unchanged by link click', pg.text_content('#chkCount'))
    stored = pg.evaluate("Object.keys(localStorage).filter(k=>k.startsWith('lrr:chk:')).sort().map(k=>k+'='+localStorage.getItem(k))")
    L.note(f'storage after fc26 ticks: {stored}')
    # switch to FIFA 23
    pg.click('[data-gm="fc23"]'); pg.wait_for_timeout(50)
    v23 = pg.evaluate(VIS)
    L.check(len(v23) == 11 and not any(k.startswith('f26-') for k, _ in v23), 'fc23: 11 boxes visible', [k for k, _ in v23])
    L.check(pg.text_content('#chkCount') == '0 of 11 done', 'fc23 count ignores fc26 ticks', pg.text_content('#chkCount'))
    for k in ('cam', 'timed'):
        pg.click(f'[data-chk="{k}"]')
    L.check(pg.text_content('#chkCount') == '2 of 11 done', 'fc23 count after 2 ticks', pg.text_content('#chkCount'))
    pg.click('#chkReset'); pg.wait_for_timeout(50)
    L.check(pg.text_content('#chkCount') == '0 of 11 done', 'Clear in fc23 clears fc23', pg.text_content('#chkCount'))
    pg.click('[data-chk="runs"]')
    pg.click('[data-gm="fc26"]'); pg.wait_for_timeout(50)
    L.check(pg.text_content('#chkCount') == '3 of 12 done', 'fc26 ticks survive fc23 Clear', pg.text_content('#chkCount'))
    # reload persistence
    pg.reload(); pg.wait_for_timeout(300)
    pg.click('#mt-plan')
    L.check(pg.text_content('#chkCount') == '3 of 12 done', 'fc26 ticks persist after reload', pg.text_content('#chkCount'))
    L.check(sorted(k for k, c in pg.evaluate(VIS) if c) == ['f26-cam', 'f26-def', 'f26-warm'], 'exact fc26 boxes persist')
    pg.click('[data-gm="fc23"]')
    L.check(pg.text_content('#chkCount') == '1 of 11 done' and pg.is_checked('[data-chk="runs"]'), 'fc23 tick persists after reload', pg.text_content('#chkCount'))
    pg.click('[data-gm="fc26"]'); pg.click('#chkReset'); pg.wait_for_timeout(50)
    L.check(pg.text_content('#chkCount') == '0 of 12 done', 'Clear in fc26', pg.text_content('#chkCount'))
    pg.click('[data-gm="fc23"]')
    L.check(pg.text_content('#chkCount') == '1 of 11 done', 'fc26 Clear leaves fc23 tick', pg.text_content('#chkCount'))
    # keyboard: space toggles a focused checkbox
    pg.focus('[data-chk="pzoom"]'); pg.keyboard.press('Space')
    L.check(pg.is_checked('[data-chk="pzoom"]') and pg.text_content('#chkCount') == '2 of 11 done', 'Space toggles a focused checkbox', pg.text_content('#chkCount'))
    # count text before JS? initial static text
    L.check(not errs, 'no console errors', errs[:4])
    # clip buttons in Plan, both games
    for game in ('fc26', 'fc23'):
        pg.click(f'[data-gm="{game}"]')
        pg.click('#mt-plan')
        refs = pg.evaluate("[...document.querySelectorAll('#p-plan .clip-ref')].filter(e=>e.checkVisibility()).map(e=>e.dataset.clip)")
        for k, cid in enumerate(refs):
            pg.click('#mt-plan'); pg.wait_for_timeout(30)
            pg.locator('#p-plan .clip-ref:visible').nth(k).click(); pg.wait_for_timeout(80)
            st = pg.evaluate(STATE_JS)
            L.check(st['active'] == 'replays' and st['bug'] == cid and st['cur'] == cid, f'{game}: plan clip {cid} opens it', (st['active'], st['bug']))
        L.note(f'{game}: plan clip refs {refs}')
    L.check(not errs, 'no console errors (clip refs)', errs[:4])
    ctx.close()
    b.close()
L.dump()
