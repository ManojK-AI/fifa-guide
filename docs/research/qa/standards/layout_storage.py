"""Standards QA (read-only): phone-width overflow, storage-throws rendering, duplicate ids, console errors."""
import sys, json, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent
WORK = HERE.parent.parent
sys.path.insert(0, str(WORK))
from harness import open_page, page_html, attach, URL

OUT = HERE / 'shots'; OUT.mkdir(exist_ok=True)
res = {'overflow': [], 'storage': {}, 'dupids': {}, 'errors': []}

OVER_JS = r"""
() => {
  const vw = document.documentElement.clientWidth;
  const se = document.scrollingElement;
  const out = {vw, scrollW: se.scrollWidth, bodyW: document.body.scrollWidth, wide: []};
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    if (!r.width || !el.offsetParent && getComputedStyle(el).position !== 'fixed') continue;
    if (r.right > vw + 0.5 || r.left < -0.5) {
      // skip elements inside a horizontal scroller (intended)
      let p = el.parentElement, inScroller = false;
      while (p && p !== document.body) { const cs = getComputedStyle(p); if ((cs.overflowX === 'auto' || cs.overflowX === 'scroll' || cs.overflowX === 'hidden') && p.getBoundingClientRect().right <= vw + 0.5) { inScroller = true; break; } p = p.parentElement; }
      if (!inScroller) out.wide.push({tag: el.tagName, cls: el.className && el.className.baseVal === undefined ? el.className : '', id: el.id, left: Math.round(r.left), right: Math.round(r.right), text: (el.innerText || '').slice(0, 60)});
    }
  }
  // gutter: .app padding
  const app = document.querySelector('.app'); const cs = getComputedStyle(app);
  out.gutter = [cs.paddingLeft, cs.paddingRight];
  return out;
}
"""

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=None)
    # 1) Phone widths, both games, all tabs, both themes
    for dark in (False, True):
        for game in ('fc26', 'fc23'):
            for w in (320, 360, 375, 390, 414):
                ctx, pg, errs = open_page(b, w, 800, dark=dark, game=game)
                for m in ('trainer', 'ai', 'replays', 'plan'):
                    pg.evaluate(f"window.__lrrMode('{m}')"); pg.wait_for_timeout(120)
                    o = pg.evaluate(OVER_JS)
                    if o['scrollW'] > o['vw'] or o['wide']:
                        res['overflow'].append({'dark': dark, 'game': game, 'w': w, 'mode': m, 'scrollW': o['scrollW'], 'vw': o['vw'], 'wide': o['wide'][:8]})
                    if w == 320 and not dark:
                        pg.screenshot(path=str(OUT / f'w320_{game}_{m}.png'), full_page=True)
                    res.setdefault('gutter', o['gutter'])
                res['errors'] += [f'{game} {w} dark={dark}: {e}' for e in errs]
                ctx.close()
    # 2) Storage that throws on every access
    THROW = """
      (function(){
        const thrower = {get(){ throw new DOMException('denied','SecurityError'); }};
        try { Object.defineProperty(window, 'localStorage', thrower); } catch(e) {}
        try { Object.defineProperty(window, 'sessionStorage', thrower); } catch(e) {}
      })();
    """
    for game_click in (None, 'fc23'):
        ctx = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2)
        pg = ctx.new_page(); errs = attach(pg, page_html())
        pg.add_init_script(THROW)
        pg.goto(URL); pg.wait_for_timeout(500)
        st = {}
        st['threw'] = pg.evaluate("(()=>{try{localStorage;return false}catch(e){return true}})()")
        st['game'] = pg.evaluate("document.documentElement.dataset.game")
        st['modeSelected'] = pg.evaluate("[...document.querySelectorAll('.mtab')].filter(b=>b.getAttribute('aria-selected')==='true').map(b=>b.id)")
        st['trainerVisible'] = pg.is_visible('#p-trainer')
        # canvas painted? sample pixels
        st['tcvPainted'] = pg.evaluate("(()=>{const c=document.getElementById('tcv');const x=c.getContext('2d').getImageData(c.width/2|0,c.height/2|0,1,1).data;return [...x]})()")
        if game_click:
            pg.click(f'[data-gm="{game_click}"]'); pg.wait_for_timeout(150)
        for m in ('ai', 'replays', 'plan'):
            pg.click(f'#mt-{m}'); pg.wait_for_timeout(250)
        st['afterClicks'] = pg.evaluate("document.documentElement.dataset.game")
        st['chkCount'] = pg.inner_text('#chkCount')
        pg.click('#mt-replays'); pg.wait_for_timeout(400)
        st['cvPainted'] = pg.evaluate("(()=>{const c=document.getElementById('cv');const x=c.getContext('2d').getImageData(c.width/2|0,c.height/2|0,1,1).data;return [...x]})()")
        st['say'] = pg.inner_text('#say')
        # tick a checkbox with storage throwing
        pg.click('#mt-plan'); pg.wait_for_timeout(100)
        vis = '.checks.g26' if not game_click else '.checks.g23'
        pg.click(f'{vis} input >> nth=0'); pg.wait_for_timeout(50)
        st['chkAfterTick'] = pg.inner_text('#chkCount')
        st['errors'] = list(errs)
        pg.screenshot(path=str(OUT / f'storage_throw_{game_click or "fc26"}.png'), full_page=False)
        res['storage'][game_click or 'fc26'] = st
        ctx.close()
    # 3) Duplicate ids (whole DOM, both games)
    for game in ('fc26', 'fc23'):
        ctx, pg, errs = open_page(b, 1280, 900, game=game)
        for m in ('trainer', 'ai', 'replays', 'plan'):
            pg.evaluate(f"window.__lrrMode('{m}')")
        res['dupids'][game] = pg.evaluate("(()=>{const c={};document.querySelectorAll('[id]').forEach(e=>{c[e.id]=(c[e.id]||0)+1});return Object.entries(c).filter(([k,v])=>v>1)})()")
        res['dupids'][game + '_aria_refs'] = pg.evaluate("""(()=>{const bad=[];document.querySelectorAll('[aria-labelledby],[aria-controls],[aria-describedby],label[for]').forEach(e=>{for(const a of ['aria-labelledby','aria-controls','aria-describedby','for']){const v=e.getAttribute(a);if(!v)continue;v.split(/\\s+/).forEach(id=>{if(!document.getElementById(id))bad.push(a+'->'+id)})}});return bad})()""")
        ctx.close()
    b.close()

(HERE / 'layout_storage.json').write_text(json.dumps(res, indent=1))
print(json.dumps({'overflow_cases': len(res['overflow']), 'first': res['overflow'][:4], 'gutter': res.get('gutter'), 'storage': res['storage'], 'dupids': res['dupids'], 'errors': res['errors'][:10]}, indent=1))
