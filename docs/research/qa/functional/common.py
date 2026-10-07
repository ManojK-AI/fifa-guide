"""Shared helpers for the functional QA scripts (QA-owned; does not modify the page)."""
import sys, json, pathlib, time
W = pathlib.Path(__file__).resolve().parents[2]          # .../work
sys.path.insert(0, str(W))
from harness import open_page, page_html, attach, URL     # noqa: E402
QA = pathlib.Path(__file__).resolve().parent
SHOTS = QA / 'shots'; SHOTS.mkdir(exist_ok=True)
DATA = json.loads((QA / 'data.json').read_text())
TAC = {t['id']: t for t in DATA['tactics']}
TIDS = [t['id'] for t in DATA['tactics']]
SC = {s['id']: s for s in DATA['scenes']}

def open_clock(browser, width=1280, height=900, dark=False, game=None, storage=None, pause=False):
    """Like harness.open_page but installs Playwright's fake clock before load so RAF/time can be fast-forwarded."""
    ctx = browser.new_context(viewport={'width': width, 'height': height}, device_scale_factor=2 if width < 700 else 1,
                              color_scheme='dark' if dark else 'light', reduced_motion='no-preference')
    page = ctx.new_page()
    errs = attach(page, page_html())
    init = ''
    if game:
        init += f"try{{localStorage.setItem('lrr:game','{game}')}}catch(e){{}};"
    for k, v in (storage or {}).items():
        init += f"try{{localStorage.setItem('lrr:{k}','{v}')}}catch(e){{}};"
    if init:
        page.add_init_script(init)
    page.clock.install()
    page.goto(URL)
    page.clock.run_for(400)
    if pause:   # stop natural time flow: only run_for() advances time from here on
        page.clock.pause_at(page.evaluate('Date.now()') + 50)
        page.clock.run_for(50)
    return ctx, page, errs

class Log:
    def __init__(self, name):
        self.name = name; self.fails = []; self.oks = []; self.notes = []
    def check(self, cond, msg, detail=''):
        (self.oks if cond else self.fails).append(msg + ((' :: ' + str(detail)) if (detail and not cond) else ''))
        return cond
    def note(self, msg):
        self.notes.append(msg)
    def dump(self):
        out = {'name': self.name, 'fails': self.fails, 'oks': len(self.oks), 'notes': self.notes}
        (QA / f'result_{self.name}.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
        print(f'[{self.name}] OK checks: {len(self.oks)}  FAILS: {len(self.fails)}')
        for f in self.fails:
            print('  FAIL', f)
        for n in self.notes:
            print('  NOTE', n)

STATE_JS = """()=>({game:document.documentElement.dataset.game,
  bug:document.getElementById('bugCode').textContent, state:document.getElementById('bugState').textContent,
  clock:document.getElementById('bugClock').textContent, say:document.getElementById('say').textContent,
  reelLabel:document.getElementById('reelLabel').textContent, reelSub:document.getElementById('reelSub').textContent,
  reelPressed:document.getElementById('reelBtn').getAttribute('aria-pressed'),
  card:!document.getElementById('card').hidden, cardK:document.getElementById('cardK').textContent, cardT:document.getElementById('cardT').textContent,
  end:!document.getElementById('endcard').hidden, endTitle:document.getElementById('endTitle').textContent,
  play:document.getElementById('playBtn').getAttribute('aria-label'),
  scrub:+document.getElementById('scrub').getAttribute('aria-valuenow'),
  scrubText:document.getElementById('scrub').getAttribute('aria-valuetext'),
  keyOn:!document.getElementById('keychip').classList.contains('off'), key:document.getElementById('kcRow').innerText.replace(/\\s+/g,' ').trim(),
  kcTag:document.getElementById('kcTag').textContent,
  jumpW:document.getElementById('jumpW').getAttribute('aria-pressed'), jumpR:document.getElementById('jumpR').getAttribute('aria-pressed'),
  coachT:document.getElementById('coachT').textContent, active:[...document.querySelectorAll('.mtab')].find(b=>b.getAttribute('aria-selected')==='true').dataset.m,
  cur:(document.querySelector('.titem[aria-current="true"] .code')||{}).textContent})"""

F26, L26, SAY26, FB26 = DATA['F26'], DATA['L26'], DATA['SAY26'], DATA['FB26']
def gkey(tok, lab, game):
    return L26[lab] if game == 'fc26' and lab in L26 else [tok, lab]
def gsay(t, game):
    return SAY26.get(t, t) if game == 'fc26' else t
def gfb(sid, game):
    return FB26[sid] if game == 'fc26' and sid in FB26 else SC[sid]['fb']
def exp_coach(tid, game):
    t = TAC[tid]; f = F26.get(tid, {}) if game == 'fc26' else {}
    keys = f.get('keys') or [gkey(k[0], k[1], game) for k in t['keys']]
    labels = [k[1] + (' (Defending: Tactical)' if game == 'fc26' and k[0][0] == 'A' and len(k[0]) > 1 and k[0][1] == 'hold' else '') for k in keys]
    setting = f['setting'] if f.get('setting') is not None else t.get('setting')
    src = f.get('src')
    srcs = (src if isinstance(src, list) else [src]) if src else ([t['src']] if t.get('src') else [])
    return {'watch': f.get('watch') or t['watch'], 'cue': f.get('cue') or t['cue'], 'setting': setting or '',
            'keys': [' '.join(x for x in k[0] if x != '+') for k in keys], 'labels': labels,
            'note': t.get('note'), 'n': f.get('n'), 'srcs': srcs, 'src_label_23': game == 'fc26' and not f.get('src')}

COACH_JS = """()=>({k:document.getElementById('coachK').textContent,t:document.getElementById('coachT').textContent,
 watch:document.getElementById('cWatch').textContent,cue:document.getElementById('cCue').textContent,
 setHidden:document.getElementById('cSetWrap').hidden,set:document.getElementById('cSet').textContent,
 keyTokens:[...document.querySelectorAll('#cKeys .keyrow')].map(r=>[...r.querySelectorAll('.kb > span')].filter(s=>!s.classList.contains('kplus')).map(s=>s.textContent).join(' ')),
 keyLabels:[...document.querySelectorAll('#cKeys .keyrow > span:last-child')].map(s=>s.textContent),
 keyAria:[...document.querySelectorAll('#cKeys .kb')].map(s=>s.getAttribute('aria-label')),
 noteVis:document.getElementById('cNote').checkVisibility(),note:document.getElementById('cNoteT').textContent,
 n26Vis:document.getElementById('cN26').checkVisibility(),n26:document.getElementById('cN26T').textContent,
 srcVis:document.getElementById('cSrc').checkVisibility(),srcText:document.getElementById('cSrc').textContent,
 links:[...document.querySelectorAll('#cSrc a')].map(a=>({t:a.textContent,u:a.getAttribute('href'),tg:a.target,rel:a.rel,vis:a.checkVisibility()}))})"""
