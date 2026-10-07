"""WCAG 2.x contrast ratios for the page's colour tokens and fixed overlay colours (read-only analysis)."""
import json, pathlib

def hex2rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))

def lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def lum(rgb):
    r, g, b = (lin(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def over(fg, a, bg):
    """composite fg with alpha a over bg (sRGB space, as browsers do)"""
    return tuple(f * a + b * (1 - a) for f, b in zip(fg, bg))

def ratio(fg, bg):
    l1, l2 = lum(fg), lum(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)

T = {
 'light': dict(bg='#EAEFEA', panel='#FFFFFF', ink='#0F1C16', ink2='#4B5B53', rule='#CBD6CF', chip='#DDE5E0', accent='#FFD31A', accentInk='#1A1500', good='#07839A', bad='#C4322A', monitor='#09100D'),
 'dark':  dict(bg='#0B1310', panel='#121C18', ink='#E4ECE6', ink2='#93A49B', rule='#24342D', chip='#1A2722', accent='#FFD31A', accentInk='#1A1500', good='#43D2E4', bad='#FF6B5F', monitor='#040806'),
}
rows = []
def add(theme, what, where, fg, bg, need, note='', fga=1.0):
    f = hex2rgb(fg) if isinstance(fg, str) else fg
    bgc = hex2rgb(bg) if isinstance(bg, str) else bg
    if fga < 1: f = over(f, fga, bgc)
    r = ratio(f, bgc)
    rows.append(dict(theme=theme, what=what, where=where, fg=fg if isinstance(fg, str) else 'blend', bg=bg if isinstance(bg, str) else 'blend', ratio=round(r, 2), need=need, ok=r >= need, note=note))

for th, t in T.items():
    for bgk in ('bg', 'panel', 'chip'):
        add(th, '--ink-2 text', f'on --{bgk}', t['ink2'], t[bgk], 4.5)
    for k in ('good', 'bad'):
        for bgk in ('panel', 'bg', 'chip'):
            add(th, f'--{k} text', f'on --{bgk}', t[k], t[bgk], 4.5)
    add(th, '--accent-ink on --accent', '.drill, .play, .looks numbers, .clip-ref:hover', t['accentInk'], t['accent'], 4.5)
    add(th, '--accent as text', 'on --panel (if used as text)', t['accent'], t['panel'], 4.5, 'not used as text on panels; shown for completeness')
    add(th, '.src link (--ink-2, .78rem/600)', 'on --panel', t['ink2'], t['panel'], 4.5)
    add(th, '.src link (--ink-2, .78rem/600)', 'on --bg', t['ink2'], t['bg'], 4.5)
    add(th, '.n26 label .note-k (--ink-2)', 'on --chip', t['ink2'], t['chip'], 4.5)
    add(th, '.n26 body .n26-t (--ink)', 'on --chip', t['ink'], t['chip'], 4.5)
    add(th, '.n26 yellow left border (non-text)', 'vs --chip box', t['accent'], t['chip'], 3.0, 'decorative edge; 3:1 only needed if it carries meaning')
    add(th, '.n26 yellow left border (non-text)', 'vs --panel card', t['accent'], t['panel'], 3.0, 'decorative edge')
    # opacity-reduced small text
    add(th, '.segc.lv small (--ink-2 @ .85)', 'on --chip (unselected level)', t['ink2'], t['chip'], 4.5, fga=0.85)
    add(th, '.segc.lv small (--ink @ .85)', 'on --panel (selected level)', t['ink'], t['panel'], 4.5, fga=0.85)
    add(th, '.mtab small (--ink-2)', 'on --chip (unselected tab)', t['ink2'], t['chip'], 4.5)
    add(th, '.mtab[selected] small (--bg @ .75)', 'on --ink', t['bg'], t['ink'], 4.5, fga=0.75)
    add(th, '.titem[current] .tcue (--bg @ .72)', 'on --ink', t['bg'], t['ink'], 4.5, fga=0.72)
    add(th, '.reel-btn[pressed] small (--bg @ .75)', 'on --ink', t['bg'], t['ink'], 4.5, fga=0.75)
    add(th, '.kword "hold"/"then" (--ink @ .8, 11px)', 'on --panel (coach Buttons)', t['ink'], t['panel'], 4.5, fga=0.8)
    add(th, '.kplus "+" (--ink @ .7)', 'on --panel', t['ink'], t['panel'], 3.0, 'symbol; treat as graphic', fga=0.7)
    # non-text
    add(th, 'focus ring --good (non-text)', 'vs --bg', t['good'], t['bg'], 3.0)
    add(th, 'focus ring --good (non-text)', 'vs --chip', t['good'], t['chip'], 3.0)
    add(th, 'focus ring --good (non-text)', 'vs --panel', t['good'], t['panel'], 3.0)
    add(th, 'focus ring --good (non-text)', 'vs monitor overlay', t['good'], '#0A110E', 3.0)
    add(th, 'scrub fill --bad (non-text)', 'vs --chip track', t['bad'], t['chip'], 3.0)
    add(th, 'scrub fill --good (non-text)', 'vs --chip track', t['good'], t['chip'], 3.0)
    add(th, 'scrub fill --ink-2 card seg (non-text)', 'vs --chip track', t['ink2'], t['chip'], 3.0)
    add(th, 'checkbox accent --good (non-text)', 'vs --panel', t['good'], t['panel'], 3.0)
    add(th, '.titem border --rule (non-text)', 'vs --bg', t['rule'], t['bg'], 3.0, 'pill outline; the label text identifies it, so advisory')
    add(th, '.ibtn border --rule (non-text)', 'vs --bg', t['rule'], t['bg'], 3.0, 'transport buttons (restart/prev/next): the icon is the only other cue')

# Fixed broadcast colours (same in both themes)
pitch = hex2rgb('#2F7942')
ov80 = over(hex2rgb('#040907'), 0.80, pitch)
ov74 = over(hex2rgb('#040907'), 0.74, pitch)
fx = [
 ('caption .who "COACH" #FFD31A', '#0A120F caption bar', '#FFD31A', '#0A120F', 4.5),
 ('caption text #EEF3EF', '#0A120F', '#EEF3EF', '#0A120F', 4.5),
 ('.bug-state "WRONG" #fff (15px/800, not large)', '#FF5148', '#FFFFFF', '#FF5148', 4.5),
 ('.tverdict.bad "Wrong/Too slow" #fff (19px/900, large)', '#FF5148', '#FFFFFF', '#FF5148', 3.0),
 ('.tchoice.bad #fff (15.2px/700, not large)', '#FF5148', '#FFFFFF', '#FF5148', 4.5),
 ('.flash.bad "Conceded" #fff (large)', '#E5433A', '#FFFFFF', '#E5433A', 3.0),
 ('canvas tag, bad: #fff 11.5px/600', '#FF5148', '#FFFFFF', '#FF5148', 4.5),
 ('canvas tag, good: #0E1A14 11.5px/600', '#3FE0F0', '#0E1A14', '#3FE0F0', 4.5),
 ('.k-B glyph #fff 12.5px/800', '#E5473C', '#FFFFFF', '#E5473C', 4.5),
 ('.k-X glyph #fff 12.5px/800', '#2F7FE6', '#FFFFFF', '#2F7FE6', 4.5),
 ('.k-A glyph #0B0F0D', '#5BC34C', '#0B0F0D', '#5BC34C', 4.5),
 ('.k-Y glyph #0B0F0D', '#F3C033', '#0B0F0D', '#F3C033', 4.5),
 ('.keychip.bad .kc-tag #FF8E86 10.5px', 'rgba(6,11,9,.9) chip', '#FF8E86', '#0A0F0D', 4.5),
 ('.kc-tag #3FE0F0 10.5px', 'chip', '#3FE0F0', '#0A0F0D', 4.5),
 ('.tbtn / .tnext #1A1500 on #FFD31A', '', '#1A1500', '#FFD31A', 4.5),
]
for what, where, fg, bg, need in fx:
    add('both', what, where, fg, bg, need)
add('both', '.tover-s #D3DDD7 (.93rem)', 'overlay rgba(4,9,7,.8) over pitch', '#D3DDD7', ov80, 4.5)
add('both', '.tover-best #9FB1A8 (.82rem)', 'overlay rgba(4,9,7,.8) over pitch', '#9FB1A8', ov80, 4.5)
add('both', '.tover-s b #FFE24A', 'overlay .8 over pitch', '#FFE24A', ov80, 4.5)
add('both', '.card-k #3FE0F0', 'overlay .74 over pitch', '#3FE0F0', ov74, 4.5)
add('both', '.end-row ghost button #fff on rgba(255,255,255,.15)', 'over endcard .66 overlay', '#FFFFFF', over(hex2rgb('#FFFFFF'), .15, over(hex2rgb('#040907'), .66, pitch)), 4.5)
add('both', '.tchoice #fff on rgba(255,255,255,.07)', 'over #0A120F', '#FFFFFF', over(hex2rgb('#FFFFFF'), .07, hex2rgb('#0A120F')), 4.5)
add('both', '.tchoice:disabled (opacity .55)', 'over #0A120F (disabled: exempt)', over(hex2rgb('#FFFFFF'), .55, hex2rgb('#0A120F')), hex2rgb('#0A120F'), 4.5, 'disabled controls are exempt')

out = pathlib.Path(__file__).parent / 'contrast.json'
out.write_text(json.dumps(rows, indent=1))
w = max(len(r['what']) for r in rows)
for r in rows:
    flag = 'ok ' if r['ok'] else 'FAIL'
    print(f"{flag} {r['theme']:5} {r['ratio']:5.2f}:1 (need {r['need']}) {r['what']:<{w}} {r['where']}  {r['note']}")
