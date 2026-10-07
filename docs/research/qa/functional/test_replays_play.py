"""3a. Every clip plays end to end in Board and Match cam, both games, through the real RAF loop (fake clock)."""
from common import *
import sys
from playwright.sync_api import sync_playwright
L = Log('replays_play' + (sys.argv[1] if len(sys.argv) > 1 else ''))
COMBOS = [('fc26', 'board', 1), ('fc23', 'board', 1), ('fc26', 'cam', 1.5), ('fc23', 'cam', 1.5)]
if len(sys.argv) > 1:
    COMBOS = [c for c in COMBOS if c[0] + c[1] == sys.argv[1]]
with sync_playwright() as p:
    b = p.chromium.launch()
    for game, view, speed in COMBOS:
        ctx, pg, errs = open_clock(b, 1280, 900, game=game, pause=True)
        pg.click('#mt-replays'); pg.clock.run_for(50)
        pg.click('#viewCam' if view == 'cam' else '#viewBoard')
        pg.click({1: '#spdOne', 1.5: '#spdFast', 0.5: '#spdHalf'}[speed])
        for i, tid in enumerate(TIDS):
            n0 = len(errs)
            pg.click(f'.titem[data-i="{i}"]'); pg.clock.run_for(20); p0 = pg.evaluate('performance.now()')
            t = TAC[tid]; total = t['wrong']['real'] + 1.25 + t['right']['real']
            seen_states, caps, saw_goal = [], [], set()
            ended_at = None
            steps = int((total / speed + 2) / 0.1)
            for k in range(steps):
                pg.clock.run_for(100)
                s = pg.evaluate("""()=>({st:document.getElementById('bugState').textContent,card:!document.getElementById('card').hidden,
                   end:!document.getElementById('endcard').hidden,say:document.getElementById('say').textContent,bug:document.getElementById('bugCode').textContent,
                   flash:document.getElementById('flash').hidden?'':document.getElementById('flash').textContent})""")
                st = 'card' if s['card'] else s['st']
                if not seen_states or seen_states[-1] != st: seen_states.append(st)
                if not caps or caps[-1] != s['say']: caps.append(s['say'])
                if s['flash']: saw_goal.add(s['flash'])
                if s['end']:
                    ended_at = (pg.evaluate('performance.now()') - p0) / 1000; break
            L.check(s['bug'] == tid, f'{game}/{view}/{tid}: stays on clip', s['bug'])
            L.check(ended_at is not None, f'{game}/{view}/{tid}: reaches end card', seen_states)
            if ended_at:
                exp = total / speed
                L.check(abs(ended_at - exp) < 0.25, f'{game}/{view}/{tid}: duration ~{exp:.1f}s at {speed}x', ended_at)
                et = pg.text_content('#endTitle'); btns = pg.eval_on_selector_all('#endRow button', 'els=>els.map(b=>b.textContent)')
                nx = TAC[TIDS[(i + 1) % len(TIDS)]]['name']
                L.check(et == f"{t['name']}: seen both ways", f'{game}/{view}/{tid}: end title', et)
                L.check(btns == ['Replay', 'Right way again', f'Next: {nx} →'], f'{game}/{view}/{tid}: end buttons', btns)
                L.check(pg.get_attribute('#playBtn', 'aria-label') == 'Play', f'{game}/{view}/{tid}: play button shows Play at end')
            L.check(seen_states[:3] == ['Wrong', 'card', 'Right'], f'{game}/{view}/{tid}: wrong -> card -> right', seen_states)
            exp_caps = [gsay(c[1], game) for c in t['wrong']['say']] + ['Now the right way.'] + [gsay(c[1], game) for c in t['right']['say']]
            # caption transitions seen while playing must equal the expected per-game sequence (collapse repeats)
            exp_seq = [c for k, c in enumerate(exp_caps) if k == 0 or exp_caps[k - 1] != c]
            L.check(caps == exp_seq, f'{game}/{view}/{tid}: caption sequence during playback = {game} script', (caps, exp_seq))
            L.check(len(errs) == n0, f'{game}/{view}/{tid}: no console errors', errs[n0:n0 + 3])
            L.note(f'{game}/{view}/{tid}: flashes {sorted(saw_goal)}')
        ctx.close()
    b.close()
L.dump()
