const fs=require('fs');
const html=fs.readFileSync(process.argv[2],'utf8');
const s=html.slice(html.indexOf('<script>')+8,html.lastIndexOf('</script>'));
eval(s);
const L=globalThis.__LRR;
const out={};
L.SCENES.forEach((sc,i)=>{for(const f of [false,true]){const d=L.sceneDef(sc,f);out[sc.id+(f?'f':'')]={cast:Object.keys(d.cast),ball:d.ball,decoy:d.decoy||{},type:d.type,ans:d.ans,okIds:d.okIds||[]};}});
fs.writeFileSync(process.argv[3],JSON.stringify(out));
console.log(Object.keys(out).length);
