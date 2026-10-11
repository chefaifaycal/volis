import sys
from PIL import Image
fs=sys.argv[2:]; out=sys.argv[1]
ims=[Image.open(f'/workspace/volis-design/ecrans/{f}.png') for f in fs]
W=sum(i.width for i in ims)+20*(len(ims)-1); b=Image.new('RGB',(W,ims[0].height),'#888')
x=0
for i in ims: b.paste(i,(x,0)); x+=i.width+20
b.save(out)
