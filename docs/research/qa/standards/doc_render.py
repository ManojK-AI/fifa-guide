"""Render the Docs read XML into readable markdown-ish text with block ids (read-only helper)."""
import json, sys, re
import xml.etree.ElementTree as ET
raw = json.load(open(sys.argv[1]))
xml = raw['data']['xml']
root = ET.fromstring(xml)
out = []
last_full = ['']
def fullid(i):
    if i is None: return ''
    if i.startswith('.'):
        return last_full[0] + i
    m = re.match(r'(.+?)\.\d+$', i)
    if m: last_full[0] = m.group(1)
    return i
def inline(el):
    s = ''
    if el.tag == 'text':
        s += el.text or ''
        for c in el:
            s += inline(c)
            s += c.tail or ''
        return s
    if el.tag == 'bold':
        t = (el.text or '') + ''.join(inline(c) + (c.tail or '') for c in el)
        return '**' + t + '**'
    if el.tag == 'italic':
        t = (el.text or '') + ''.join(inline(c) + (c.tail or '') for c in el)
        return '*' + t + '*'
    if el.tag == 'code':
        t = (el.text or '') + ''.join(inline(c) + (c.tail or '') for c in el)
        return '`' + t + '`'
    if el.tag == 'link':
        t = (el.text or '') + ''.join(inline(c) + (c.tail or '') for c in el)
        return '[' + t + '](' + el.get('href', '') + ')'
    if el.tag == 'date':
        return '{date:' + el.get('value', '') + '}'
    if el.tag == 'mention':
        return '@' + (el.get('name') or el.get('user') or el.get('ref') or '')
    if el.tag in ('dropdown', 'chip'):
        return '{' + el.tag + ':' + json.dumps(el.attrib) + '}'
    t = (el.text or '') + ''.join(inline(c) + (c.tail or '') for c in el)
    return '<' + el.tag + ' ' + json.dumps(el.attrib) + '>' + t
def para_text(p):
    s = p.text or ''
    for c in p:
        s += inline(c) + (c.tail or '')
    return s
def walk(el, depth=0, listkind=None, idx=None):
    tag = el.tag
    i = fullid(el.get('id'))
    if tag == 'doc':
        for c in el: walk(c, depth)
        return
    if tag == 'paragraph':
        h = el.get('heading')
        txt = para_text(el)
        prefix = ('#' * int(h) + ' ') if h else ''
        out.append(f'[{i}] ' + '  ' * depth + prefix + txt)
        return
    if tag == 'list':
        k = el.get('kind')
        n = 0
        for c in el:
            n += 1
            walk(c, depth, k, n)
        return
    if tag == 'listItem':
        mark = f'{idx}.' if listkind == 'ordered' else ('- [ ]' if listkind == 'task' else '-')
        first = True
        for c in el:
            if c.tag == 'paragraph' and first:
                out.append(f'[{i}] ' + '  ' * depth + mark + ' ' + para_text(c))
                first = False
            else:
                walk(c, depth + 1)
        return
    if tag == 'table':
        out.append(f'[{i}] TABLE')
        for r in el:
            cells = []
            for cell in r:
                ps = []
                for p in cell:
                    if p.tag == 'paragraph': ps.append(para_text(p))
                    else: ps.append(ET.tostring(p, encoding='unicode')[:200])
                cells.append(' / '.join(ps))
            out.append('   | ' + ' | '.join(cells) + ' |' + ('  <header>' if r.get('header') else ''))
        return
    # other
    out.append(f'[{i}] <{tag} {json.dumps(el.attrib)}> ' + ''.join(el.itertext())[:300])
walk(root)
print('\n'.join(out))
