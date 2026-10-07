// Real on-screen time of every caption (and key chip) at 1x, accounting for freeze-frame holds.
const fs=require('fs');
const html=fs.readFileSync(process.argv[2],'utf8');
const s=html.slice(html.indexOf('<script>')+8,html.lastIndexOf('</script>'));
eval(s.replace("if(typeof document==='undefined'){globalThis.__LRR={","if(typeof document==='undefined'){globalThis.__LRR={SAY26,"));
const L=globalThis.__LRR;
const rows=[];
for(const t of L.TACTICS){
  for(const side of ['wrong','right']){
    const c=side==='wrong'?t.W:t.R; const say=t[side].say||[];
    for(let i=0;i<say.length;i++){
      const a=L.realOf(c,say[i][0]); const bEnd=i+1<say.length?L.realOf(c,say[i+1][0]):c.real;
      const shown=bEnd-a; const words=say[i][1].split(/\s+/).length;
      rows.push({id:t.id,side,i,t:say[i][0],shown:+shown.toFixed(2),words,text:say[i][1],last:i===say.length-1});
    }
  }
}
const short=rows.filter(r=>r.shown<1.0);
console.log('captions total',rows.length,'shown < 1.0 s at 1x:',short.length);
for(const r of short)console.log(`${r.id} ${r.side} #${r.i} t=${r.t} shown ${r.shown}s (${r.words} words): ${r.text}`);
const wps=rows.filter(r=>!r.last&&r.words/r.shown>4.5);
console.log('\nfaster than 4.5 words/s (not last):',wps.length);
for(const r of wps)console.log(`${r.id} ${r.side} #${r.i} shown ${r.shown}s ${r.words}w = ${(r.words/r.shown).toFixed(1)} w/s: ${r.text}`);
