"""Smoke test: both games, every tab, every clip, trainer feedback, widths, errors."""
import sys, json
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(__import__('pathlib').Path(__file__).parent))
from harness import open_page

OUT = __import__('pathlib').Path(__file__).parent / 'shots'
OUT.mkdir(exist_ok=True)
fails = []
def check(cond, msg):
    if not cond:
        fails.append(msg)

with sync_playwright() as p:
    b = p.chromium.launch()
    # default game is FC 26
    ctx, pg, errs = open_page(b, 390, 844)
    check(pg.evaluate("document.documentElement.dataset.game") == 'fc26', 'default game should be fc26')
    check(pg.is_visible('.eyebrow .g26') and not pg.is_visible('.eyebrow .g23'), 'eyebrow shows FC 26 only')
    # AI tab FC 26
    pg.click('#mt-ai')
    n26 = pg.eval_on_selector_all('#p-ai .g26 .mcard', 'els=>els.filter(e=>e.offsetParent).length')
    n23 = pg.eval_on_selector_all('#p-ai .g23 .mcard', 'els=>els.filter(e=>e.offsetParent).length')
    check(n26 == 18 and n23 == 0, f'AI cards visible fc26={n26} fc23={n23}')
    # clip refs in FC 26 AI tab all resolve
    refs = pg.eval_on_selector_all('#p-ai .g26 .clip-ref', 'els=>els.map(e=>e.dataset.clip)')
    ids = pg.evaluate("[...document.querySelectorAll('.titem .code')].map(e=>e.textContent)")
    check(all(r in ids for r in refs), 'unknown clip ref in FC 26 AI tab: ' + str([r for r in refs if r not in ids]))
    # Plan FC 26
    pg.click('#mt-plan')
    check(pg.inner_text('#chkCount') == '0 of 12 done', 'FC 26 check count: ' + pg.inner_text('#chkCount'))
    pg.click('[data-chk="f26-def"]')
    check(pg.inner_text('#chkCount') == '1 of 12 done', 'tick counts: ' + pg.inner_text('#chkCount'))
    # switch to FIFA 23
    pg.click('[data-gm="fc23"]')
    check(pg.evaluate("document.documentElement.dataset.game") == 'fc23', 'switch to fc23')
    check(pg.inner_text('#chkCount') == '0 of 11 done', 'FIFA 23 check count: ' + pg.inner_text('#chkCount'))
    pg.click('#mt-ai')
    n23 = pg.eval_on_selector_all('#p-ai .g23 .mcard', 'els=>els.filter(e=>e.offsetParent).length')
    check(n23 == 18, f'FIFA 23 AI cards visible {n23}')
    pg.reload(); pg.wait_for_timeout(300)
    check(pg.evaluate("document.documentElement.dataset.game") == 'fc23', 'game choice persists')
    pg.click('[data-gm="fc26"]')
    check(pg.inner_text('#chkCount') == '1 of 12 done', 'FC 26 tick persisted: ' + pg.inner_text('#chkCount'))
    # Pro tab (added 2026-11-04): panel, tables, evidence tags, clip links, FIFA 23 note, Pro clips in the picker
    pg.click('#mt-pro')
    check(pg.is_visible('#p-pro') and not pg.is_visible('#p-plan'), 'Pro tab shows only its panel')
    check(pg.eval_on_selector_all('#p-pro table.ptab', 'els=>els.length') == 5, 'Pro tab tables')
    check(pg.eval_on_selector_all('#p-pro .ev', 'els=>els.length') > 50, 'Pro tab evidence tags')
    hrefs = pg.eval_on_selector_all('#p-pro a.src, #p-pro .srcs a', 'els=>els.map(a=>a.getAttribute("href"))')
    check(hrefs and all(h.startswith('https://') for h in hrefs), 'Pro tab links: ' + str([h for h in hrefs if not h.startswith('https://')][:3]))
    check(not pg.is_visible('#p-pro .g23'), 'FIFA 23 note hidden in FC 26')
    prefs = pg.eval_on_selector_all('#p-pro .clip-ref', 'els=>els.map(e=>e.dataset.clip)')
    pids = pg.evaluate("[...document.querySelectorAll('.titem .code')].map(e=>e.textContent)")
    check(prefs and all(r in pids for r in prefs), 'unknown clip ref in Pro tab: ' + str([r for r in prefs if r not in pids]))
    check(pg.eval_on_selector_all('#grp-pro .titem', 'els=>els.length') == 4, 'Pro patterns group has 4 clips')
    pg.click('#p-pro .clip-ref[data-clip="P1"]'); pg.wait_for_timeout(150)
    check(pg.evaluate("document.documentElement.querySelector('#p-replays').hidden") is False, 'Pro clip link opens Replays')
    check(pg.evaluate("document.querySelector('.titem[aria-current=\"true\"] .code').textContent") == 'P1', 'Pro clip link selects P1')
    check('Deep-Lying Playmaker' in pg.inner_text('#cSet'), 'P1 FC 26 setting: ' + pg.inner_text('#cSet'))
    check('1.4.0' in pg.inner_text('#cN26T'), 'P1 FC 26 note: ' + pg.inner_text('#cN26T'))
    pg.click('[data-gm="fc23"]'); pg.click('#mt-pro')
    check(pg.is_visible('#p-pro .g23'), 'FIFA 23 note shown in FIFA 23')
    check('Stay Back While Attacking' in pg.evaluate("(()=>{window.__lrrMode('replays');document.querySelector('.titem[data-i]');return ''})()") + pg.evaluate("(()=>{const i=[...document.querySelectorAll('.titem')].find(b=>b.querySelector('.code').textContent==='P1').dataset.i;document.querySelector('.titem[data-i=\"'+i+'\"]').click();return document.getElementById('cSet').innerText})()"), 'P1 FIFA 23 setting')
    pg.click('[data-gm="fc26"]')
    # Replays: coach card per game
    pg.click('#mt-replays')
    pg.evaluate("window.__lrrShow && 0")
    tmap = pg.evaluate("Object.fromEntries([...document.querySelectorAll('.titem')].map(b=>[b.querySelector('.code').textContent,+b.dataset.i]))")
    tids = sorted(tmap, key=lambda k: tmap[k])
    def coach(i):
        pg.evaluate(f"document.querySelector('.titem[data-i=\"{i}\"]').click()")
        return pg.evaluate("({keys:document.getElementById('cKeys').innerText,set:document.getElementById('cSet').innerText,n:document.getElementById('cN26').hidden?'':document.getElementById('cN26T').innerText,src:document.getElementById('cSrc').innerText,cue:document.getElementById('cCue').innerText})")
    u1 = coach(tids.index('U1'))
    check('LB' in u1['keys'] and 'RB' not in u1['keys'].split('Lobbed')[0], 'U1 FC 26 keys: ' + u1['keys'])
    check('Advanced Forward' in u1['set'], 'U1 FC 26 setting: ' + u1['set'])
    check('1.0.3' in u1['n'], 'U1 FC 26 note: ' + u1['n'])
    d2 = coach(tids.index('D2'))
    check('Tactical' in d2['keys'], 'D2 contain label: ' + d2['keys'])
    c4 = coach(tids.index('C4'))
    check(c4['keys'].count('LB') >= 1 and 'Driven through' in c4['keys'], 'C4 keys: ' + c4['keys'])
    # play every clip in FC 26 through several time points (both views)
    bad = []
    for view in ('board', 'cam'):
        for i, t in enumerate(tids):
            for side in ('wrong', 'right'):
                for ct in (0.2, 0.9, 1.6, 2.4, 3.3, 4.4, 5.6):
                    r = pg.evaluate(f"(()=>{{try{{window.__lrrShow({i},'{side}',{ct},'{view}');return 'ok'}}catch(e){{return String(e)}}}})()")
                    if r != 'ok':
                        bad.append((t, view, side, ct, r))
    check(not bad, 'clip render errors: ' + str(bad[:5]))
    # key chip + caption mapping during U6 right
    i6 = tids.index('U6')
    pg.evaluate(f"document.querySelector('.titem[data-i=\"{i6}\"]').click()")
    pg.wait_for_timeout(200)
    # trainer FC 26 feedback
    pg.click('#mt-trainer')
    scenes = pg.evaluate("window.__LRR_SC||null")
    for idx, want in ((12, 'close enough to block'), (22, 'double-tap B')):
        pg.evaluate(f"window.__lrrTrain({idx},false,'reveal',null,'board')")
        pg.wait_for_timeout(150)
        say = pg.inner_text('#tsay')
        check(want in say, f'trainer fb s{idx+1} FC 26: {say}')
    pg.click('[data-gm="fc23"]')
    pg.evaluate("window.__lrrTrain(12,false,'reveal',null,'board')"); pg.wait_for_timeout(150)
    check('The CPU blocks almost anything' in pg.inner_text('#tsay'), 'trainer fb FIFA 23: ' + pg.inner_text('#tsay'))
    pg.click('[data-gm="fc26"]')
    check(not errs, 'errors: ' + json.dumps(errs[:8]))
    ctx.close()

    # widths x games x tabs: no horizontal scroll
    for w in (320, 390, 820, 1280):
        for game in ('fc26', 'fc23'):
            for dark in (False, True):
                ctx, pg, errs = open_page(b, w, 900, dark=dark, game=game)
                for m in ('trainer', 'ai', 'replays', 'plan', 'pro'):
                    pg.evaluate(f"window.__lrrMode('{m}')"); pg.wait_for_timeout(120)
                    sw = pg.evaluate('document.documentElement.scrollWidth'); cw = pg.evaluate('document.documentElement.clientWidth')
                    check(sw <= cw, f'h-scroll {w} {game} {m} dark={dark}: {sw}>{cw}')
                check(not errs, f'errors {w} {game}: ' + json.dumps(errs[:5]))
                ctx.close()
    b.close()

print('FAILS:', len(fails))
for f in fails:
    print(' -', f)
