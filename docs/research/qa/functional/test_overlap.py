"""Canvas annotation labels hidden under the HTML overlays (bug top-left, key chip top-right) - instrumented fillText."""
from common import *
import sys
from playwright.sync_api import sync_playwright
L = Log('overlap')
INSTR = """(()=>{const o=CanvasRenderingContext2D.prototype.fillText;window.__txt=[];
CanvasRenderingContext2D.prototype.fillText=function(t,x,y){try{if(this.canvas.id==='cv'&&this.font.indexOf('11.5px')>=0){const m=this.getTransform();
 window.__txt.push({t:String(t),x:m.a*x+m.c*y+m.e,y:m.b*x+m.d*y+m.f,w:this.measureText(t).width*m.a,a:this.globalAlpha,s:m.a});}}catch(e){}
 return o.apply(this,arguments);};})();"""
SWEEP = r"""([i,dw,dr,view])=>{const out=[];
 const cvR=document.getElementById('cv').getBoundingClientRect();const dpr=document.getElementById('cv').width/cvR.width;
 for(const side of ['wrong','right']){const dur=side==='wrong'?dw:dr;
  for(let ct=0;ct<=dur;ct+=0.1){window.__txt=[];window.__lrrShow(i,side,ct,view,true);
   const kc=document.getElementById('keychip'),bug=document.querySelector('#screen .bug');
   const rects=[];const b=bug.getBoundingClientRect();rects.push(['bug',b]);
   if(!kc.classList.contains('off'))rects.push(['keychip',kc.getBoundingClientRect()]);
   for(const tx of window.__txt){if(tx.a<0.5)continue;
     const w=(tx.w/ tx.s*1+13), h=20, cx=cvR.left+tx.x/dpr, cy=cvR.top+tx.y/dpr;
     const L0=cx-w/2,R0=cx+w/2,T0=cy-h/2,B0=cy+h/2;
     for(const [nm,r] of rects){const ix=Math.min(R0,r.right)-Math.max(L0,r.left),iy=Math.min(B0,r.bottom)-Math.max(T0,r.top);
       if(ix>2&&iy>2){const k=side+' "'+tx.t+'" under '+nm+' ('+Math.round(ix)+'x'+Math.round(iy)+'px)';
         const f=out.find(o=>o.k===k);if(f)f.n++;else out.push({k,n:1,ct:+ct.toFixed(1)});}}}}}
 return out;}"""
with sync_playwright() as p:
    b = p.chromium.launch()
    for w, h in ((390, 844), (820, 1180), (1280, 900)):
        for view in ('board', 'cam'):
            for game in ('fc26', 'fc23'):
                ctx = b.new_context(viewport={'width': w, 'height': h}, device_scale_factor=2 if w < 700 else 1, color_scheme='light')
                pg = ctx.new_page(); errs = attach(pg, page_html())
                pg.add_init_script(INSTR + f"try{{localStorage.setItem('lrr:game','{game}')}}catch(e){{}}")
                pg.goto(URL); pg.wait_for_timeout(400); pg.evaluate("window.__lrrMode('replays')"); pg.wait_for_timeout(100)
                found = {}
                for i, tid in enumerate(TIDS):
                    r = pg.evaluate(SWEEP, [i, TAC[tid]['wrong']['dur'], TAC[tid]['right']['dur'], view])
                    hits = [x for x in r if x['n'] >= 3]   # visible for >= 0.3 s of clip time
                    if hits: found[tid] = [f"{x['k']} ~{x['n']/10:.1f}s from ct {x['ct']}" for x in hits]
                tag = f'{w}/{view}/{game}'
                L.check(not found, f'{tag}: no canvas label hidden under the bug or key chip', found)
                L.check(not errs, f'{tag}: no console errors', errs[:3])
                ctx.close()
    b.close()
L.dump()
