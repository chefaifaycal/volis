import json, re, sys, html
sys.path.insert(0, '.')
from content import PHASES, UI, DEV, LEG, YOU
F = '/workspace/logos/final/'
logo = open(F + '01-logo-principal/svg/volis-logo-couleur-fond-creme.svg').read()
logo = logo.replace('viewBox="-12.0 -140.0 286.4 156.0"', 'viewBox="-4 -116 266 122" role="img" aria-label="Volis" width="132" height="60"')
logo = logo.replace('id="k1"', 'id="lg-k1"').replace('url(#k1)', 'url(#lg-k1)').replace('id="k2"', 'id="lg-k2"').replace('url(#k2)', 'url(#lg-k2)')
assert 'k1' not in logo.replace('lg-k1', '') and 'k2' not in logo.replace('lg-k2', '')
fav = open(F + '03-icone-app/favicon/favicon.svg').read()
import urllib.parse
favuri = 'data:image/svg+xml,' + urllib.parse.quote(fav)
BOTS = {UI: dict(k='ui', d='Design : écrans, charte, accessibilité, fiches des stores.'),
        DEV: dict(k='dev', d='Code, architecture, sécurité, CI, builds et soumissions.'),
        LEG: dict(k='leg', d='Questions juridiques, conformité, documents (pas un avis juridique).'),
        YOU: dict(k='you', d='Décisions et démarches que vous faites vous-même.')}
data = dict(phases=PHASES, bots=BOTS)
js_data = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
nsteps = sum(len(p['steps']) for p in PHASES)
tpl = open('template.html').read()
out = (tpl.replace('%%LOGO%%', logo).replace('%%FAV%%', favuri).replace('%%DATA%%', js_data)
          .replace('%%NPH%%', str(len(PHASES))).replace('%%NST%%', str(nsteps)))
open('/workspace/volis/guide/volis-guide-interactif.html', 'w').write(out)
print(len(PHASES), nsteps, len(out))
