"""Read-only: replays canvas under throwing storage, screenshot for visual confirmation."""
import sys, pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent; WORK = HERE.parent.parent; sys.path.insert(0, str(WORK))
from harness import page_html, attach, URL
THROW = """(function(){const t={get(){throw new DOMException('denied','SecurityError')}};try{Object.defineProperty(window,'localStorage',t)}catch(e){};})();"""
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=1)
    pg = ctx.new_page(); errs = attach(pg, page_html()); pg.add_init_script(THROW)
    pg.goto(URL); pg.wait_for_timeout(500)
    pg.screenshot(path=str(HERE / 'shots' / 'storage_throw_trainer.png'))
    pg.click('#mt-replays'); pg.wait_for_timeout(1500)
    pg.screenshot(path=str(HERE / 'shots' / 'storage_throw_replays.png'))
    print('errors', errs)
    b.close()
