#!/bin/bash
cd /workspace/volis-design/build
for f in "$@"; do b=$(basename $f .html)
  google-chrome --headless --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --window-size=393,852 --virtual-time-budget=1500 --screenshot=/workspace/volis-design/ecrans/$b.png file://$PWD/html/$b.html >/dev/null 2>&1 &
  while [ $(jobs -r | wc -l) -ge 6 ]; do sleep .2; done
done; wait
