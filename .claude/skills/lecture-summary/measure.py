import sys
from playwright.sync_api import sync_playwright
f=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1200,'height':900})
    pg.goto('file://'+__import__('os').path.abspath(f)); pg.emulate_media(media='print')
    res=pg.evaluate('''()=>[...document.querySelectorAll('.page')].map((p,i)=>{
      const r=p.getBoundingClientRect(); const pad=parseFloat(getComputedStyle(p).paddingBottom);
      const limit=r.bottom-pad; let maxb=0;
      p.querySelectorAll('.card,table,.q,h2').forEach(e=>{maxb=Math.max(maxb,e.getBoundingClientRect().bottom)});
      const cols=[...p.querySelectorAll('.col')].map(c=>{let m=0;[...c.children].forEach(e=>m=Math.max(m,e.getBoundingClientRect().bottom));return Math.round(limit-m)});
      return {page:i+1, spare:Math.round(limit-maxb), cols};
    })''')
    for r in res: print(r)
    b.close()
