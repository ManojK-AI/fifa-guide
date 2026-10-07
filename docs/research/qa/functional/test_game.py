"""1. Game switch: default, visibility per tab, coach card per clip, captions/key chip per clip, persistence, live switching."""
from common import *
import re
from playwright.sync_api import sync_playwright
L = Log('game')

VIS_JS = """(panel)=>{
  const vis=e=>e.checkVisibility({checkOpacity:true,checkVisibilityCSS:true});
  const scope=[document.querySelector('.mast'),document.getElementById(panel)];
  const out={g26:[0,0],g23:[0,0],leak:[],missing:[]};
  for(const root of scope){
    for(const cls of ['g26','g23']){
      root.querySelectorAll('.'+cls).forEach(e=>{const v=vis(e);out[cls][v?0:1]++;
        const want=(document.documentElement.dataset.game==='fc23')===(cls==='g23');
        if(v&&!want)out.leak.push(cls+':'+e.tagName+':'+(e.textContent||'').trim().slice(0,60));
        if(!v&&want)out.missing.push(cls+':'+e.tagName+':'+(e.textContent||'').trim().slice(0,60));});
    }
  }
  // also: elements of the other game anywhere in the document that are visible
  const other=document.documentElement.dataset.game==='fc23'?'.g26':'.g23';
  out.anyOther=[...document.querySelectorAll(other)].filter(vis).length;
  out.cards=[...document.querySelectorAll('#'+panel+' .mcard')].filter(vis).length;
  out.checks=[...document.querySelectorAll('#'+panel+' [data-chk]')].filter(vis).length;
  out.refs=[...document.querySelectorAll('#'+panel+' .clip-ref')].filter(vis).map(e=>e.dataset.clip);
  out.drills=[...document.querySelectorAll('#'+panel+' [data-drill]')].filter(vis).map(e=>e.dataset.drill);
  out.text=document.getElementById(panel).innerText;
  return out;}"""

with sync_playwright() as p:
    b = p.chromium.launch()
    # ---------- A. default ----------
    ctx, pg, errs = open_page(b, 1280, 900)
    L.check(pg.evaluate("document.documentElement.dataset.game") == 'fc26', 'default data-game is fc26')
    L.check(pg.get_attribute('[data-gm="fc26"]', 'aria-pressed') == 'true' and pg.get_attribute('[data-gm="fc23"]', 'aria-pressed') == 'false', 'default switch aria-pressed')
    L.check(pg.evaluate("localStorage.getItem('lrr:game')") is None, 'no stored game on first load')
    L.check(pg.is_visible('.eyebrow .g26') and not pg.is_visible('.eyebrow .g23'), 'eyebrow FC 26 only by default')
    L.check(pg.inner_text('.eyebrow').strip() == 'EA SPORTS FC 26 · SQUAD BATTLES AI · YOUR 4-3-3', 'eyebrow text fc26', pg.inner_text('.eyebrow'))
    texts = {}
    for game in ('fc26', 'fc23'):
        if game == 'fc23':
            pg.click('[data-gm="fc23"]'); pg.wait_for_timeout(100)
            L.check(pg.evaluate("document.documentElement.dataset.game") == 'fc23', 'click FIFA 23 sets data-game')
            L.check(pg.evaluate("localStorage.getItem('lrr:game')") == 'fc23', 'click FIFA 23 stores lrr:game')
            L.check(pg.get_attribute('[data-gm="fc23"]', 'aria-pressed') == 'true' and pg.get_attribute('[data-gm="fc26"]', 'aria-pressed') == 'false', 'fc23 aria-pressed')
            L.check(pg.inner_text('.eyebrow').strip() == 'FIFA 23 · ULTIMATE AI · YOUR 4-3-3 ATTACK', 'eyebrow text fc23', pg.inner_text('.eyebrow'))
        for tab in ('trainer', 'ai', 'replays', 'plan'):
            pg.click(f'#mt-{tab}'); pg.wait_for_timeout(80)
            r = pg.evaluate(VIS_JS, f'p-{tab}')
            L.check(not r['leak'], f'{game}/{tab}: no visible blocks from the other game', r['leak'][:5])
            L.check(not r['missing'], f'{game}/{tab}: all own-game blocks visible', r['missing'][:5])
            L.check(r['anyOther'] == 0, f'{game}/{tab}: zero visible other-game elements in whole doc', r['anyOther'])
            texts[(game, tab)] = r['text']
            if tab == 'ai':
                L.check(r['cards'] == 18, f'{game}: 18 AI cards visible', r['cards'])
                L.check(r['drills'] == ['def', 'att'], f'{game}: drill buttons def/att', r['drills'])
                L.note(f'{game} AI clip refs: {r["refs"]}')
            if tab == 'plan':
                n = 12 if game == 'fc26' else 11
                L.check(r['checks'] == n, f'{game}: {n} plan checkboxes visible', r['checks'])
                L.check(pg.inner_text('#chkCount') == f'0 of {n} done', f'{game}: count text', pg.inner_text('#chkCount'))
                L.note(f'{game} plan clip refs: {r["refs"]}')
        texts[(game, 'mast')] = pg.inner_text('.mast'); texts[(game, 'foot')] = pg.inner_text('.foot')
    # ---------- C. text leak scan ----------
    leak26 = re.compile(r"FIFA ?23|Title Update [2467]\b|\+10|Stay Back|Forward Runs|Chance Creation|Stay On Edge|Timed Finishing: Off|First Time Shots|Round the Keeper|trait|Players in Box|Extra Striker|Ultimate AI|Lengthy\.|Pitch Notes, FIFA")
    leak23 = re.compile(r"FC ?26|FC ?25|1\.[0-5]\.[0-9]|PlayStyle|Deep-Lying|FC IQ|Squad Battles AI|double-tap|Line Height|Advanced Forward|Competitive gameplay")
    for (game, tab), t in texts.items():
        rx = leak26 if game == 'fc26' else leak23
        for line in t.split('\n'):
            for m in rx.finditer(line):
                L.note(f'TEXT[{game}/{tab}] "{m.group(0)}" in: {line.strip()[:160]}')
    ctx.close()

    # ---------- D. coach card per clip, both games ----------
    for game in ('fc26', 'fc23'):
        ctx, pg, errs = open_page(b, 1280, 900, game=game)
        pg.click('#mt-replays'); pg.wait_for_timeout(100)
        for i, tid in enumerate(TIDS):
            pg.click(f'.titem[data-i="{i}"]'); pg.wait_for_timeout(30)
            c = pg.evaluate(COACH_JS); e = exp_coach(tid, game)
            L.check(c['t'] == TAC[tid]['name'], f'{game}/{tid} coach title', c['t'])
            L.check(c['watch'] == e['watch'] and c['cue'] == e['cue'], f'{game}/{tid} watch/cue', (c['watch'], c['cue']))
            L.check(c['set'] == e['setting'] and c['setHidden'] == (not e['setting']), f'{game}/{tid} setting', c['set'])
            L.check(c['keyTokens'] == e['keys'], f'{game}/{tid} key tokens', (c['keyTokens'], e['keys']))
            L.check(c['keyLabels'] == e['labels'], f'{game}/{tid} key labels', (c['keyLabels'], e['labels']))
            L.check(c['noteVis'] == bool(e['note']), f'{game}/{tid} notes block visibility')
            if game == 'fc26':
                L.check(c['n26Vis'] == bool(e['n']) and (not e['n'] or c['n26'] == e['n']), f'fc26/{tid} In FC 26 note shown iff defined', (c['n26Vis'], c['n26'][:50]))
            else:
                L.check(not c['n26Vis'], f'fc23/{tid} In FC 26 note hidden', c['n26'][:60])
            L.check(c['srcVis'] == bool(e['srcs']), f'{game}/{tid} sources visibility')
            got = [(l['t'], l['u']) for l in c['links']]; want = [(s['t'], s['u']) for s in e['srcs']]
            L.check(got == want, f'{game}/{tid} source links', (got, want))
            for l in c['links']:
                L.check(l['u'].startswith('https://') and l['tg'] == '_blank' and 'noopener' in l['rel'] and l['vis'], f'{game}/{tid} link attrs {l["u"]}')
            if e['srcs']:
                lab = 'Sources: ' if len(e['srcs']) > 1 else ('Source (FIFA 23): ' if e['src_label_23'] else 'Source: ')
                L.check(c['srcText'].startswith(lab), f'{game}/{tid} source label', c['srcText'][:40])
                if 'FIFA 23' in lab: L.note(f'{game}/{tid}: source shown as "(FIFA 23)"')
        L.check(not errs, f'{game}: no console errors in coach sweep', errs[:4])
        ctx.close()

    # ---------- E. captions + key chip per clip (fine steps), both games ----------
    SWEEP = r"""([i,game,dw,dr])=>{
      const out={say:[],keys:[],err:null};
      for(const side of ['wrong','right']){
        const dur=side==='wrong'?dw:dr;
        for(let ct=0;ct<=dur+1e-6;ct+=0.025){
          try{window.__lrrShow(i,side,ct,'board');}catch(e){out.err=String(e);break;}
          const s=document.getElementById('say').textContent; if(!out.say.length||out.say[out.say.length-1][1]!==s)out.say.push([side,s]);
          const kc=document.getElementById('keychip');
          if(!kc.classList.contains('off')){const k=[...document.querySelectorAll('#kcRow .kb > span')].filter(x=>!x.classList.contains('kplus')).map(x=>x.textContent).join(' ')+' | '+document.querySelector('#kcRow > span:last-child').textContent+' | '+document.getElementById('kcTag').textContent;
            if(!out.keys.includes(k))out.keys.push(k);}
        }
      }
      return out;}"""
    for game in ('fc26', 'fc23'):
        ctx, pg, errs = open_page(b, 1280, 900, game=game)
        for i, tid in enumerate(TIDS):
            r = pg.evaluate(SWEEP, [i, game, TAC[tid]['wrong']['dur'], TAC[tid]['right']['dur']])
            L.check(r['err'] is None, f'{game}/{tid} sweep no exception', r['err'])
            t = TAC[tid]
            exp_say = [gsay(s[1], game) for s in t['wrong']['say']] + [gsay(s[1], game) for s in t['right']['say']]
            got_say = [s for side, s in r['say'] if s != 'Now the right way.']
            L.check(got_say == exp_say, f'{game}/{tid} captions sequence', (got_say, exp_say))
            exp_keys = []
            for side in ('wrong', 'right'):
                for k in t[side]['key']:
                    tok, lab = gkey(k[1], k[2], game)
                    s = ' '.join(x for x in tok if x != '+') + ' | ' + lab + ' | ' + ('The mistake' if k[3] == 'bad' else 'Press')
                    if s not in exp_keys: exp_keys.append(s)
            L.check(r['keys'] == exp_keys, f'{game}/{tid} key chips', (r['keys'], exp_keys))
        L.check(not errs, f'{game}: no console errors in caption sweep', errs[:4])
        ctx.close()

    # ---------- F. live switching ----------
    ctx, pg, errs = open_page(b, 1280, 900, game='fc23')
    u3 = TIDS.index('U3')
    pg.evaluate(f"window.__lrrShow({u3},'wrong',1.2,'board')"); pg.wait_for_timeout(100)
    before = pg.inner_text('#say')
    pg.click('[data-gm="fc26"]'); pg.wait_for_timeout(200)
    after = pg.inner_text('#say')
    L.check(before == 'Blocked. CPU defenders block anything within about a yard.' and after == 'Blocked. He was close enough to get a foot to it.', 'paused replay caption updates live on switch', (before, after))
    u1 = TIDS.index('U1')
    pg.evaluate(f"window.__lrrShow({u1},'right',1.75,'board')"); pg.wait_for_timeout(100)
    k26 = pg.inner_text('#kcRow').replace('\n', ' ')
    pg.click('[data-gm="fc23"]'); pg.wait_for_timeout(200)
    k23 = pg.inner_text('#kcRow').replace('\n', ' ')
    L.check('RB' not in k26 and 'RB' in k23, 'paused replay key chip updates live on switch', (k26, k23))
    # trainer reveal, then switch game
    for sid in ('s13', 's23', 's17'):
        idx = int(sid[1:]) - 1
        pg.click('[data-gm="fc23"]'); pg.wait_for_timeout(50)
        pg.evaluate(f"window.__lrrTrain({idx},false,'reveal',null,'board')"); pg.wait_for_timeout(100)
        t23 = pg.inner_text('#tsay')
        pg.click('[data-gm="fc26"]'); pg.wait_for_timeout(150)
        t26 = pg.inner_text('#tsay')
        L.check(t23 == gfb(sid, 'fc23') and t26 == gfb(sid, 'fc26'), f'trainer reveal feedback {sid} follows a live game switch (fc23 -> fc26)', (t23[:70], t26[:70]))
    # plan count live
    pg.click('#mt-plan'); pg.click('[data-gm="fc26"]')
    L.check(pg.inner_text('#chkCount') == '0 of 12 done', 'plan count on switch fc26')
    pg.click('[data-gm="fc23"]')
    L.check(pg.inner_text('#chkCount') == '0 of 11 done', 'plan count on switch fc23')
    L.check(not errs, 'no console errors in live switching', errs[:4])
    ctx.close()
    # persistence after reload, both ways, in a clean context (no init script forcing the game)
    ctx, pg, errs = open_page(b, 1280, 900)
    pg.click('[data-gm="fc23"]'); pg.wait_for_timeout(50)
    pg.reload(); pg.wait_for_timeout(300)
    L.check(pg.evaluate("document.documentElement.dataset.game") == 'fc23' and pg.get_attribute('[data-gm="fc23"]', 'aria-pressed') == 'true', 'fc23 persists after reload')
    L.check(pg.is_visible('.eyebrow .g23') and not pg.is_visible('.eyebrow .g26'), 'eyebrow after reload fc23')
    pg.click('[data-gm="fc26"]'); pg.reload(); pg.wait_for_timeout(300)
    L.check(pg.evaluate("document.documentElement.dataset.game") == 'fc26', 'fc26 persists after reload')
    # bogus stored value
    pg.evaluate("localStorage.setItem('lrr:game','fifa99')"); pg.reload(); pg.wait_for_timeout(300)
    L.check(pg.evaluate("document.documentElement.dataset.game") == 'fc26', 'bogus stored game falls back to fc26')
    L.check(not errs, 'no console errors in live switching', errs[:4])
    ctx.close()
    b.close()
L.dump()
