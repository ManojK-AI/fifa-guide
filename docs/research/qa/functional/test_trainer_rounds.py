"""4b. Full 10-scene rounds by tapping the real canvas (fake clock): right taps, wrong taps, a timeout, empty taps.
Checks scoring, bug, verdicts, feedback per game, summary, Work on these, Watch buttons, best score per level."""
from common import *
from playwright.sync_api import sync_playwright
L = Log('trainer_rounds')
CAST = json.loads((QA / 'scenes_cast.json').read_text())
WRONG = {'predict': 'Not that one. ', 'mate': 'Not that one. ', 'spot': 'Not there. ', 'switch': 'Not him. ', 'lane': 'Not in the lane. ', 'choice': 'Not this time. '}
LV = {'wc': ('World Class', 3.0), 'leg': ('Legendary', 2.2), 'ult': ('Ultimate', 1.4)}
FOC = {'all': 'All reads', 'def': 'Their ball', 'att': 'Your ball'}
ALL_IDS = sorted({pid for c in CAST.values() for pid in c['cast']})
T = lambda pg, sel: pg.evaluate(f"document.querySelector('{sel}').textContent")

def wait_phase(pg, who, limit=6000):
    for _ in range(limit // 25):
        if T(pg, '#twho') in who: return True
        pg.clock.run_for(25)
    return False

def ensure_canvas(pg):
    pg.evaluate("""(()=>{const c=document.getElementById('tcv'),r=c.getBoundingClientRect(),ch=document.getElementById('tchoices').getBoundingClientRect();
      if(r.top<0||Math.max(r.bottom,ch.bottom)>innerHeight)c.closest('.stage').scrollIntoView({block:'start'});})()""")

def identify(text, game, lead_opts):
    for s in DATA['scenes']:
        fb = gfb(s['id'], game)
        if text.endswith(fb):
            return s['id'], text[:-len(fb)]
    return None, None

def play_round(pg, game, level, focus, view, plan, tag):
    """plan: list of 'R' (right tap), 'W' (wrong tap), 'T' (timeout), 'E' (empty tap then right)."""
    for sel in (f'[data-lv="{level}"]', f'[data-tf="{focus}"]', f'[data-tv="{view}"]'):
        pg.click(sel)
    pg.clock.run_for(50)
    L.check(T(pg, '#tiK') == 'Scan trainer · ' + {'all': 'All reads', 'def': 'Their ball: read the AI', 'att': 'Your ball: break the AI'}[focus], f'{tag}: intro kicker', T(pg, '#tiK'))
    L.check(T(pg, '#tiTime') == f'{LV[level][1]:.1f} seconds', f'{tag}: intro time', T(pg, '#tiTime'))
    if pg.is_visible('#tsum'):
        L.note(f'{tag}: started from the summary with Go again (level/focus/camera changed while the summary was up)')
        pg.click('#tsRow button[data-ta="again"]')
    else:
        pg.click('#tstart')
    seen, score, missed, results = [], 0, [], []
    for n in range(10):
        ok = wait_phase(pg, ('Your call',))
        L.check(ok, f'{tag}: scene {n+1} reaches ask phase')
        L.check(T(pg, '#tbCode') == f'{n+1}/10', f'{tag}: bug scene counter', T(pg, '#tbCode'))
        ensure_canvas(pg)
        ask = T(pg, '#tsay'); act = plan[n]
        typ = 'choice' if pg.is_visible('#tchoices') else ('predict' if 'their player' in ask else 'player' if 'Tap the player' in ask else 'area')
        ans = pg.evaluate("window.__lrrAnsPt()")
        if ans is None:
            L.check(False, f'{tag}: scene {n+1}: no answer point in ask phase', (ok, T(pg, '#twho'), T(pg, '#tsay'), T(pg, '#tbCode'), pg.is_visible('#tsum'), pg.is_visible('#tintro')))
            return None
        pick = None
        if act == 'E' and typ != 'choice':
            r = pg.locator('#tcv').bounding_box()
            # find an empty spot: sample a grid, pick the point farthest from every player
            pts = [p for p in (pg.evaluate(f"window.__lrrAnsPt('{pid}')") for pid in ALL_IDS) if p]
            best = max(((r['x'] + r['width'] * fx / 10, r['y'] + r['height'] * fy / 10) for fx in range(1, 10) for fy in range(2, 10)),
                       key=lambda q: min(((q[0] - a[0]) ** 2 + (q[1] - a[1]) ** 2) ** .5 for a in pts + [ans]))
            if typ in ('predict', 'player'):
                pg.mouse.click(*best); pg.clock.run_for(30)
                L.check(T(pg, '#twho') == 'Your call' and T(pg, '#tsay').startswith('Tap'), f'{tag}: empty tap gives a hint, keeps asking', T(pg, '#tsay'))
                pg.clock.run_for(1600)
                L.check(T(pg, '#tsay') == ask, f'{tag}: hint reverts to the question after 1.5 s', T(pg, '#tsay'))
            act = 'R'
        if act == 'E' and typ == 'choice':
            r = pg.locator('#tcv').bounding_box(); pg.mouse.click(r['x'] + r['width'] / 2, r['y'] + r['height'] / 2); pg.clock.run_for(30)
            L.check(T(pg, '#tsay') == 'Pick one of the buttons under the pitch.', f'{tag}: canvas tap on a choice question hints', T(pg, '#tsay'))
            act = 'R'
        pg.clock.run_for(300)  # think time
        if act == 'R':
            if typ == 'choice':
                pg.mouse.click(ans[0], ans[1])
            else:
                pg.mouse.click(ans[0], ans[1])
        elif act == 'W':
            if typ == 'choice':
                for c in range(3):
                    bb = pg.locator(f'.tchoice[data-c="{c}"]').bounding_box()
                    if abs(bb['x'] + bb['width'] / 2 - ans[0]) > 5:
                        pg.mouse.click(bb['x'] + bb['width'] / 2, bb['y'] + bb['height'] / 2); pick = c; break
            elif typ in ('predict', 'player'):
                cands = []
                for pid in ALL_IDS:
                    if pid in ('gk', 'xgk'): continue
                    if (typ == 'predict') != pid.startswith('x'): continue
                    q = pg.evaluate(f"window.__lrrAnsPt('{pid}')")
                    if q and ((q[0] - ans[0]) ** 2 + (q[1] - ans[1]) ** 2) ** .5 > 60: cands.append((pid, q))
                for pid, q in cands:
                    pg.mouse.click(q[0], q[1]); pg.clock.run_for(20)
                    if T(pg, '#twho') != 'Your call': pick = pid; break
            else:
                r = pg.locator('#tcv').bounding_box()
                q = (r['x'] + (r['width'] * 0.1 if ans[0] > r['x'] + r['width'] / 2 else r['width'] * 0.9), r['y'] + r['height'] * 0.5)
                pg.mouse.click(*q)
        elif act == 'T':
            pg.clock.run_for(int(LV[level][1] * 1000) + 200)
        pg.clock.run_for(30)
        who = T(pg, '#twho'); verdict = T(pg, '#tverdict'); say = T(pg, '#tsay')
        sid, lead = identify(say, game, None)
        L.check(sid is not None, f'{tag}: scene {n+1} feedback is the {game} text of a known scene', say[:90])
        if sid is None: return None
        seen.append(sid); s = SC[sid]
        if act == 'R':
            L.check(who == 'Right' and verdict.startswith('Right') and lead == '', f'{tag}: {sid} right tap -> Right', (who, verdict, lead))
            score += 1
        elif act == 'W':
            want = {WRONG[s['type']]} | {CAST[sid][k] if False else v for k2 in (sid, sid + 'f') for kk, v in CAST[k2]['decoy'].items() if kk == pick}
            L.check(who == 'Wrong' and verdict == 'Wrong' and lead in want, f'{tag}: {sid} wrong tap ({pick}) -> Wrong with right lead', (who, verdict, lead))
            missed.append(sid)
        else:
            L.check(who == 'Too slow' and verdict == 'Too slow' and lead == 'Decide before the ball gets there. ' and T(pg, '#tbClock') == '0.0', f'{tag}: {sid} timeout', (who, verdict, lead))
            missed.append(sid)
        L.check(T(pg, '#tbScore') == f'✓ {score}', f'{tag}: score bug after scene {n+1}', T(pg, '#tbScore'))
        if focus != 'all':
            L.check(s['side'] == focus, f'{tag}: {sid} matches focus {focus}', s['side'])
        wb_hidden = pg.evaluate("document.getElementById('tclip').hidden")
        L.check(wb_hidden == (not s.get('clip')) and (not s.get('clip') or T(pg, '#tclip') == '▶ Watch ' + s.get('clip')), f'{tag}: {sid} Watch button', T(pg, '#tclip'))
        nx = T(pg, '#tnext')
        L.check(nx == ('See score →' if n == 9 else 'Next →'), f'{tag}: next label scene {n+1}', nx)
        results.append((sid, act, pick))
        pg.click('#tnext'); pg.clock.run_for(30)
    L.check(len(set(seen)) == 10, f'{tag}: 10 different scenes', seen)
    return seen, score, missed, results

def check_summary(pg, tag, level, focus, score, missed, prev_best):
    L.check(pg.is_visible('#tsum'), f'{tag}: summary shown')
    L.check(T(pg, '#tsScore') == f'{score}/10', f'{tag}: summary score', T(pg, '#tsScore'))
    L.check(T(pg, '#tsK') == f'Round done · {LV[level][0]} speed · {FOC[focus]}', f'{tag}: summary kicker', T(pg, '#tsK'))
    sub = T(pg, '#tsSub')
    L.check(sub.startswith('Average decision ') if score else sub.startswith('No right answers'), f'{tag}: summary sub', sub)
    if prev_best is None:
        L.check(' · ' not in sub, f'{tag}: first round has no best note', sub)
    elif score > prev_best:
        L.check(sub.endswith(' · New best'), f'{tag}: New best note', sub)
    else:
        L.check(sub.endswith(f' · Best {prev_best}/10'), f'{tag}: previous best note', sub)
    nxt = {'wc': 'leg', 'leg': 'ult', 'ult': None}[level]
    if score >= 9: want = 'Sharp. Step up the speed.' if nxt else 'That is Ultimate speed. Now take it into Squad Battles.'
    elif score >= 7: want = 'Good. Go again until you get 9.'
    else: want = 'Learn the tells below, then go again.' if level == 'wc' else 'Drop to a slower speed, learn the tells below, then come back.'
    L.check(T(pg, '#tsVerdict') == want, f'{tag}: verdict for {score}', T(pg, '#tsVerdict'))
    btns = pg.eval_on_selector_all('#tsRow button', 'els=>els.map(b=>b.textContent)')
    L.check(btns == ['Go again'] + ([f'Try {LV[nxt][0]} speed →'] if nxt else []), f'{tag}: summary buttons', btns)
    L.check(T(pg, '#tsay') == f'{score} right out of 10. {want}', f'{tag}: caption after round', T(pg, '#tsay'))
    uniq = list(dict.fromkeys(missed))
    L.check(pg.is_visible('#tmissed') == bool(uniq), f'{tag}: Work on these visible iff misses')
    items = pg.eval_on_selector_all('#tmissedList li', 'els=>els.map(li=>[li.querySelector(".see").textContent,(li.querySelector(".clip-ref")||{}).dataset?(li.querySelector(".clip-ref")||{dataset:{}}).dataset.clip:null])')
    want_items = [[SC[s]['tell'], SC[s].get('clip')] for s in uniq]
    L.check(items == want_items, f'{tag}: Work on these list = missed scenes', (items, want_items))
    best = pg.evaluate(f"localStorage.getItem('lrr:best:{level}')")
    return best

with sync_playwright() as p:
    b = p.chromium.launch()
    configs = [
        ('fc26', 'leg', 'all', 'board', ['R', 'W', 'T', 'R', 'E', 'W', 'R', 'R', 'R', 'R']),
        ('fc26', 'leg', 'def', 'cam',   ['R', 'R', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'R']),
        ('fc26', 'ult', 'att', 'board', ['R', 'R', 'R', 'R', 'T', 'R', 'R', 'R', 'R', 'W']),
        ('fc23', 'leg', 'all', 'board', ['W', 'R', 'R', 'T', 'R', 'R', 'E', 'R', 'W', 'R']),
        ('fc23', 'leg', 'def', 'cam',   ['R', 'W', 'R', 'R', 'R', 'R', 'T', 'R', 'R', 'R']),
        ('fc23', 'ult', 'att', 'cam',   ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']),
    ]
    fb_seen = {'fc26': set(), 'fc23': set()}
    for w in (390,):
        ctx, pg, errs = open_clock(b, w, 844, pause=True)
        bests = {}
        for game, level, focus, view, plan in configs:
            if pg.evaluate("document.documentElement.dataset.game") != game:
                pg.click(f'[data-gm="{game}"]')
            tag = f'{w}/{game}/{level}/{focus}/{view}'
            if pg.is_visible('#tsum'):
                pass
            prev = bests.get(level)
            res = play_round(pg, game, level, focus, view, plan, tag)
            if not res: continue
            seen, score, missed, results = res
            fb_seen[game] |= set(seen)
            exp_score = sum(1 for a in plan if a in ('R', 'E'))
            L.check(score == exp_score, f'{tag}: score as planned', (score, exp_score))
            best = check_summary(pg, tag, level, focus, score, missed, prev)
            want_best = max(score, prev) if prev is not None else score
            L.check(best is not None and best.split('|')[0] == str(want_best), f'{tag}: best stored per level', best)
            bests[level] = want_best
            L.note(f'{tag}: scenes {results}; score {score}; best {best}')
            # Work on these clip button -> Replays, then back
            if pg.is_visible('#tmissedList .clip-ref'):
                cid = pg.get_attribute('#tmissedList .clip-ref', 'data-clip')
                pg.click('#tmissedList .clip-ref'); pg.clock.run_for(100)
                L.check(T(pg, '#bugCode') == cid and pg.get_attribute('#mt-replays', 'aria-selected') == 'true', f'{tag}: Work on these {cid} opens Replays on that clip', T(pg, '#bugCode'))
                pg.click('#mt-trainer'); pg.clock.run_for(100)
                L.check(pg.is_visible('#tsum') and pg.is_visible('#tmissed'), f'{tag}: summary still there after returning')
        # intro best text per level
        pg.click('[data-lv="wc"]'); pg.click('[data-lv="leg"]')
        pg.click('#tsRow button[data-ta="again"]'); pg.clock.run_for(50)
        pg.click('[data-tf="all"]'); pg.clock.run_for(50)   # focus change mid-round returns to intro
        L.check(pg.is_visible('#tintro'), 'changing focus mid-round returns to intro')
        L.check(T(pg, '#tiBest') == f"Your best at Legendary speed: {bests['leg']}/10", 'intro shows best for level', T(pg, '#tiBest'))
        pg.click('[data-lv="ult"]'); pg.clock.run_for(30)
        L.check(T(pg, '#tiBest') == f"Your best at Ultimate speed: {bests['ult']}/10", 'intro best follows level', T(pg, '#tiBest'))
        pg.click('[data-lv="wc"]'); pg.clock.run_for(30)
        L.check(T(pg, '#tiBest') == '', 'no best at World Class yet', T(pg, '#tiBest'))
        # Watch X during reveal -> replays, then back
        pg.click('[data-lv="leg"]'); pg.click('#tstart')
        for _ in range(12):
            wait_phase(pg, ('Your call',)); ensure_canvas(pg); ans = pg.evaluate("window.__lrrAnsPt()"); pg.mouse.click(ans[0], ans[1]); pg.clock.run_for(30)
            if pg.is_visible('#tclip'): break
            pg.click('#tnext')
        cid = pg.get_attribute('#tclip', 'data-clip'); before = T(pg, '#tbCode')
        pg.click('#tclip'); pg.clock.run_for(100)
        L.check(T(pg, '#bugCode') == cid and pg.get_attribute('#mt-replays', 'aria-selected') == 'true', f'Watch {cid} opens Replays on that clip', T(pg, '#bugCode'))
        pg.click('#mt-trainer'); pg.clock.run_for(100)
        L.check(T(pg, '#twho') in ('Right',) and T(pg, '#tbCode') == before and pg.is_visible('#tnext'), 'returning from Watch keeps the reveal', (T(pg, '#twho'), T(pg, '#tbCode')))
        # leaving during the ask phase restarts that scene
        pg.click('#tnext'); wait_phase(pg, ('Your call',)); code = T(pg, '#tbCode')
        pg.click('#mt-plan'); pg.clock.run_for(5000); pg.click('#mt-trainer'); pg.clock.run_for(30)
        L.check(T(pg, '#twho') == 'Read' and T(pg, '#tbCode') == code, 'leaving mid-question replays the same scene, no timeout while away', (T(pg, '#twho'), T(pg, '#tbCode')))
        # "Try X speed" button
        L.check(not errs, f'{w}: no console errors in rounds', errs[:4])
        ctx.close()
    L.note(f"scenes seen in real rounds fc26: {sorted(fb_seen['fc26'], key=lambda s: int(s[1:]))}")
    L.note(f"scenes seen in real rounds fc23: {sorted(fb_seen['fc23'], key=lambda s: int(s[1:]))}")
    b.close()
L.dump()
