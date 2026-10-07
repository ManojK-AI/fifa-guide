"""Read-only plain-language scan of audit text (both games) and the doc: long sentences, abbreviations, update naming, button notation."""
import json, re, pathlib, collections, sys
HERE = pathlib.Path(__file__).parent; WORK = HERE.parent.parent
games = {g: json.load(open(WORK / 'audit' / f'{g}.json')) for g in ('fc26', 'fc23')}
doc = (HERE / 'doc_render.txt').read_text()

def units(g):
    d = games[g]
    for k, v in d['static'].items():
        yield f'static:{k}', v
    for sec in ('coach', 'say', 'keys', 'fb'):
        for k, v in d[sec].items():
            yield f'{sec}:{k}', '\n'.join(v) if isinstance(v, list) else v

SENT = re.compile(r'(?<=[.!?])\s+(?=[A-Z“"(])')
def sentences(txt):
    for line in txt.splitlines():
        line = line.strip()
        if not line: continue
        for s in SENT.split(line):
            yield s.strip()

out = {}
for g in games:
    longs = []
    seen = set()
    for where, txt in units(g):
        for s in sentences(txt):
            n = len(re.findall(r"[A-Za-z0-9’'+.-]+", s))
            if n > 25 and s not in seen:
                seen.add(s); longs.append((n, where, s))
    out[g + '_long'] = sorted(longs, reverse=True)
doc_long = []
for line in doc.splitlines():
    m = re.match(r'\[(\S+)\]\s*(.*)', line)
    if not m: continue
    bid, txt = m.groups()
    txt = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', txt)
    for s in sentences(txt.lstrip('-#0123456789. ')):
        n = len(re.findall(r"[A-Za-z0-9’'+.-]+", s))
        if n > 25: doc_long.append((n, bid, s))
out['doc_long'] = sorted(doc_long, reverse=True)

# update naming variants (page fc26 + doc)
pat = re.compile(r"(Title Update \d[\d.]*|[Uu]pdate \d\.\d\.\d|\bTU ?\d[\d.]*|\bEA \d\.\d\.\d|\bSince \d\.\d\.\d|\(\d\.\d\.\d\)|\bpatch(?:es)? ?[\d.]*|May 2026 update|The World.s Game|update notes|Pitch Notes)")
cnt = collections.Counter()
for where, txt in units('fc26'):
    for m in pat.findall(txt): cnt[('page', re.sub(r'\d[\d.]*', 'N', m))] += 1
for m in pat.findall(doc): cnt[('doc', re.sub(r'\d[\d.]*', 'N', m))] += 1
out['update_naming'] = sorted(((k[0], k[1], v) for k, v in cnt.items()), key=lambda x: (x[0], -x[2]))

# button notation variants
bpat = re.compile(r"(double-tap (?:B|shoot|of B)|\bB, B\b|\bB B\b|B then A|B, then A|LB \+ RB \+ X, X|hold [A-Z]{1,2}\b|Hold [A-Z]{1,2}\b|[A-Z]{1,2} hold\b|switch \(LB\)|\(LB\)|[Ff]lick (?:the )?(?:right stick|RS))")
bc = collections.Counter()
for g in games:
    for where, txt in units(g):
        for m in bpat.findall(txt): bc[(g, m)] += 1
for m in bpat.findall(doc): bc[('doc', m)] += 1
out['button_notation'] = sorted(((k[0], k[1], v) for k, v in bc.items()))

# abbreviations seen in fc26 text
abbr = collections.Counter()
for where, txt in units('fc26'):
    for m in re.findall(r"\b(?:[A-Z]{2,4}s?|\d-\d-\d(?: \(\d\))?)\b", txt): abbr[m] += 1
out['abbr_fc26'] = abbr.most_common(60)
(HERE / 'language.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
for g in ('fc26', 'fc23'):
    print(f'=== {g}: sentences over 25 words: {len(out[g + "_long"])}')
    for n, w, s in out[g + '_long']: print(f'  {n:3} {w:14} {s}')
print(f'=== doc: sentences over 25 words: {len(out["doc_long"])}')
for n, w, s in out['doc_long']: print(f'  {n:3} {w:20} {s}')
print('=== update naming'); [print('  ', *r) for r in out['update_naming']]
print('=== button notation'); [print('  ', *r) for r in out['button_notation']]
print('=== abbreviations (fc26)'); print('  ', out['abbr_fc26'])
