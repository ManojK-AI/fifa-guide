"""8. Layout: widths x light/dark x games x tabs - horizontal scroll, elements off-screen, truncated text; key chip truncation sweep; trainer overlays."""
from common import *
from playwright.sync_api import sync_playwright
L = Log('layout')
OVER_JS = r"""()=>{
 const W=document.documentElement.clientWidth;
 const out={sw:document.documentElement.scrollWidth,cw:W,off:[],trunc:[]};
 const scrollers=[...document.querySelectorAll('.tabs,.tlist,.tover,#tabs')];
 const name=el=>(el.id?'#'+el.id:el.tagName.toLowerCase()+(el.className&&typeof el.className==='string'?'.'+el.className.trim().split(/\s+/).join('.'):''));
 for(const el of document.querySelectorAll('body *')){
   if(!el.checkVisibility())continue;
   const r=el.getBoundingClientRect();if(r.width===0||r.height===0)continue;
   if(scrollers.some(s=>s!==el&&s.contains(el)))continue;
   if(r.right>W+0.5||r.left<-0.5)out.off.push(name(el)+' ['+Math.round(r.left)+','+Math.round(r.right)+'] '+(el.textContent||'').trim().slice(0,40));
   const cs=getComputedStyle(el);
   if((cs.overflowX==='hidden'||cs.overflow==='hidden'||cs.textOverflow==='ellipsis')&&el.scrollWidth>el.clientWidth+1&&el.tagName!=='CANVAS'&&!el.classList.contains('screen')&&!el.classList.contains('stage')&&!el.classList.contains('card'))
     out.trunc.push(name(el)+' sw='+el.scrollWidth+' cw='+el.clientWidth+' "'+(el.textContent||'').trim().slice(0,50)+'"');
 }
 return out;}"""
with sync_playwright() as p:
    b = p.chromium.launch()
    for w in (320, 390, 820, 1280):
        for dark in (False, True):
            for game in ('fc26', 'fc23'):
                ctx, pg, errs = open_page(b, w, 900, dark=dark, game=game)
                for m in ('trainer', 'ai', 'replays', 'plan'):
                    pg.evaluate(f"window.__lrrMode('{m}')"); pg.wait_for_timeout(150)
                    r = pg.evaluate(OVER_JS)
                    tag = f'{w}/{"dark" if dark else "light"}/{game}/{m}'
                    L.check(r['sw'] <= r['cw'], f'{tag}: no horizontal page scroll', (r['sw'], r['cw']))
                    L.check(not r['off'], f'{tag}: nothing sticks out of the viewport', r['off'][:6])
                    if r['trunc']:
                        L.note(f'{tag}: clipped/ellipsised: {r["trunc"][:8]}')
                L.check(not errs, f'{w}/{dark}/{game}: no console errors', errs[:3])
                ctx.close()
    # key chip truncation across every clip, phone widths, both games
    SWEEP = r"""([i,dw,dr])=>{const out=[];
      for(const side of ['wrong','right']){const dur=side==='wrong'?dw:dr;
        for(let ct=0;ct<=dur;ct+=0.1){window.__lrrShow(i,side,ct,'board');
          const kc=document.getElementById('keychip');if(kc.classList.contains('off'))continue;
          const lab=document.querySelector('#kcRow > span:last-child'),kb=document.querySelector('#kcRow .kb');
          const r=kc.getBoundingClientRect(),bug=document.querySelector('#screen .bug').getBoundingClientRect();
          const s=lab.textContent+' | sw='+lab.scrollWidth+' cw='+lab.clientWidth+' kb='+Math.round(kb.getBoundingClientRect().width)+' chip='+Math.round(r.width)+' overlapBug='+(r.left<bug.right&&r.top<bug.bottom);
          if((lab.scrollWidth>lab.clientWidth+1||r.left<bug.right)&&!out.includes(s))out.push(s);}}
      return out;}"""
    for w in (320, 390):
        for game in ('fc26', 'fc23'):
            ctx, pg, errs = open_page(b, w, 844, game=game)
            bad = {}
            for i, tid in enumerate(TIDS):
                r = pg.evaluate(SWEEP, [i, TAC[tid]['wrong']['dur'], TAC[tid]['right']['dur']])
                if r: bad[tid] = r
            L.check(not bad, f'{w}/{game}: key chip labels fit (no ellipsis, no overlap with the bug)', {k: v for k, v in list(bad.items())})
            ctx.close()
    # trainer summary overlay fit at each width (scrollable overlay = clipped content)
    for w, h in ((320, 640), (390, 844), (820, 1180), (1280, 900)):
        ctx, pg, errs = open_page(b, w, h)
        pg.evaluate("window.__lrrTrain(9,false,'reveal','timeout','board')"); pg.click('#tnext'); pg.wait_for_timeout(200)
        r = pg.evaluate("""(()=>{const o=document.getElementById('tsum');return {sh:o.scrollHeight,ch:o.clientHeight,sw:o.scrollWidth,cw:o.clientWidth}})()""")
        L.check(r['sh'] <= r['ch'] + 1, f'{w}x{h}: trainer summary fits its overlay', r)
        pg.evaluate("window.__lrrMode('trainer')")
        r2 = pg.evaluate("""(()=>{const o=document.getElementById('tintro');return {sh:o.scrollHeight,ch:o.clientHeight}})()""")
        ctx.close()
        ctx, pg, errs = open_page(b, w, h)
        r2 = pg.evaluate("""(()=>{const o=document.getElementById('tintro');return {sh:o.scrollHeight,ch:o.clientHeight}})()""")
        L.check(r2['sh'] <= r2['ch'] + 1, f'{w}x{h}: trainer intro fits its overlay', r2)
        # end card fits
        pg.evaluate("window.__lrrMode('replays')"); pg.evaluate("window.__lrrShow(0,'right',7,'board')")
        pg.evaluate("document.getElementById('endcard').hidden=false")
        ctx.close()
    b.close()
L.dump()
