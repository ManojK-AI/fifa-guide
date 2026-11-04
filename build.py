#!/usr/bin/env python3
"""Builds replay-room.html (FC 26 + FIFA 23) from the FIFA 23 base page plus parts/. Every edit is an exact, single-occurrence replace.

The base page is base/replay-room-fifa23.html (the published v3 FIFA 23 page with the publisher's wrapper).
It used to live outside the repo at ../live/index.html; see base/README.md."""
import pathlib, re, subprocess, sys

W = pathlib.Path(__file__).parent
P = W / 'parts'
live = (W / 'base' / 'replay-room-fifa23.html').read_text()

# 1. strip the publish wrapper: keep from <title> to the end of the last </script>
start = live.index('<title>')
end = live.rindex('</script>') + len('</script>')
s = live[start:end] + '\n'

def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        sys.exit(f'expected {count} of {old[:90]!r}, found {n}')
    s = s.replace(old, new)

def part(name):
    return (P / name).read_text()

subprocess.run([sys.executable, str(W / 'make_ai26.py')], check=True)
subprocess.run([sys.executable, str(W / 'make_plan26.py')], check=True)
subprocess.run([sys.executable, str(W / 'make_pro.py')], check=True)

# 2. CSS
first_style_end = s.index('</style>')
s = s[:first_style_end] + part('game.css') + s[first_style_end:]
# 2b. Pro tab CSS, after the FC 26 CSS
first_style_end = s.index('</style>')
s = s[:first_style_end] + part('pro.css') + s[first_style_end:]

# 3. masthead: game switch + eyebrow per game
rep('<p class="eyebrow">FIFA 23 · Ultimate AI · your 4-3-3 Attack</p>',
    '<div class="gsw" role="group" aria-label="Which game"><span class="gsw-k" aria-hidden="true">Game</span>'
    '<div class="segc"><button type="button" data-gm="fc26" aria-pressed="true">FC 26</button>'
    '<button type="button" data-gm="fc23" aria-pressed="false">FIFA 23</button></div></div>\n'
    '      <p class="eyebrow"><span class="g26">EA SPORTS FC 26 · Squad Battles AI · your 4-3-3</span>'
    '<span class="g23">FIFA 23 · Ultimate AI · your 4-3-3 Attack</span></p>')

# 4. scan card wording that named FIFA
rep('FIFA works the same way, just faster.', 'The game works the same way, just faster.')

# 5. AI moves tab: FIFA 23 report kept, FC 26 report added
rep('<section class="panel" id="p-ai" role="tabpanel" aria-labelledby="mt-ai" hidden>\n',
    '<section class="panel" id="p-ai" role="tabpanel" aria-labelledby="mt-ai" hidden>\n    <div class="g23">\n')
rep('    </section>\n  </section>\n\n  <section class="panel" id="p-replays"',
    '    </section>\n    </div>\n' + part('ai26.html') + '  </section>\n\n  <section class="panel" id="p-replays"')

# 6. coach card: FC 26 note
rep('<div class="note" id="cNote" hidden><p class="note-k">From your notes</p><p class="note-t" id="cNoteT"></p></div>\n',
    '<div class="note" id="cNote" hidden><p class="note-k">From your notes</p><p class="note-t" id="cNoteT"></p></div>\n'
    '      <div class="n26" id="cN26" hidden><p class="note-k">In FC 26</p><p class="n26-t" id="cN26T"></p></div>\n')

# 7. Plan tab
rep('<p class="pintro">Most of these live in', '<p class="pintro g23">Most of these live in')
rep('<ul class="checks">', '<ul class="checks g23">')
i = s.index('<ul class="checks g23">'); j = s.index('</ul>\n', i) + len('</ul>\n')
s = s[:j] + part('plan26_checks.html') + s[j:]
rep('<article class="pcard">\n        <p class="coach-k">Your match script</p>', '<article class="pcard g23">\n        <p class="coach-k">Your match script</p>')
rep('<article class="pcard">\n        <p class="coach-k">Your squad</p>', '<article class="pcard g23">\n        <p class="coach-k">Your squad</p>')
rep('<article class="pcard pwide honest">', '<article class="pcard pwide honest g23">')
rep('<article class="pcard pwide">\n        <p class="coach-k">Where this comes from</p>', '<article class="pcard pwide g23">\n        <p class="coach-k">Where this comes from</p>')
rep('</ol>\n      </article>\n    </div>\n  </section>\n\n  <p class="foot">',
    '</ol>\n      </article>\n' + part('plan26_cards.html') + '    </div>\n  </section>\n\n  <p class="foot">')

# 7b. Pro patterns: a new clip group, four advanced clips at the end of TACTICS (parts/pro_clips.js)
rep("  {id:'notes',  name:'Your notes', tab:'Notes', gap:'Your sketches'}\n",
    "  {id:'notes',  name:'Your notes', tab:'Notes', gap:'Your sketches'},\n  {id:'pro',    name:'Pro patterns', tab:'Pro', gap:'Advanced'}\n")
rep("}\n];\n\n/* ======================= Scan trainer scenes",
    "},\n" + part('pro_clips.js') + "\n];\n\n/* ======================= Scan trainer scenes")

# 7c. Pro tab: fifth section tab, its panel (parts/pro.html from make_pro.py), mode list and clip links
rep('<button type="button" class="mtab" role="tab" id="mt-plan" data-m="plan" aria-controls="p-plan" aria-selected="false" tabindex="-1"><strong>Plan</strong><small>Settings, script</small></button>\n',
    '<button type="button" class="mtab" role="tab" id="mt-plan" data-m="plan" aria-controls="p-plan" aria-selected="false" tabindex="-1"><strong>Plan</strong><small>Settings, script</small></button>\n'
    '    <button type="button" class="mtab" role="tab" id="mt-pro" data-m="pro" aria-controls="p-pro" aria-selected="false" tabindex="-1"><strong>Pro</strong><small>Advanced kit</small></button>\n')
rep('    </div>\n  </section>\n\n  <p class="foot">', '    </div>\n  </section>\n\n' + part('pro.html') + '\n  <p class="foot">')
rep("const MODES=['trainer','ai','replays','plan'];", "const MODES=['trainer','ai','replays','plan','pro'];")
rep("['p-plan','p-ai','tmissed'].forEach(", "['p-plan','p-ai','p-pro','tmissed'].forEach(")

# 8. JS: reel lists move into the game block
rep("const REEL = ['U1','A1','U2','U3','A2','A3','U6'];\n", '')
rep('\n];\n\n/* ======================= Engine ======================= */',
    '\n];\n\n' + part('game.js') + '\n/* ======================= Engine ======================= */')

# coach card
rep("$('cWatch').textContent=tac.watch;$('cCue').textContent=tac.cue;",
    "const f=f26(tac.id);$('cWatch').textContent=f.watch||tac.watch;$('cCue').textContent=f.cue||tac.cue;")
rep("$('cSetWrap').hidden=!tac.setting;$('cSet').textContent=tac.setting||'';",
    "const set=f.setting!=null?f.setting:tac.setting;$('cSetWrap').hidden=!set;$('cSet').textContent=set||'';")
rep("""$('cKeys').innerHTML=tac.keys.map(k=>'<div class="keyrow">'+keysHTML(k[0])+'<span>'+esc(k[1])+'</span></div>').join('');""",
    """$('cKeys').innerHTML=(f.keys||tac.keys.map(k=>gkey(k[0],k[1]))).map(k=>'<div class="keyrow">'+keysHTML(k[0])+'<span>'+esc(k[1])+'</span></div>').join('');""")
rep("""$('cNote').hidden=!tac.note;$('cNoteT').textContent=tac.note?'“'+tac.note+'”':'';""",
    """$('cNote').hidden=!tac.note;$('cNoteT').textContent=tac.note?'“'+tac.note+'”':'';
  $('cN26').hidden=!f.n;$('cN26T').textContent=f.n||'';""")
rep("""const src=tac.src;$('cSrc').hidden=!src;$('cSrc').innerHTML=src?'Source: <a href="'+esc(src.u)+'" target="_blank" rel="noopener">'+esc(src.t)+'</a>':'';""",
    """const srcs=f.src?[].concat(f.src):tac.src?[tac.src]:[];$('cSrc').hidden=!srcs.length;
  $('cSrc').innerHTML=srcs.length?(srcs.length>1?'Sources: ':'Source'+(is26()&&!f.src?' (FIFA 23)':'')+': ')+srcs.map(x=>'<a href="'+esc(x.u)+'" target="_blank" rel="noopener">'+esc(x.t)+'</a>').join(' · '):'';""")

# live captions and key chips
rep('for(const b of clip.say)if(b[0]<=ct)say=b[1];', 'for(const b of clip.say)if(b[0]<=ct)say=gsay(b[1]);')
rep("""kcRow.innerHTML=keysHTML(key[1])+'<span>'+esc(key[2])+'</span>';""",
    """const gk2=gkey(key[1],key[2]);kcRow.innerHTML=keysHTML(gk2[0])+'<span>'+esc(gk2[1])+'</span>';""")

# trainer feedback
rep('setTSay(lead+d.fb);', "TS.lead=lead;setTSay(lead+G(d,'fb'));")
rep("tcv.setAttribute('aria-label',(ok?'Right. ':'Wrong. ')+d.fb);", "tcv.setAttribute('aria-label',(ok?'Right. ':'Wrong. ')+G(d,'fb'));")

# checklist counts only the game on screen
old_checks = s[s.index('function initChecks(){'):s.index('function watchClip(id){')]
rep(old_checks, """function initChecks(){
  const boxes=[...document.querySelectorAll('[data-chk]')];
  const vis=()=>boxes.filter(c=>c.closest(is26()?'.g26':'.g23'));
  const upd=()=>{const v=vis();let n=0;v.forEach(c=>{if(c.checked)n++;});$('chkCount').textContent=n+' of '+v.length+' done';};
  boxes.forEach(c=>{c.checked=load('chk:'+c.dataset.chk)==='1';c.addEventListener('change',()=>{store('chk:'+c.dataset.chk,c.checked?'1':'0');upd();});});
  $('chkReset').addEventListener('click',()=>{vis().forEach(c=>{c.checked=false;store('chk:'+c.dataset.chk,'0');});upd();});
  upd();updChecks=upd;
}
function setGame(g,init){
  GAME=g==='fc23'?'fc23':'fc26';REEL=GAME==='fc26'?REEL26:REEL23;
  document.documentElement.setAttribute('data-game',GAME);
  document.querySelectorAll('[data-gm]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.gm===GAME?'true':'false'));
  if(init)return;
  store('game',GAME);
  if(S.mode==='reel')stopReel();else refreshStatic();
  if(TS.phase==='reveal'&&TS.sc){setTSay((TS.lead||'')+G(TS.sc.d,'fb'));tcv.setAttribute('aria-label',(TS.res&&TS.res.ok?'Right. ':'Wrong. ')+G(TS.sc.d,'fb'));}
  S.dirty=true;TS.dirty=true;updChecks();
}
document.querySelectorAll('[data-gm]').forEach(b=>b.addEventListener('click',()=>setGame(b.dataset.gm)));
""")

# start-up and debug hook
rep('function start(data){\n  buildPicker();', "function start(data){\n  setGame(load('game')||'fc26',true);\n  buildPicker();")
rep('window.__lrrMode=m=>setMode(m);', 'window.__lrrMode=m=>setMode(m);\nwindow.__lrrGame=g=>setGame(g);')


# ---------- QA fixes (fact-check, standards, functional) ----------
# play/pause icon follows playback whenever a clip is (re)selected
rep("PROG=buildProgram();refreshStatic();hideEnd();S.dirty=true;store('tid',TACTICS[S.idx].id);",
    "PROG=buildProgram();refreshStatic();hideEnd();S.dirty=true;store('tid',TACTICS[S.idx].id);setPlayIcon();")
# button combos: readable names for screen readers, "hold A" order
rep("function keysHTML(tokens){\n  return '<span class=\"kb\" aria-label=\"'+esc(tokens.filter(t=>t!=='+').join(' plus ').replace(' plus then plus ',' then '))+'\">'",
    "function keysLabel(t){\n  const nm=k=>({LS:'left stick',RS:'right stick'})[k]||k,out=[];\n  for(let i=0;i<t.length;i++){const k=t[i];\n    if(k==='+'||k==='then'){out.push(k==='+'?'plus':'then');continue;}\n    if(k==='hold'){out.push('hold '+nm(t[i+1]||''));i++;continue;}\n    if(t[i+1]==='hold'){out.push('hold '+nm(k));i++;continue;}\n    if(t[i+1]===k){out.push('double-tap '+nm(k));i++;continue;}\n    out.push(nm(k));}\n  return out.join(' ');\n}\nfunction keysHTML(tokens){\n  return '<span class=\"kb\" role=\"img\" aria-label=\"'+esc(keysLabel(tokens))+'\">'")
rep("['A','hold']", "['hold','A']", 3)
# red labels on the pitch: darker fill so white text passes contrast
rep("ctx.fillStyle=col;rrect(bx,by,w,h,5);ctx.fill();", "ctx.fillStyle=col===C.bad?'#CC3A30':col;rrect(bx,by,w,h,5);ctx.fill();")
rep("  --good:#07839A;", "  --good:#057489;")
# line labels can sit at the bottom end (C4 labels were hidden under the key chip)
rep("const q=v.pt(a.x,v.kind==='board'?4:3,0);tag(q[0],Math.max(q[1],60),a.text,col,alpha);",
    "if(a.lb==='b'){const q=v.pt(a.x,v.kind==='board'?64:65,0);tag(q[0],Math.min(q[1],H-8),a.text,col,alpha);}else{const q=v.pt(a.x,v.kind==='board'?4:3,0);tag(q[0],Math.max(q[1],60),a.text,col,alpha);}")
rep("{k:'line',x:82,c:'pen',text:'Offside line'", "{k:'line',x:82,c:'pen',lb:'b',text:'Offside line'")
rep("{k:'line',x:82,c:'pen',text:'Last defender'", "{k:'line',x:82,c:'pen',lb:'b',text:'Last defender'")
# wording shared by both games
rep("Learn every move Ultimate AI makes and how to punish it.", "Learn every move the AI makes and how to punish it.")
rep("<p class=\"coach-k\">Before kick-off · 2 minutes</p>", "<p class=\"coach-k\">Set once · check before kick-off</p>")
rep("cue:'Ball in midfield? Control a midfielder, never a CB. Let the back four hold itself.'",
    "cue:'Ball in midfield? Control a midfielder, not a CB. Switch to a CB only when their midfielder turns to face your goal.'")
rep("Let a midfielder press, and switch (LB) to the CB nearest their runner.", "Let a midfielder close him down, and press LB to switch to the CB nearest their runner.")
rep("Switch (LB) to the CB nearest the runner and stay goal-side.", "Press LB to switch to the CB nearest the runner and stay goal-side.")
rep("Hold your line and switch (LB) to the CB nearest the runner.", "Hold your line and press LB to switch to the CB nearest the runner.")
rep("Switch to the pivot (LB) and stand him up.", "Press LB to switch to the pivot and block his path.")
rep("Their 10 is standing in the lane to your CM.", "Their playmaker is standing in the lane to your CM.")
rep("Blocked. Their 10 is in the lane. ", "Blocked. Their playmaker is in the lane. ")
# names that match what is on screen
rep("cb.setAttribute('aria-label','Watch the move in Replays, clip '+d.clip);", "cb.setAttribute('aria-label','Watch '+d.clip+' in Replays');")
# keyboard users keep their place when a button jumps to another tab
rep("function watchClip(id){\n  const i=TACTICS.findIndex(t=>t.id===id);if(i<0)return;\n  setMode('replays');selectTactic(i,{});",
    "function watchClip(id,kb){\n  const i=TACTICS.findIndex(t=>t.id===id);if(i<0)return;\n  setMode('replays');selectTactic(i,{});if(kb)$('playBtn').focus({preventScroll:true});")
rep("const b=e.target.closest('.clip-ref');if(b)watchClip(b.dataset.clip);", "const b=e.target.closest('.clip-ref');if(b)watchClip(b.dataset.clip,e.detail===0);")
rep("setMode('trainer');trSetFocus(b.dataset.drill);trStart();", "setMode('trainer');trSetFocus(b.dataset.drill);if(e.detail===0){trIntro();$('tstart').focus({preventScroll:true});}else trStart();")
rep("$('tclip').addEventListener('click',e=>watchClip(e.currentTarget.dataset.clip));", "$('tclip').addEventListener('click',e=>watchClip(e.currentTarget.dataset.clip,e.detail===0));")
rep("function start(data){\n  setGame(load('game')||'fc26',true);\n  buildPicker();buildTells();initChecks();",
    "function start(data){\n  setGame(load('game')||'fc26',true);\n  buildPicker();buildTells();initChecks();\n  document.querySelectorAll('.clip-ref').forEach(b=>{const t=TACTICS.find(x=>x.id===b.dataset.clip);if(t)b.setAttribute('aria-label','Watch clip '+t.id+': '+t.name);});\n  document.querySelectorAll('[data-drill]').forEach(b=>b.setAttribute('aria-label',b.dataset.drill==='def'?'Drill their-ball reads in the trainer':'Drill your-ball reads in the trainer'));\n  $('spdHalf').setAttribute('aria-label','Half speed');$('spdOne').setAttribute('aria-label','Normal speed');$('spdFast').setAttribute('aria-label','One and a half times speed');$('chkReset').setAttribute('aria-label','Clear ticks');")

# sanity: every FIFA 23 string the FC 26 maps refer to must exist
js = part('game.js')
for key in re.findall(r"^\s*'((?:[^'\\]|\\.)+)':(?:\[\[|')", js, re.M):
    if key.startswith('s') and key[1:].isdigit():
        continue
    if ("'" + key + "'") not in s:
        sys.exit('mapped string not found in page: ' + key)
out = W / 'replay-room.html'
out.write_text(s)
print('wrote', out, len(s))
