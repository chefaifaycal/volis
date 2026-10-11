import sys, os, glob
sys.path.insert(0, '/workspace/maquettes-v4/build')
from PIL import Image, ImageDraw, ImageFilter
from board import font, J, IN
from flows import FLOWS, LABEL
E = '/workspace/volis-design/ecrans'
files = {os.path.basename(f)[:2]: f for f in glob.glob(E + '/*.png')}
wm = Image.open('/workspace/logos/final/01-logo-principal/png-4000px-transparent/volis-logo-couleur-fond-creme.png')
wm = wm.resize((int(wm.width*120/wm.height), 120), Image.LANCZOS)
def board(code, title, ids, out):
    cols = min(len(ids), 6) if len(ids) != 9 else 5
    if len(ids) == 11: cols = 6
    sw, sh = 590, 1278; gap = 60; pad = 90; top = 280; lab = 120
    rows = (len(ids)+cols-1)//cols
    W = pad*2+cols*sw+(cols-1)*gap; H = top+rows*(sh+lab+30)+40
    b = Image.new('RGB', (W, H), '#EAE3D3'); d = ImageDraw.Draw(b)
    b.paste(wm, (pad-16, 50), wm)
    d.text((pad+wm.width+20, 58), f'Parcours {code} · {title}', font=font(J, 66, 800), fill='#1E2A3A')
    d.text((pad+wm.width+20, 150), f'Concept 1 « Carnet de voyage » · {len(ids)} écrans · 393×852 @2x · français (Québec)', font=font(IN, 32, 500), fill='#4E5A69')
    for i, k in enumerate(ids):
        r, c = divmod(i, cols); x = pad+c*(sw+gap); y = top+r*(sh+lab+30)
        im = Image.open(files[k]).convert('RGB').resize((sw, sh), Image.LANCZOS)
        m = Image.new('L', (sw, sh), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, sw-1, sh-1), radius=64, fill=255)
        s_ = Image.new('L', (sw+120, sh+120), 0); ImageDraw.Draw(s_).rounded_rectangle((60, 70, sw+60, sh+70), radius=64, fill=80)
        s_ = s_.filter(ImageFilter.GaussianBlur(22)); b.paste(Image.new('RGB', s_.size, '#000'), (x-60, y-60), s_)
        b.paste(im, (x, y), m)
        d.text((x+8, y+sh+30), f'{k}. {LABEL[k]}', font=font(IN, 32, 600), fill='#1E2A3A')
    b.save(out, optimize=True); print(out, b.size, os.path.getsize(out)//1024, 'KB')
slug = lambda s: s.lower().replace('’', '').replace(' ', '-').replace(',', '').replace('(', '').replace(')', '').replace('é', 'e').replace('è', 'e').replace('ô', 'o')
for code, title, ids in FLOWS:
    board(code, title, ids, f'/workspace/volis-design/boards/parcours-{code}-{slug(title)}.png')
# PDF léger : tous les écrans
ims = [Image.open(files[k]).convert('RGB') for k in sorted(files)]
out = '/workspace/volis-design/volis-ecrans-concept1.pdf'
ims[0].save(out, 'PDF', save_all=True, append_images=ims[1:], resolution=144, quality=85)
print(out, len(ims), round(os.path.getsize(out)/1e6, 2), 'MB')
