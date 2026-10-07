// Every text drawn on the canvases (annotations, zone labels, flashes, trainer marks) - not game-mapped
const fs=require('fs');
const html=fs.readFileSync(process.argv[2],'utf8');
const s=html.slice(html.indexOf('<script>')+8,html.lastIndexOf('</script>'));
eval(s);
const L=globalThis.__LRR;
for(const t of L.TACTICS){
  for(const side of ['wrong','right']){
    const d=t[side];
    const texts=[];
    for(const a of (d.ann||[]))if(a.text)texts.push(a.k+':'+a.text+' @'+(a.t||[]).join('-'));
    for(const f of (d.fx||[]))texts.push('fx:'+f[1]);
    if(texts.length)console.log(t.id,side,JSON.stringify(texts));
  }
}
for(const sc of L.SCENES){if(sc.markText||sc.q)console.log(sc.id,'markText',sc.markText||'', 'q', sc.q||'');}
// does the drawing code ever consult GAME for annotation text?
const draw=s.slice(s.indexOf('function drawAnn'),s.indexOf('function drawTrails'));
console.log('drawAnn uses gsay/is26?', /gsay|is26|GAME/.test(draw));
