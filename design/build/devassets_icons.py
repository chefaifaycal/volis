import sys; sys.path.insert(0, '/workspace/maquettes-v4/build')
from common import P
import re
src = open('/workspace/volis-design/build/devassets.py').read()
EXTRA = eval(re.search(r"EXTRA = (\{.*?\n\})", src, re.S).group(1))
NAMES = eval(re.search(r"NAMES = (\{.*?\})\n", src, re.S).group(1))
ALLI = {NAMES.get(k, k): v for k, v in {**P, **EXTRA}.items()}
