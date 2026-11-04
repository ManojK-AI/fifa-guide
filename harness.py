"""Headless harness for the Replay Room: wraps the fragment like the publisher does, serves local fonts, collects errors."""
import pathlib, re

W = pathlib.Path(__file__).parent
FP = W / 'fontpkg'
LIVE = (W / 'base' / 'replay-room-fifa23.html').read_text()
WRAP_HEAD = LIVE[:LIVE.index('<title>')]           # the publisher's own skeleton
WRAP_TAIL = '\n</body></html>'
URL = 'https://lrr.test/'

FONT_CSS = ''.join(
    f"@font-face{{font-family:'Big Shoulders Display';font-style:normal;font-weight:{w};font-display:swap;src:url(https://fonts.local/bsd-{w}.woff2) format('woff2')}}"
    for w in (600, 700, 800, 900)) + \
    "@font-face{font-family:'Instrument Sans';font-style:normal;font-weight:400 700;font-stretch:75% 100%;font-display:swap;src:url(https://fonts.local/is-wdth.woff2) format('woff2')}" + \
    "@font-face{font-family:'Kalam';font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.local/kalam.woff2) format('woff2')}"

FILES = {f'bsd-{w}.woff2': FP / 'fontsource-big-shoulders-display-5.3.0/package/files' / f'big-shoulders-display-latin-{w}-normal.woff2' for w in (600, 700, 800, 900)}
FILES['is-wdth.woff2'] = FP / 'fontsource-variable-instrument-sans-5.3.0/package/files/instrument-sans-latin-wdth-normal.woff2'
FILES['kalam.woff2'] = FP / 'fontsource-kalam-5.3.0/package/files/kalam-latin-400-normal.woff2'

def page_html(path=None):
    frag = (pathlib.Path(path) if path else W / 'replay-room.html').read_text()
    return WRAP_HEAD + frag + WRAP_TAIL

def attach(page, html):
    errs = []
    page.on('pageerror', lambda e: errs.append('pageerror: ' + str(e)))
    page.on('console', lambda m: errs.append('console.' + m.type + ': ' + m.text) if m.type in ('error', 'warning') else None)
    def route(r):
        u = r.request.url
        if u.startswith(URL):
            return r.fulfill(status=200, content_type='text/html; charset=utf-8', body=html)
        if u.startswith('https://fonts.googleapis.com/'):
            return r.fulfill(status=200, content_type='text/css', body=FONT_CSS)
        if u.startswith('https://fonts.local/'):
            name = u.rsplit('/', 1)[1]
            return r.fulfill(status=200, content_type='font/woff2', body=FILES[name].read_bytes())
        return r.abort()
    page.route('**/*', route)
    return errs

def open_page(browser, width=390, height=844, dark=False, game=None, path=None, storage=None):
    ctx = browser.new_context(viewport={'width': width, 'height': height}, device_scale_factor=2 if width < 700 else 1,
                              color_scheme='dark' if dark else 'light', reduced_motion='no-preference')
    page = ctx.new_page()
    html = page_html(path)
    errs = attach(page, html)
    init = ''
    if game:
        init += f"try{{localStorage.setItem('lrr:game','{game}')}}catch(e){{}};"
    for k, v in (storage or {}).items():
        init += f"try{{localStorage.setItem('lrr:{k}','{v}')}}catch(e){{}};"
    if init:
        page.add_init_script(init)
    page.goto(URL)
    page.wait_for_timeout(400)
    page.evaluate('document.fonts && document.fonts.ready')
    return ctx, page, errs
