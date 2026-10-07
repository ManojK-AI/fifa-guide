"""Re-test the bugs QA found: play icon, live game switch in the trainer, key chip labels, accessible names."""
import sys, pathlib, json
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from harness import open_page
fails=[]
def check(c,m):
    if not c: fails.append(m)
with sync_playwright() as p:
    b=p.chromium.launch()
    ctx,pg,errs=open_page(b,390,844)
    pg.evaluate("window.__lrrMode('replays')")
    # pause, then pick another clip: icon must say Pause (playing)
    pg.click('#playBtn'); pg.wait_for_timeout(100)
    check(pg.get_attribute('#playBtn','aria-label')=='Play','paused label')
    pg.evaluate("document.querySelector('.titem[data-i=\"3\"]').click()"); pg.wait_for_timeout(100)
    check(pg.get_attribute('#playBtn','aria-label')=='Pause','after picking a clip while paused the button should read Pause, got '+str(pg.get_attribute('#playBtn','aria-label')))
    # accessible names
    kb=pg.evaluate("[...document.querySelectorAll('#cKeys .kb')].map(k=>[k.getAttribute('role'),k.getAttribute('aria-label')])")
    check(all(r=='img' and l for r,l in kb),'kb role/label: '+str(kb))
    names=pg.evaluate("[...document.querySelectorAll('#p-ai .g26 .clip-ref')].slice(0,3).map(b=>b.getAttribute('aria-label'))")
    check(all(n and ':' in n for n in names),'clip-ref names: '+str(names))
    # U6 / D2 key names
    for tid,want in (('U6','double-tap B'),('D2','hold A')):
        i=pg.evaluate(f"+[...document.querySelectorAll('.titem')].find(b=>b.querySelector('.code').textContent==='{tid}').dataset.i")
        pg.evaluate(f"window.__lrrShow({i},'right',0.5,'board')")
        lab=pg.evaluate("[...document.querySelectorAll('#cKeys .kb')].map(k=>k.getAttribute('aria-label')).join(' | ')")
        check(want in lab, f'{tid} key names: {lab}')
    # trainer: reveal in FIFA 23, then switch to FC 26 -> feedback follows
    pg.click('[data-gm="fc23"]')
    pg.evaluate("window.__lrrTrain(12,false,'reveal',null,'board')"); pg.wait_for_timeout(100)
    before=pg.inner_text('#tsay')
    pg.click('[data-gm="fc26"]'); pg.wait_for_timeout(100)
    after=pg.inner_text('#tsay')
    check('CPU blocks almost anything' in before and 'close enough to block' in after, f'live switch fb: {before[:50]} -> {after[:50]}')
    check(not errs,'errors: '+json.dumps(errs[:5]))
    ctx.close()
    # key chip labels: no clipping at 320 and 390, both games
    for w in (320,390):
        for game in ('fc26','fc23'):
            ctx,pg,errs=open_page(b,w,800,game=game)
            pg.evaluate("window.__lrrMode('replays')")
            bad=pg.evaluate("""()=>{const out=[];const items=[...document.querySelectorAll('.titem')].map(b=>+b.dataset.i);
              for(const i of items){for(const side of ['wrong','right']){for(let ct=0;ct<7;ct+=0.25){window.__lrrShow(i,side,ct,'board');
                const kc=document.getElementById('keychip');if(kc.classList.contains('off'))continue;
                const lab=document.querySelector('#kcRow>span:last-child');const r=kc.getBoundingClientRect(),sc=document.getElementById('screen').getBoundingClientRect();
                if(lab.scrollWidth>lab.clientWidth+1||r.left<sc.left-1||r.right>sc.right+1)out.push(i+side+ct+':'+lab.textContent+' '+lab.scrollWidth+'/'+lab.clientWidth);
                if(r.height>sc.height*0.45)out.push('tall chip '+i+':'+r.height);}}}
              return [...new Set(out)].slice(0,12);}""")
            check(not bad, f'{w}/{game} key chip: {bad}')
            check(not errs, f'{w}/{game} errors: '+json.dumps(errs[:3]))
            ctx.close()
    b.close()
print('FAILS',len(fails))
for f in fails: print(' -',f)
