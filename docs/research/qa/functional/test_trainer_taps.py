"""4a. Exhaustive: every scene (x flip x camera x width) - a real tap at __lrrAnsPt() scores Right; wrong/timeout feedback text per game via the debug hook."""
from common import *
from playwright.sync_api import sync_playwright
L = Log('trainer_taps')
CAST = json.loads((QA / 'scenes_cast.json').read_text())
WRONG = {'predict': 'Not that one. ', 'mate': 'Not that one. ', 'spot': 'Not there. ', 'switch': 'Not him. ', 'lane': 'Not in the lane. ', 'choice': 'Not this time. '}
with sync_playwright() as p:
    b = p.chromium.launch()
    for w, h in ((390, 844), (1280, 900), (320, 640)):
        ctx, pg, errs = open_page(b, w, h)
        for view in ('board', 'cam'):
            for i, s in enumerate(DATA['scenes']):
                for flip in (False, True):
                    pg.evaluate(f"window.__lrrTrain({i},{str(flip).lower()},'ask',null,'{view}')")
                    pt = pg.evaluate("window.__lrrAnsPt()")
                    if s['type'] == 'choice':
                        pg.click(f'.tchoice[data-c="{s["ans"]}"]')
                    else:
                        # make sure the point is on screen
                        pg.evaluate(f"window.scrollTo(0, Math.max(0, {pt[1]} + window.scrollY - 300))")
                        pt = pg.evaluate("window.__lrrAnsPt()")
                        inside = pg.evaluate(f"""(()=>{{const r=document.getElementById('tcv').getBoundingClientRect();return {pt[0]}>=r.left&&{pt[0]}<=r.right&&{pt[1]}>=r.top&&{pt[1]}<=r.bottom}})()""")
                        L.check(inside, f'{w}/{view}/{s["id"]}{"f" if flip else ""}: answer point inside canvas', pt)
                        pg.mouse.click(pt[0], pt[1])
                    v = pg.inner_text('#tverdict') if pg.is_visible('#tverdict') else '(none)'
                    L.check(v.startswith('Right') or v.startswith('RIGHT'), f'{w}/{view}/{s["id"]}{"f" if flip else ""}: tap on the answer scores Right', (v, pg.inner_text('#tsay')[:80]))
        L.check(not errs, f'{w}: no console errors', errs[:3])
        ctx.close()
    # feedback text per game: right, wrong (decoys and generic), timeout - via hook, flipped and not
    for game in ('fc26', 'fc23'):
        ctx, pg, errs = open_page(b, 1280, 900, game=game)
        for i, s in enumerate(DATA['scenes']):
            sid = s['id']; fb = gfb(sid, game)
            for flip in (False, True):
                c = CAST[sid + ('f' if flip else '')]
                pg.evaluate(f"window.__lrrTrain({i},{str(flip).lower()},'reveal','right','board')")
                L.check(pg.text_content('#tsay') == fb, f'{game}/{sid}{"f" if flip else ""}: right feedback', pg.text_content('#tsay'))
                pg.evaluate(f"window.__lrrTrain({i},{str(flip).lower()},'reveal','timeout','board')")
                L.check(pg.text_content('#tsay') == 'Decide before the ball gets there. ' + fb and pg.text_content('#tverdict') == 'Too slow', f'{game}/{sid}: timeout feedback')
                for pid, txt in list(c['decoy'].items())[:3]:
                    pg.evaluate(f"window.__lrrTrain({i},{str(flip).lower()},'reveal','{pid}','board')")
                    want = txt + fb
                    if s['type'] in ('spot', 'lane'):
                        want = None  # string picks are treated as id hits only for player types
                    got = pg.text_content('#tsay')
                    if want: L.check(got == want, f'{game}/{sid}{"f" if flip else ""}: decoy {pid} feedback', got)
                wb = pg.evaluate("document.getElementById('tclip').hidden")
                L.check(wb == (not s.get('clip')), f'{game}/{sid}: Watch button shown iff clip', wb)
                if s.get('clip'):
                    L.check(pg.text_content('#tclip') == '▶ Watch ' + s.get('clip') and pg.get_attribute('#tclip', 'data-clip') == s.get('clip'), f'{game}/{sid}: Watch button text')
        L.check(not errs, f'{game}: no console errors (feedback sweep)', errs[:3])
        ctx.close()
    b.close()
L.dump()
