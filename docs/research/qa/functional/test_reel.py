"""2. Pre-game reel in each game: full run through all 7 clips (fake clock), labels, Stop, end card, prev/next, switching game mid-reel."""
from common import *
from playwright.sync_api import sync_playwright
L = Log('reel')
REEL = {'fc26': DATA['REEL26'], 'fc23': DATA['REEL23']}

def run_and_sample(pg, ms, step=100):
    seq = []
    for _ in range(int(ms / step)):
        pg.clock.run_for(step)
        seq.append(pg.evaluate(STATE_JS))
    return seq

with sync_playwright() as p:
    b = p.chromium.launch()
    for game in ('fc26', 'fc23'):
        ctx, pg, errs = open_clock(b, 1280, 900, game=game, pause=True)
        L.check(pg.text_content('#reelLabel') == 'Pre-game reel', f'{game}: reel label idle')
        # start from the Trainer tab
        pg.click('#reelBtn'); pg.clock.run_for(50)
        s = pg.evaluate(STATE_JS)
        L.check(s['active'] == 'replays', f'{game}: reel button switches to Replays', s['active'])
        L.check(s['reelLabel'] == 'Stop reel' and s['reelPressed'] == 'true', f'{game}: reel label/pressed while playing', s)
        L.check(s['reelSub'] == 'Clip 1 of 7 · right way only', f'{game}: reel sub clip 1', s['reelSub'])
        L.check(s['card'] and s['cardK'] == 'Reel 1 of 7', f'{game}: first title card', (s['card'], s['cardK']))
        seq = [s] + run_and_sample(pg, 60000)
        order = []
        for x in seq:
            if not order or order[-1] != x['bug']:
                order.append(x['bug'])
        L.check(order == REEL[game], f'{game}: reel clip order', (order, REEL[game]))
        # per-clip label checks and right-side-only captions
        for n, cid in enumerate(REEL[game]):
            during = [x for x in seq if x['bug'] == cid]
            subs = set(x['reelSub'] for x in during if not x['end'])
            states = set(x['state'] for x in during)
            L.check(subs == {f'Clip {n+1} of 7 · right way only'}, f'{game}: reelSub for {cid}', subs)
            L.check(states == {f'Reel {n+1}/7'}, f'{game}: bug state for {cid}', states)
            cards = set(x['cardK'] for x in during if x['card'])
            L.check(cards == {f'Reel {n+1} of 7'}, f'{game}: title card for {cid}', cards)
            titles = set(x['cardT'] for x in during if x['card'])
            L.check(titles == {TAC[cid]['name']}, f'{game}: title card name for {cid}', titles)
            wrong_caps = [gsay(c[1], game) for c in TAC[cid]['wrong']['say']]
            right_caps = [gsay(c[1], game) for c in TAC[cid]['right']['say']]
            caps = [x['say'] for x in during if not x['card']]
            bad = [c for c in caps if c not in right_caps and c not in wrong_caps[:0]]
            L.check(not bad, f'{game}: only right-way captions during {cid}', bad[:3])
            L.check(all(c in caps for c in right_caps), f'{game}: all right-way captions seen for {cid}', [c for c in right_caps if c not in caps])
            coach = set(x['coachT'] for x in during)
            L.check(coach == {TAC[cid]['name']}, f'{game}: coach card follows reel clip {cid}', coach)
        last = seq[-1]
        L.check(last['end'] and last['endTitle'] == 'Reel done. Play your match.', f'{game}: end card after reel', (last['end'], last['endTitle']))
        btns = pg.eval_on_selector_all('#endRow button', 'els=>els.map(b=>b.textContent)')
        L.check(btns == ['Replay reel', 'Back to all tactics'], f'{game}: reel end buttons', btns)
        L.note(f"{game}: after the reel ends the masthead button reads '{last['reelLabel']}' (aria-pressed={last['reelPressed']}), play button '{last['play']}'")
        # time taken
        tend = next((k for k, x in enumerate(seq) if x['end']), None)
        L.note(f'{game}: reel took about {tend/10 if tend else "?"} s simulated')
        # Replay reel
        pg.click('#endRow button[data-act="reel"]'); pg.clock.run_for(100)
        s = pg.evaluate(STATE_JS)
        L.check(s['bug'] == REEL[game][0] and s['reelSub'].startswith('Clip 1 of 7') and not s['end'], f'{game}: Replay reel restarts at clip 1', s)
        # next / prev in reel mode
        pg.click('#nextBtn'); pg.clock.run_for(50); s = pg.evaluate(STATE_JS)
        L.check(s['bug'] == REEL[game][1] and s['reelSub'].startswith('Clip 2 of 7'), f'{game}: next in reel goes to reel clip 2', (s['bug'], s['reelSub']))
        pg.click('#prevBtn'); pg.clock.run_for(50); s = pg.evaluate(STATE_JS)
        L.check(s['bug'] == REEL[game][0] and s['reelSub'].startswith('Clip 1 of 7'), f'{game}: prev in reel back to clip 1', (s['bug'], s['reelSub']))
        pg.click('#prevBtn'); pg.clock.run_for(50); s = pg.evaluate(STATE_JS)
        L.check(s['bug'] == REEL[game][0], f'{game}: prev at clip 1 stays', s['bug'])
        for _ in range(8): pg.click('#nextBtn'); pg.clock.run_for(30)
        s = pg.evaluate(STATE_JS)
        L.check(s['bug'] == REEL[game][-1] and s['reelSub'].startswith('Clip 7 of 7'), f'{game}: next clamps at clip 7', (s['bug'], s['reelSub']))
        # restart in reel mode
        pg.clock.run_for(3000); pg.click('#restartBtn'); pg.clock.run_for(50); s = pg.evaluate(STATE_JS)
        L.check(s['bug'] == REEL[game][-1] and s['card'] and s['scrub'] <= 2, f'{game}: restart in reel restarts current reel clip', (s['bug'], s['card'], s['scrub']))
        # Back to all tactics (end card) -> stop
        pg.clock.run_for(9000); s = pg.evaluate(STATE_JS)
        L.check(s['end'], f'{game}: end card again at clip 7 end', s['end'])
        pg.click('#endRow button[data-act="exit"]'); pg.clock.run_for(100); s = pg.evaluate(STATE_JS)
        L.check(s['reelLabel'] == 'Pre-game reel' and s['reelPressed'] == 'false' and not s['end'], f'{game}: Back to all tactics leaves reel mode', s)
        # Stop mid reel via the masthead button
        pg.click('#reelBtn'); pg.clock.run_for(10500); s1 = pg.evaluate(STATE_JS)
        L.check(s1['bug'] == REEL[game][1], f'{game}: reel at clip 2 after 10.5 s', s1['bug'])
        pg.click('#reelBtn'); pg.clock.run_for(100); s2 = pg.evaluate(STATE_JS)
        L.check(s2['reelLabel'] == 'Pre-game reel' and s2['reelPressed'] == 'false', f'{game}: Stop resets label', s2)
        L.check(s2['play'] == 'Play' and s2['state'] == 'Wrong', f'{game}: Stop pauses on current clip (wrong way)', (s2['play'], s2['state']))
        pg.clock.run_for(3000); s3 = pg.evaluate(STATE_JS)
        L.check(s3['scrub'] == s2['scrub'] and s3['bug'] == s2['bug'], f'{game}: nothing advances after Stop', (s2['scrub'], s3['scrub']))
        L.check(not errs, f'{game}: no console errors during reel', errs[:4])
        ctx.close()

    # ---------- switching game while the reel plays ----------
    for start_game, other in (('fc26', 'fc23'), ('fc23', 'fc26')):
        for label, ms in (('during title card', 600), ('mid clip 2', 11500), ('in auto-next gap', None)):
            ctx, pg, errs = open_clock(b, 1280, 900, game=start_game, pause=True)
            pg.click('#mt-replays'); pg.clock.run_for(50)
            pg.click('#reelBtn'); pg.clock.run_for(50)
            if ms is None:
                # run until the first clip has ended (ended && reel), then switch inside the 700 ms gap
                for _ in range(400):
                    pg.clock.run_for(50)
                    if pg.evaluate("document.getElementById('bugState').textContent==='Reel 1/7' && +document.getElementById('scrub').getAttribute('aria-valuenow')>=100"):
                        break
                pg.clock.run_for(100)
            else:
                pg.clock.run_for(ms)
            before = pg.evaluate(STATE_JS)
            pg.click(f'[data-gm="{other}"]'); pg.clock.run_for(100)
            s = pg.evaluate(STATE_JS)
            c = pg.evaluate(COACH_JS)
            e = exp_coach(s['bug'], other)
            L.check(s['game'] == other, f'switch {start_game}->{other} {label}: game switched')
            L.check(s['reelLabel'] == 'Pre-game reel' and s['reelPressed'] == 'false', f'switch {start_game}->{other} {label}: reel stopped cleanly', (s['reelLabel'], s['reelPressed']))
            L.check(c['cue'] == e['cue'] and c['n26Vis'] == bool(e['n']) and c['keyLabels'] == e['labels'], f'switch {start_game}->{other} {label}: coach card is the {other} version of {s["bug"]}', (c['cue'][:40], c['n26Vis']))
            pg.clock.run_for(2000)
            s2 = pg.evaluate(STATE_JS)
            L.check(s2['bug'] == s['bug'] and s2['reelSub'] == '7 clips, right way only · about 1 minute', f'switch {start_game}->{other} {label}: stays stopped (no auto-advance)', (s['bug'], s2['bug'], s2['reelSub']))
            L.note(f'switch {start_game}->{other} {label}: was {before["bug"]} {before["state"]}; after switch {s["bug"]} state={s["state"]} play={s["play"]}')
            # restarting reel now uses the new game's list
            pg.click('#reelBtn'); pg.clock.run_for(50)
            seq = run_and_sample(pg, 60000, 200)
            order = []
            for x in seq:
                if not order or order[-1] != x['bug']: order.append(x['bug'])
            L.check(order == REEL[other], f'switch {start_game}->{other} {label}: next reel plays {other} list', order)
            L.check(not errs, f'switch {start_game}->{other} {label}: no console errors', errs[:4])
            ctx.close()
    b.close()
L.dump()
