// Pull the script out of the page and run it headless (document undefined) to get TACTICS/SCENES data
const fs=require('fs');
const html=fs.readFileSync(process.argv[2],'utf8');
const s=html.slice(html.indexOf('<script>')+8,html.lastIndexOf('</script>'));
// expose the game-layer constants as well by injecting before the early return
const patched=s.replace("if(typeof document==='undefined'){globalThis.__LRR={","if(typeof document==='undefined'){globalThis.__LRR={F26,L26,SAY26,FB26,REEL23,REEL26,GROUPS,");
eval(patched);
const L=globalThis.__LRR;
const out={tactics:L.TACTICS.map(t=>({id:t.id,g:t.g,name:t.name,short:t.short,watch:t.watch,cue:t.cue,setting:t.setting,note:t.note,keys:t.keys,src:t.src,
  wrong:{dur:t.wrong.dur,say:t.wrong.say,key:t.wrong.key,real:t.W.real},right:{dur:t.right.dur,say:t.right.say,key:t.right.key,real:t.R.real}})),
  scenes:L.SCENES.map(s=>({id:s.id,clip:s.clip,side:s.side,type:s.type,fb:s.fb,tell:s.tell,act:s.act,opts:s.opts,ans:s.ans,q:s.q,qs:s.qs,decoy:s.decoy,okIds:s.okIds})),
  F26:L.F26,L26:L.L26,SAY26:L.SAY26,FB26:L.FB26,REEL23:L.REEL23,REEL26:L.REEL26,GROUPS:L.GROUPS};
fs.writeFileSync(process.argv[3],JSON.stringify(out,null,1));
console.log('tactics',out.tactics.length,'scenes',out.scenes.length);
console.log(out.tactics.map(t=>t.id+'('+t.g+')').join(' '));
const sides={};out.scenes.forEach(s=>{sides[s.side]=(sides[s.side]||0)+1;});console.log('scene sides',sides);
console.log('scene types',out.scenes.map(s=>s.id+':'+s.type+':'+s.side+':'+(s.clip||'-')).join(' '));
