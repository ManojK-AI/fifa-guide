const fs=require('fs');
const html=fs.readFileSync(process.argv[2],'utf8');
const s=html.slice(html.indexOf('<script>')+8,html.lastIndexOf('</script>'));
eval(s.replace("if(typeof document==='undefined'){globalThis.__LRR={","if(typeof document==='undefined'){globalThis.__LRR={SAY26,"));
const L=globalThis.__LRR;
const rows=[];
for(const t of L.TACTICS)for(const side of ['wrong','right']){const c=side==='wrong'?t.W:t.R;const say=t[side].say||[];
  for(let i=0;i<say.length;i++){const a=L.realOf(c,say[i][0]);const e=i+1<say.length?L.realOf(c,say[i+1][0]):c.real;
    rows.push({id:t.id,side,shown:+(e-a).toFixed(2),words:say[i][1].split(/\s+/).length,text:say[i][1]});}}
const bad=rows.filter(r=>r.shown<=0.5&&r.words>=6);
console.log('captions total',rows.length,'| on screen <=0.5 s with >=6 words:',bad.length,'| <=0.5 s any:',rows.filter(r=>r.shown<=0.5).length);
bad.sort((a,b)=>a.shown-b.shown).forEach(r=>console.log(`${r.id} ${r.side}: ${r.shown}s, ${r.words} words: "${r.text}"`));
