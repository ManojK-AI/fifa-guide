"""Standards QA (read-only): accessibility tree, headings, tabs/keyboard, focus handling, target sizes, links."""
import sys, json, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent; WORK = HERE.parent.parent; sys.path.insert(0, str(WORK))
from harness import open_page
SH = HERE / 'shots'; SH.mkdir(exist_ok=True)
R = {}

HEADINGS = """() => [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(h => h.offsetParent || h.getClientRects().length).map(h => h.tagName + ' ' + h.innerText.replace(/\\s+/g,' ').slice(0,60))"""

def ax(pg, sel):
    try:
        return pg.locator(sel).first.aria_snapshot()
    except Exception as e:
        return 'ERR ' + str(e)

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx, pg, errs = open_page(b, 1280, 900, game='fc26')
    # --- headings per tab, both games
    for game in ('fc26', 'fc23'):
        pg.evaluate(f"window.__lrrGame('{game}')")
        for m in ('trainer', 'ai', 'replays', 'plan'):
            pg.evaluate(f"window.__lrrMode('{m}')"); pg.wait_for_timeout(60)
            R[f'headings_{game}_{m}'] = pg.evaluate(HEADINGS)
    pg.evaluate("window.__lrrGame('fc26')")
    # --- hidden blocks out of the a11y tree (FC 26 mode): aria snapshot of AI panel must not contain FIFA 23 texts
    pg.evaluate("window.__lrrMode('ai')")
    snap_ai = ax(pg, '#p-ai')
    R['ai_snapshot_has_fifa23'] = ('Scouting report · FIFA 23 CPU' in snap_ai) or ('Title Update 2' in snap_ai)
    R['ai_snapshot_head'] = snap_ai[:1500]
    pg.evaluate("window.__lrrMode('plan')")
    snap_plan = ax(pg, '#p-plan')
    R['plan_snapshot_has_fifa23'] = ('Timed Finishing: Off' in snap_plan) or ('Lengthy' in snap_plan and 'Striker: Lengthy' in snap_plan)
    # --- coach card buttons as exposed to AT
    pg.evaluate("window.__lrrMode('replays')")
    tmap = pg.evaluate("Object.fromEntries([...document.querySelectorAll('.titem')].map(b=>[b.querySelector('.code').textContent,+b.dataset.i]))")
    R['coach_ax'] = {}
    for cid in ('U6', 'D2', 'U3', 'B5', 'C1'):
        pg.evaluate(f"window.__lrrShow({tmap[cid]},'right',0,'board')")
        R['coach_ax'][cid] = ax(pg, '#cKeys')
        R['coach_ax'][cid + '_labels'] = pg.evaluate("[...document.querySelectorAll('#cKeys .kb')].map(k=>k.getAttribute('aria-label'))")
    # keychip
    R['keychip_hidden'] = pg.get_attribute('#keychip', 'aria-hidden')
    # canvas labels
    pg.evaluate(f"window.__lrrShow({tmap['A1']},'wrong',1.0,'board')")
    R['cv_label_A1_wrong'] = pg.get_attribute('#cv', 'aria-label')
    pg.evaluate(f"window.__lrrShow({tmap['A1']},'right',2.0,'board')")
    R['cv_label_A1_right'] = pg.get_attribute('#cv', 'aria-label')
    R['tcv_label_intro'] = pg.get_attribute('#tcv', 'aria-label')
    # --- clip-ref names, drill names, links opening new tabs
    pg.evaluate("window.__lrrMode('ai')")
    R['clipref_names_sample'] = pg.evaluate("[...document.querySelectorAll('#p-ai .g26 .clip-ref')].slice(0,6).map(b=>[b.innerText,b.getAttribute('aria-label')])")
    R['drill_names'] = pg.evaluate("[...document.querySelectorAll('#p-ai .g26 [data-drill]')].map(b=>b.innerText)")
    R['new_tab_links'] = pg.evaluate("[...document.querySelectorAll('a[target=_blank]')].length")
    R['new_tab_links_with_hint'] = pg.evaluate("[...document.querySelectorAll('a[target=_blank]')].filter(a=>/new tab|new window/i.test((a.getAttribute('aria-label')||'')+a.innerText+(a.title||''))).length")
    R['same_text_diff_href'] = pg.evaluate("""(()=>{const m={};document.querySelectorAll('.g26 a, a:not(.g23 a)').forEach(a=>{if(a.closest('.g23'))return;const t=a.innerText.trim();(m[t]=m[t]||new Set()).add(a.href)});return Object.entries(m).filter(([t,s])=>s.size>1).map(([t,s])=>[t,s.size])})()""")
    # --- focus after activating a clip link from AI tab (keyboard)
    pg.focus('#p-ai .g26 .clip-ref >> nth=0')
    pg.keyboard.press('Enter'); pg.wait_for_timeout(200)
    R['focus_after_clipref'] = pg.evaluate("(()=>{const a=document.activeElement;return a?(a.tagName+'#'+a.id+'.'+a.className+' visible='+!!(a.offsetParent||a===document.body)):null})()")
    R['mode_after_clipref'] = pg.evaluate("[...document.querySelectorAll('.mtab')].find(b=>b.getAttribute('aria-selected')==='true').id")
    pg.evaluate("window.__lrrMode('ai')")
    pg.focus('#p-ai .g26 [data-drill] >> nth=0')
    pg.keyboard.press('Enter'); pg.wait_for_timeout(200)
    R['focus_after_drill'] = pg.evaluate("(()=>{const a=document.activeElement;return a?(a.tagName+'#'+a.id+'.'+a.className):null})()")
    R['trainer_phase_after_drill'] = pg.evaluate("document.getElementById('tintro').hidden")
    # --- tab key order at top: from game switch through main tabs
    pg.evaluate("window.__lrrMode('replays')")
    pg.focus('#mt-replays')
    seq = []
    for _ in range(12):
        pg.keyboard.press('Tab')
        seq.append(pg.evaluate("(()=>{const a=document.activeElement;return a.tagName+(a.id?'#'+a.id:'')+(a.className?'.'+String(a.className).split(' ')[0]:'')+' '+(a.getAttribute('role')||'')+' '+(a.innerText||'').replace(/\\s+/g,' ').slice(0,24)})()"))
    R['tab_seq_from_replays_tab'] = seq
    # picker tablist: arrow key on a picker tab
    pg.focus('#tab-stop')
    before = pg.evaluate("document.querySelector('.titem[aria-current=true] .code').textContent")
    pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(100)
    after = pg.evaluate("document.querySelector('.titem[aria-current=true] .code').textContent")
    R['picker_tab_arrow'] = {'before': before, 'after': after, 'focus': pg.evaluate("document.activeElement.id"), 'picker_tabs_tabindex': pg.evaluate("[...document.querySelectorAll('#tabs .tab')].map(t=>t.getAttribute('tabindex'))")}
    # main tabs: Home/End support?
    pg.focus('#mt-replays'); pg.keyboard.press('End'); pg.wait_for_timeout(80)
    R['main_tabs_End'] = pg.evaluate("document.activeElement.id")
    ctx.close()

    # --- target sizes (WCAG 2.5.8: 24x24 CSS px) at phone width, FC 26
    ctx, pg, errs = open_page(b, 390, 844, game='fc26')
    small = {}
    for m in ('trainer', 'ai', 'replays', 'plan'):
        pg.evaluate(f"window.__lrrMode('{m}')"); pg.wait_for_timeout(80)
        small[m] = pg.evaluate("""() => {
          const out = [];
          for (const el of document.querySelectorAll('button, a, input, [role=slider], [tabindex]')) {
            if (!(el.offsetParent || el.getClientRects().length)) continue;
            const r = el.getBoundingClientRect(); if (!r.width) continue;
            const inline = el.tagName === 'A' && getComputedStyle(el).display === 'inline';
            if ((r.width < 24 || r.height < 24) && !inline) out.push((el.className||el.tagName) + ' ' + (el.innerText||el.getAttribute('aria-label')||'').slice(0,20) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height));
          }
          return [...new Set(out)].slice(0, 12);
        }""")
    R['small_targets_390'] = small
    # focus ring clipping screenshots
    pg.evaluate("window.__lrrMode('replays')"); pg.wait_for_timeout(200)
    pg.focus('.titem >> nth=0'); pg.keyboard.press('Shift+Tab'); pg.keyboard.press('Tab'); pg.wait_for_timeout(100)
    pg.locator('#picker').screenshot(path=str(SH / 'focus_titem_390.png'))
    pg.focus('#tab-ultimate'); pg.keyboard.press('Shift+Tab'); pg.keyboard.press('Tab'); pg.wait_for_timeout(100)
    pg.locator('#picker').screenshot(path=str(SH / 'focus_pickertab_390.png'))
    R['outline_clip_check'] = pg.evaluate("""() => {
      const t = document.querySelector('.titem'); const l = t.closest('.tlist');
      const tr = t.getBoundingClientRect(), lr = l.getBoundingClientRect(); const cs = getComputedStyle(l);
      return {titemTop: tr.top - lr.top, listOverflowX: cs.overflowX, listOverflowY: cs.overflowY, listPad: cs.padding, ringNeeds: 4.5};
    }""")
    ctx.close()

    # --- reduced motion: replays paused on load? trainer?
    rctx = b.new_context(viewport={'width': 1280, 'height': 900}, reduced_motion='reduce')
    rp = rctx.new_page()
    from harness import page_html, attach, URL
    attach(rp, page_html()); rp.add_init_script("try{localStorage.setItem('lrr:mode','replays')}catch(e){}")
    rp.goto(URL); rp.wait_for_timeout(800)
    R['reduced_motion_replays_playing'] = rp.get_attribute('#playBtn', 'aria-label')
    rp.click('.titem >> nth=2'); rp.wait_for_timeout(300)
    R['reduced_motion_after_click_playing'] = rp.get_attribute('#playBtn', 'aria-label')
    R['reduced_motion_card_anim'] = rp.evaluate("getComputedStyle(document.querySelector('.caption .say')).animationName")
    rctx.close()
    b.close()

(HERE / 'a11y.json').write_text(json.dumps(R, indent=1, ensure_ascii=False))
print(json.dumps(R, indent=1, ensure_ascii=False)[:9000])
