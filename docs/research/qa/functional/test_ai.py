"""5. AI moves: every visible .clip-ref opens the right clip in Replays; both Drill buttons start the trainer with the right focus, in each game."""
from common import *
from playwright.sync_api import sync_playwright
L = Log('ai')
T = lambda pg, sel: pg.evaluate(f"document.querySelector('{sel}').textContent")
with sync_playwright() as p:
    b = p.chromium.launch()
    for game in ('fc26', 'fc23'):
        for w in (1280, 390):
            ctx, pg, errs = open_page(b, w, 900 if w > 700 else 844, game=game)
            pg.click('#mt-ai'); pg.wait_for_timeout(700)
            n = pg.evaluate("[...document.querySelectorAll('#p-ai .clip-ref')].filter(e=>e.checkVisibility()).length")
            for k in range(n):
                pg.click('#mt-ai'); pg.wait_for_timeout(40)
                ref = pg.locator('#p-ai .clip-ref:visible').nth(k)
                cid = ref.get_attribute('data-clip'); card = ref.evaluate("e=>e.closest('.mcard').querySelector('h4').textContent")
                ref.scroll_into_view_if_needed(); ref.click(); pg.wait_for_timeout(700)
                st = pg.evaluate(STATE_JS)
                L.check(st['active'] == 'replays' and st['bug'] == cid and st['cur'] == cid, f'{game}/{w}: AI ref {cid} ({card[:30]}) opens Replays on {cid}', (st['active'], st['bug'], st['cur']))
                L.check(st['coachT'] == TAC[cid]['name'] and st['state'] == 'Wrong' and st['play'] == 'Pause', f'{game}/{w}: {cid} starts from the wrong way, playing', (st['coachT'], st['state'], st['play']))
                top = pg.evaluate("document.querySelector('#p-replays .stage').getBoundingClientRect().top")
                L.check(top >= -1, f'{game}/{w}: replay stage scrolled into view after {cid}', top)
                L.check(pg.evaluate("document.getElementById('cN26').checkVisibility()") == (game == 'fc26' and bool(F26.get(cid, {}).get('n'))), f'{game}/{w}: {cid} FC 26 note state')
            L.note(f'{game}/{w}: tested {n} clip refs')
            # drill buttons
            for focus in ('def', 'att'):
                pg.click('#mt-ai'); pg.wait_for_timeout(40)
                btn = pg.locator(f'#p-ai [data-drill="{focus}"]:visible')
                L.check(btn.count() == 1, f'{game}/{w}: one visible drill button for {focus}', btn.count())
                btn.scroll_into_view_if_needed(); btn.click(); pg.wait_for_timeout(700)
                L.check(pg.get_attribute('#mt-trainer', 'aria-selected') == 'true', f'{game}/{w}: drill {focus} opens the trainer')
                L.check(pg.get_attribute(f'[data-tf="{focus}"]', 'aria-pressed') == 'true', f'{game}/{w}: drill {focus} sets focus button')
                L.check(not pg.is_visible('#tintro') and T(pg, '#twho') == 'Read' and T(pg, '#tbCode') == '1/10', f'{game}/{w}: drill {focus} starts a round immediately', (T(pg, '#twho'), T(pg, '#tbCode')))
                top = pg.evaluate("document.querySelector('#p-trainer .stage').getBoundingClientRect().top")
                L.check(top >= -1, f'{game}/{w}: trainer stage in view after drill', top)
                L.check(pg.evaluate("localStorage.getItem('lrr:tfocus')") == focus, f'{game}/{w}: focus stored')
                # play the round, identify each scene from the feedback, check side
                sides = []
                for n2 in range(10):
                    for _ in range(200):
                        if T(pg, '#twho') == 'Your call': break
                        pg.wait_for_timeout(25)
                    a = pg.evaluate("window.__lrrAnsPt()"); pg.mouse.click(a[0], a[1]); pg.wait_for_timeout(40)
                    say = T(pg, '#tsay')
                    sid = next((s['id'] for s in DATA['scenes'] if say.endswith(gfb(s['id'], game))), None)
                    sides.append((sid, SC[sid]['side'] if sid else None))
                    pg.click('#tnext'); pg.wait_for_timeout(40)
                L.check(all(sd == focus for _, sd in sides) and len({s for s, _ in sides}) == 10, f'{game}/{w}: drill {focus} round has only {focus} scenes', sides)
                L.check(T(pg, '#tsK').endswith({'def': 'Their ball', 'att': 'Your ball'}[focus]), f'{game}/{w}: summary names the focus', T(pg, '#tsK'))
            L.check(not errs, f'{game}/{w}: no console errors', errs[:4])
            ctx.close()
    b.close()
L.dump()
