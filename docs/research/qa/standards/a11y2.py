"""Read-only: picker tabs keyboard at phone width, play-button state after tactic change, trainer answer types."""
import sys, json, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent; WORK = HERE.parent.parent; sys.path.insert(0, str(WORK))
from harness import open_page, page_html, attach, URL
R = {}
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx, pg, errs = open_page(b, 390, 844, game='fc26')
    pg.evaluate("window.__lrrMode('replays')"); pg.wait_for_timeout(200)
    pg.focus('#tab-ultimate')
    before = pg.evaluate("document.querySelector('.titem[aria-current=true] .code').textContent")
    pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(150)
    R['picker_arrow_390'] = {'before': before, 'after': pg.evaluate("document.querySelector('.titem[aria-current=true] .code').textContent"),
                             'focus': pg.evaluate("document.activeElement.id"),
                             'selected_tab': pg.evaluate("[...document.querySelectorAll('#tabs .tab')].filter(t=>t.getAttribute('aria-selected')==='true').map(t=>t.id)")}
    # Tab order through picker tabs (all are tab stops?)
    pg.focus('#tab-ultimate'); seq = []
    for _ in range(7):
        pg.keyboard.press('Tab'); seq.append(pg.evaluate("document.activeElement.id||document.activeElement.className"))
    R['picker_tab_order_390'] = seq
    # play state after choosing another tactic while paused
    pg.click('#playBtn'); pg.wait_for_timeout(100)   # pause (it autoplays without reduced motion)
    lab1 = pg.get_attribute('#playBtn', 'aria-label')
    pg.click('.titem >> nth=3'); pg.wait_for_timeout(1600)
    c1 = pg.inner_text('#bugClock'); pg.wait_for_timeout(1200); c2 = pg.inner_text('#bugClock')
    R['play_state_after_pick'] = {'label_when_paused': lab1, 'label_after_pick': pg.get_attribute('#playBtn', 'aria-label'), 'clock_t1': c1, 'clock_t2': c2}
    # next/prev buttons same issue?
    pg.click('#playBtn'); pg.wait_for_timeout(50)
    lab_before = pg.get_attribute('#playBtn', 'aria-label')
    pg.click('#nextBtn'); pg.wait_for_timeout(1300)
    R['play_state_after_next'] = {'label_before': lab_before, 'label_after': pg.get_attribute('#playBtn', 'aria-label'), 'clock': pg.inner_text('#bugClock')}
    # game switch while a clip is shown: does the coach card update + label?
    ctx.close()
    # trainer scene types
    ctx, pg, errs = open_page(b, 1280, 900, game='fc26')
    types = pg.evaluate("(()=>{const out={};for(let i=0;i<23;i++){const d=window.__lrrScene(i,false);out[d.type]=(out[d.type]||0)+1}return out})()")
    R['trainer_types'] = types
    # keyboard-only round: start with Space, then do nothing but press 1..3 -> how many scenes answerable?
    pg.evaluate("window.__lrrMode('trainer')"); pg.wait_for_timeout(100)
    pg.focus('body'); pg.keyboard.press('Space'); pg.wait_for_timeout(100)
    R['trainer_started_by_space'] = pg.evaluate("document.getElementById('tintro').hidden")
    # focus on canvas? is it focusable?
    R['tcv_tabindex'] = pg.get_attribute('#tcv', 'tabindex')
    R['tsay_live'] = pg.get_attribute('#tsay', 'aria-live')
    ctx.close()
    b.close()
print(json.dumps(R, indent=1))
(HERE / 'a11y2.json').write_text(json.dumps(R, indent=1))
