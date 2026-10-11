cd /workspace/volis-design/build/charte
for f in p*.html; do b=${f%.html}
 google-chrome --headless --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --window-size=1600,1000 --virtual-time-budget=2000 --screenshot=/workspace/volis-design/charte/volis-charte-$b.png file://$PWD/$f >/dev/null 2>&1 &
 while [ $(jobs -r | wc -l) -ge 6 ]; do sleep .2; done
done; wait
google-chrome --headless --no-sandbox --disable-gpu --virtual-time-budget=4000 --no-pdf-header-footer --print-to-pdf=/workspace/volis-design/volis-charte-graphique.pdf file://$PWD/all.html >/dev/null 2>&1
