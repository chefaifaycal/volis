import sys, os, base64
from kit import *
from tokens import *
import tokens as TK
LG = '/workspace/logos/final'
WMS = open(f'{LG}/01-logo-principal/svg/volis-logo-couleur-fond-creme.svg').read()
def img(p, style=''): return f'<img src="file://{p}" style="{style}"/>'
PW, PH = 1600, 1000
BASE = CSS.replace('html,body{width:393px;height:852px;overflow:hidden;background:transparent}', '').replace('GRAIN', GRAIN)
PCSS = BASE + f"""
html,body{{margin:0;padding:0;background:{CREAM}}}
@page{{size:{PW}px {PH}px;margin:0}}
.pg{{width:{PW}px;height:{PH}px;position:relative;overflow:hidden;background:{CREAM};font-family:Inter;color:{INK};page-break-after:always;break-after:page;-webkit-font-smoothing:antialiased}}
.pg .grain{{opacity:.10;mix-blend-mode:multiply}}
.pin{{position:absolute;inset:0;padding:72px 80px 70px;display:flex;flex-direction:column}}
.kick{{font:700 15px/20px 'JetBrains Mono';letter-spacing:2px;color:{TEAL};text-transform:uppercase}}
.ptitle{{font:800 46px/54px 'Plus Jakarta Sans';letter-spacing:-1px;margin-top:6px}}
.plead{{font:400 19px/28px Inter;color:{T2};margin-top:8px;max-width:1100px}}
.foot{{position:absolute;left:80px;right:80px;bottom:28px;display:flex;justify-content:space-between;align-items:center;font:500 13px/18px Inter;color:{T2}}}
.g{{display:grid;gap:24px}}
.box2{{background:{CARD};border:1.5px solid {LINE};border-radius:20px;padding:22px}}
.bt{{font:800 20px/26px 'Plus Jakarta Sans'}}
.cap{{font:500 14px/20px Inter;color:{T2}}}
.mono{{font-family:'JetBrains Mono'}}
table.t{{border-collapse:collapse;width:100%;font:500 14px/20px Inter}}
table.t th{{text-align:left;font:700 13px/18px Inter;color:{T2};padding:8px 10px;border-bottom:2px solid {LINE}}}
table.tc td{{padding:3px 10px!important}} table.ty td{{padding:2px 8px!important}}
table.t td{{padding:7px 10px;border-bottom:1px solid {LINE};vertical-align:middle}}
ul.l{{margin:0;padding-left:20px;font:400 16px/25px Inter}} ul.l li{{margin:3px 0}}
.do{{border-top:6px solid {SUCC_FG}}} .dont{{border-top:6px solid {ERR}}}
"""
PAGES = []
def P(title, kick, lead, inner, dark=False):
    n = len(PAGES)+1
    PAGES.append((title, f'<section class="pg"{" style=background:#121A24;color:#F3EEE4" if dark else ""}><div class="grain"></div><div class="pin"><div class="kick">{kick}</div><div class="ptitle">{title}</div>'
                  + (f'<div class="plead">{lead}</div>' if lead else '') + f'<div style="flex:1;min-height:0;margin-top:28px;position:relative">{inner}</div></div>'
                  f'<div class="foot"><span style="display:flex;align-items:center;gap:12px">{wordmark(22)}<span>Charte graphique · v1 · octobre 2026</span></span><span class="mono">{n:02d}</span></div></section>'))
# 1 Couverture
cover = (f'<section class="pg" style="background:{CREAM}"><div class="grain"></div>'
         f'<div class="abs" style="left:0;top:0">{blobsvg(1600,1000,[(5,1250,380,330,"#BFE3DB",.6),(9,1380,760,210,"#FFC4B2",.55)])}</div>'
         f'<div class="abs" style="left:110px;top:150px">{wordmark(150)}</div>'
         f'<div class="abs" style="left:116px;top:390px;font:800 64px/72px \'Plus Jakarta Sans\';letter-spacing:-1.5px;max-width:800px">Charte graphique<br>et système de design</div>'
         f'<div class="abs" style="left:118px;top:560px;font:400 22px/32px Inter;color:{T2};max-width:720px">Concept « Carnet de voyage » — application mobile (iOS, Android) et web. Couleurs, typographie, composants, illustration, accessibilité et ton.</div>'
         f'<div class="abs" style="left:118px;top:700px;display:flex;gap:10px">{status("v1 · octobre 2026", "teal", False)}{status("Français (Québec)", "mute", False)}{status("Expo / React Native + web", "sand", False)}</div>'
         f'<img src="{ill("a-voyageur")}" class="abs" style="right:140px;top:160px;height:640px"/>'
         f'<div class="abs" style="right:118px;bottom:40px;font:600 30px/30px Caveat;color:{TEAL};transform:rotate(-3deg)">vos colis voyagent avec des voyageurs vérifiés</div></section>')
PAGES.append(('Couverture', cover))
# 2 Principes + sommaire
prin = [('Confiance d’abord', 'Chaque écran rappelle ce qui protège l’utilisateur : identité vérifiée, séquestre, preuves de remise. Jamais caché, jamais alarmiste.'),
        ('Chaleureux, pas enfantin', 'Le crayonné et le papier donnent de la chaleur; les grilles, les marges et la typographie restent nettes et professionnelles.'),
        ('Clair à chaque étape', 'Une action principale par écran, des statuts explicites, des montants toujours détaillés.'),
        ('Accessible par défaut', 'Contraste AA, cibles de 44 pt, tailles dynamiques, texte d’abord : la couleur ne porte jamais seule le sens.')]
toc_items = ['Logo', 'Couleurs', 'Sémantique et mode sombre', 'Contrastes', 'Typographie', 'Espacement, grille, rayons, élévation', 'Iconographie', 'Illustration', 'Composants (3 pages)', 'Mouvement', 'Accessibilité', 'Voix et ton', 'À faire / à éviter']
inner = (f'<div class="g" style="grid-template-columns:1.3fr 1fr;gap:40px;height:100%"><div class="g" style="grid-template-columns:1fr 1fr;align-content:start">'
         + ''.join(f'<div class="box2" style="min-height:220px"><div class="mono" style="font:700 14px/18px \'JetBrains Mono\';color:{CORAL}">0{i+1}</div><div class="bt" style="margin-top:8px">{t}</div><div style="font:400 16px/24px Inter;color:{T2};margin-top:8px">{d}</div></div>' for i, (t, d) in enumerate(prin))
         + f'</div><div class="box2"><div class="bt">Sommaire</div><ol style="margin:14px 0 0;padding-left:22px;font:500 17px/34px Inter">' + ''.join(f'<li>{t}</li>' for t in toc_items) + '</ol></div></div>')
P('Principes', 'Introduction', 'Volis met en relation des expéditeurs et des voyageurs vérifiés qui transportent des colis dans leurs bagages. Le design doit inspirer la confiance d’un service financier avec la chaleur d’un carnet de voyage.', inner)
# 3 Logo
LP = f'{LG}/01-logo-principal/apercus-avec-fond'
logo_inner = (f'<div class="g" style="grid-template-columns:1.25fr 1fr;gap:28px;height:100%">'
              f'<div class="g" style="grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:16px">'
              + ''.join(f'<div style="border-radius:18px;overflow:hidden;position:relative;border:1.5px solid {LINE}">{img(f"{LP}/{f}", "width:100%;height:100%;object-fit:contain;display:block;background:"+bgc)}<span class="badge abs" style="left:10px;bottom:10px;background:{CARD};color:{INK}">{l}</span></div>'
                        for f, l, bgc in [('volis-logo-couleur-fond-creme-apercu.png', 'Couleur · fond crème (principal)', CREAM), ('volis-logo-fond-encre-apercu.png', 'Fond encre', INK), ('volis-logo-fond-sarcelle-apercu.png', 'Fond sarcelle', TEAL), ('volis-logo-mono-noir-apercu.png', 'Mono noir', '#FFFFFF')])
              + '</div><div class="col" style="gap:16px">'
              f'<div class="box2"><div class="bt">Zone de protection</div><div style="display:flex;align-items:center;gap:22px;margin-top:12px"><div style="position:relative;padding:34px;border:2px dashed {CORAL};border-radius:8px">{wordmark(60)}<span class="abs mono" style="left:6px;top:6px;font-size:13px;color:{CORAL};font-weight:700">x</span></div>'
              f'<span class="cap" style="flex:1">x = diamètre de la pastille corail. Laisser au moins x tout autour du logo.</span></div></div>'
              f'<div class="box2"><div class="bt">Tailles minimales</div><div class="row" style="gap:28px;margin-top:12px;align-items:flex-end"><div class="col" style="gap:6px">{wordmark(30)}<span class="cap">Logo : 100 px / 25 mm</span></div>'
              f'<div class="col" style="gap:6px">{symbol(28)}<span class="cap">Symbole : 24 px / 7 mm</span></div><div class="col" style="gap:6px">{appicon(44)}<span class="cap">Icône : système</span></div></div></div>'
              f'<div class="box2"><div class="bt">Où utiliser quoi</div><ul class="l" style="margin-top:8px;font-size:15px;line-height:23px"><li><b>Mot-symbole « Colis caché »</b> : splash, en-tête Accueil, site, documents.</li><li><b>Symbole</b> (o-colis + pastille) : avatar réseaux, tampons, en-têtes compacts.</li><li><b>Icône « Signature »</b> : écran d’accueil iOS/Android, favicon, notifications, Live Activity.</li><li>Fichiers : <span class="mono" style="font-size:13px">dev-assets/logos/</span> et <span class="mono" style="font-size:13px">app-icons/</span>.</li></ul></div></div></div>')
P('Logo', '01 · Identité', 'Le logo principal est le mot-symbole « Colis caché » : le o est un colis vu en 3D, le point du i est une pastille corail avec un avion découpé. L’icône d’appli reste « Signature ».', logo_inner)
# 4 Couleurs
def sw(name, hexv, role, tok, txt=None, big=False):
    tc = txt or ('#FFFFFF' if lum(hexv) < .25 else INK)
    return (f'<div style="border-radius:18px;overflow:hidden;border:1.5px solid {LINE};background:{CARD};display:flex;flex-direction:column">'
            f'<div style="height:{170 if big else 110}px;background:{hexv};padding:14px;color:{tc};font:800 {22 if big else 17}px/24px \'Plus Jakarta Sans\'">{name}</div>'
            f'<div style="padding:10px 14px"><div class="mono" style="font:700 15px/20px \'JetBrains Mono\'">{hexv}</div><div class="cap" style="font-size:13px">{role}</div><div class="mono" style="font:500 12px/16px \'JetBrains Mono\';color:{TEAL};margin-top:2px">{tok}</div></div></div>')
cols = (f'<div class="g" style="grid-template-columns:repeat(4,1fr);gap:16px">'
        + sw('Sarcelle', '#0F766E', 'Primaire : actions, liens, états actifs', 'color.primary', None, True)
        + sw('Encre', '#1E2A3A', 'Secondaire : texte, boutons Apple Pay, surfaces inversées', 'color.text / secondary', None, True)
        + sw('Crème', '#F5F1E8', 'Fond d’écran (papier)', 'color.bg', None, True)
        + sw('Corail', '#FF7A59', 'Accent décoratif. Texte encre dessus, jamais blanc', 'color.accent', INK, True)
        + '</div><div class="g" style="grid-template-columns:repeat(7,1fr);gap:12px;margin-top:16px">'
        + sw('Papier', '#FFFDF8', 'Surfaces, cartes', 'surface') + sw('Ardoise', '#4E5A69', 'Texte secondaire', 'textSecondary') + sw('Sarcelle claire', '#D6ECE8', 'Sélection, badges', 'primarySubtle')
        + sw('Menthe', '#DCEFEA', 'Bandeaux confiance', 'mint') + sw('Pêche', '#FFE1D6', 'Cartes d’entrée', 'accentSubtle') + sw('Sable', '#FFE9C7', 'Mise en avant douce', 'sand') + sw('Lin', '#E4DACA', 'Bordures de carte', 'borderSubtle')
        + '</div>'
        + f'<div class="row" style="gap:16px;margin-top:18px"><div style="flex:1;height:26px;border-radius:13px;overflow:hidden;display:flex"><i style="flex:60;background:{CREAM};border:1.5px solid {LINE}"></i><i style="flex:20;background:#FFFDF8"></i><i style="flex:10;background:{TEAL}"></i><i style="flex:7;background:{INK}"></i><i style="flex:3;background:{CORAL}"></i></div>'
        f'<span class="cap">Proportions visées : 60 % crème · 20 % papier · 10 % sarcelle · 7 % encre · 3 % corail</span></div>')
P('Couleurs de marque', '02 · Couleurs', 'Une couleur dominante (sarcelle) et un accent vif (corail) sur papier crème. Le corail est décoratif : souligné, pastille, point de notification. Il ne porte jamais de texte blanc.', cols)
# 5 Sémantique + sombre
sem = [('Succès', 'success', 'successText', 'successBg'), ('Avertissement', 'warning', 'warningText', 'warningBg'), ('Erreur', 'error', 'errorText', 'errorBg'), ('Info', 'info', 'infoText', 'infoBg')]
def semcard(T, dark=False):
    out = ''
    for n, k, kt, kb in sem:
        out += (f'<div style="border-radius:14px;padding:12px 14px;background:{T[kb]};display:flex;gap:12px;align-items:center">'
                f'<span style="width:34px;height:34px;border-radius:17px;background:{T[k]};flex:none"></span><div class="col"><b style="font:700 16px/20px Inter;color:{T[kt]}">{n}</b>'
                f'<span class="mono" style="font:600 12px/16px \'JetBrains Mono\';color:{T[kt]}">{T[k]} · texte {T[kt]} · fond {T[kb]}</span></div></div>')
    return out
def mini(T, dark):
    return (f'<div style="border-radius:24px;padding:20px;background:{T["bg"]};border:1.5px solid {T["borderSubtle"]};display:flex;flex-direction:column;gap:12px">'
            f'<div style="font:800 22px/28px \'Plus Jakarta Sans\';color:{T["text"]}">{"Mode sombre" if dark else "Mode clair"}</div>'
            f'<div style="border-radius:18px;padding:14px;background:{T["surface"]};border:1.5px solid {T["borderSubtle"]}"><div style="font:700 16px/20px Inter;color:{T["text"]}">Karim B. · 4,9</div><div style="font:400 14px/20px Inter;color:{T["textSecondary"]}">YUL → ALG · 14 nov. · 5 kg dispo</div>'
            f'<div class="row" style="gap:8px;margin-top:10px"><span class="badge" style="background:{T["primarySubtle"]};color:{T["text"] if dark else "#0B5B55"}">ID vérifiée</span><span class="badge" style="background:{T["accentSubtle"]};color:{T["text"]}">Meilleur choix</span></div></div>'
            f'<div style="height:52px;border-radius:26px;background:{T["primary"]};color:{T["onPrimary"]};font:700 16px/52px Inter;text-align:center">Demander l’envoi</div>'
            + semcard(T, dark) + '</div>')
P('Couleurs sémantiques et mode sombre', '02 · Couleurs', 'Chaque état a trois valeurs : couleur pleine (icône, bordure), texte et fond. En mode sombre, la sarcelle s’éclaircit (#3FB8AC) et le texte sur bouton primaire devient foncé.',
  f'<div class="g" style="grid-template-columns:1fr 1fr;gap:28px">{mini(LIGHT, False)}{mini(DARK, True)}</div>')
# 6 Contrastes
def rowc(a, b):
    out = ''
    for T in (LIGHT, DARK):
        r = contrast(T[a], T[b]); ok = 'AAA' if r >= 7 else ('AA' if r >= 4.5 else ('AA grand / UI' if r >= 3 else 'Échec'))
        kind = 'ok' if r >= 4.5 else ('warn' if r >= 3 else 'err')
        out += f'<td><span style="display:inline-flex;align-items:center;gap:8px"><span style="display:inline-block;padding:3px 10px;border-radius:8px;background:{T[b]};color:{T[a]};font:700 14px/20px Inter;border:1px solid {LINE}">Aa</span><b class="mono" style="font-size:14px">{r:.2f}</b>{status(ok, kind, False)}</span></td>'
    return f'<tr><td class="mono" style="font-size:13px">{a}</td><td class="mono" style="font-size:13px">{b}</td>{out}</tr>'
rows_ = ''.join(rowc(a, b) for a, b in PAIRS)
P('Tableau de contrastes (WCAG 2.2)', '02 · Couleurs', 'Texte courant ≥ 4,5:1 (AA), grand texte et composants d’interface ≥ 3:1. Calculé sur les valeurs des tokens. L’état désactivé est exempté, mais reste lisible.',
  f'<table class="t tc"><tr><th>Texte / avant-plan</th><th>Fond</th><th>Clair</th><th>Sombre</th></tr>{rows_}</table>')
# 7 Typographie
FAMC = {'display': "'Plus Jakarta Sans'", 'body': 'Inter', 'mono': "'JetBrains Mono'", 'hand': 'Caveat'}
SAMPLE = {'display': '145,00 $', 'h1': 'Bonjour, Camille!', 'h2': 'Paiement protégé', 'h3': 'Suivi du colis', 'title': 'Envoi en cours', 'bodyLg': 'camille.t@exemple.com', 'body': 'Votre paiement reste en séquestre jusqu’à la remise.',
          'bodySm': 'Détails du vol visibles après l’acceptation', 'label': 'Valeur déclarée', 'caption': 'Prise à 17 h 58 · ajoutée au dossier', 'micro': 'ID VÉRIFIÉE', 'tab': 'Messages', 'button': 'Demander l’envoi', 'buttonSm': 'Voir le profil',
          'code': '4821', 'monoMd': 'YUL → ALG · AT 201', 'monoSm': 'VL-4821', 'hand': 'montre l’intérieur, puis ferme!'}
trow = ''.join(f'<tr><td class="mono" style="font-size:13px;color:{TEAL};width:90px">{n}</td><td style="font:{w} {s}px/{lh}px {FAMC[f]};letter-spacing:{ls}px;white-space:nowrap;max-width:560px;overflow:hidden;{"color:"+TEAL if f=="hand" else ""}">{SAMPLE[n]}</td>'
               f'<td class="mono" style="font-size:12.5px;white-space:nowrap">{s}/{lh} · {w}</td><td class="cap" style="font-size:13px">{u}</td></tr>' for n, f, s, lh, w, ls, u in TYPE)
fams = ''.join(f'<div class="box2" style="padding:14px 16px"><div style="font:{w} 30px/34px {c}">{n}</div><div class="cap">{d}</div></div>' for n, c, w, d in [
    ('Plus Jakarta Sans', "'Plus Jakarta Sans'", 800, 'Titres, montants · 700/800'), ('Inter', 'Inter', 500, 'Texte et interface · 400 à 700'), ('JetBrains Mono', "'JetBrains Mono'", 700, 'Codes, aéroports, vols, réf.'), ('Caveat', 'Caveat', 600, 'Décoratif seulement')])
P('Typographie', '03 · Typographie', 'Échelle mobile en points (pt = px @1x). Respecter le texte dynamique : prévoir jusqu’à 200 % sans troncature des informations critiques. Caveat est réservée aux annotations décoratives : jamais pour une étiquette, un bouton, un champ ou un montant.',
  f'<div class="g" style="grid-template-columns:1fr 3.2fr;gap:24px"><div class="col" style="gap:12px">{fams}</div><div style="overflow:hidden"><table class="t ty" style="font-size:13px">{trow}</table></div></div>')
# 8 Espacement etc.
spc = ''.join(f'<div class="row" style="gap:12px;height:30px"><span class="mono" style="width:40px;font-size:13px;color:{TEAL}">{k}</span><i style="width:{v*1.5}px;height:16px;background:{CORAL};border-radius:3px;opacity:.85"></i><span class="mono" style="font-size:13px">{v} pt</span></div>' for k, v in SPACE.items())
rad = ''.join(f'<div class="col" style="align-items:center;gap:6px"><div style="width:76px;height:76px;background:{TSEL};border:2px solid {TEAL};border-radius:{min(v, 38)}px"></div><span class="mono" style="font-size:13px">{k} · {v if v < 999 else "∞"}</span></div>' for k, v in RADII.items())
radu = '<div class="cap" style="margin-top:8px">xs badges/puces carrées · sm vignettes · md champs (14) · lg cartes (20) · xl feuilles (28) · pill boutons, puces, onglet actif</div>'
elev = ''.join(f'<div class="col" style="align-items:center;gap:8px;flex:1"><div style="width:120px;height:80px;background:{CARD};border-radius:16px;{"border:1.5px solid "+LINE+";" if k=="e0" else ""}box-shadow:0 {v["y"]}px {v["blur"]}px {v["spread"]}px rgba(20,28,40,{v["opacity"]})"></div><b class="mono" style="font-size:13px">{k}</b><span class="cap" style="font-size:12px;text-align:center">{v["use"]}</span></div>' for k, v in SHADOWS.items())
grid = (f'<div style="position:relative;width:170px;height:370px;border-radius:26px;background:{CREAM};border:2px solid {INK};overflow:hidden;flex:none">'
        f'<div class="abs" style="left:8px;right:8px;top:0;bottom:0;display:grid;grid-template-columns:repeat(4,1fr);gap:6px">' + ''.join(f'<i style="background:rgba(255,122,89,.18)"></i>' for _ in range(4)) + '</div>'
        f'<div class="abs" style="left:0;right:0;top:0;height:27px;background:rgba(15,118,110,.18)"></div><div class="abs" style="left:0;right:0;bottom:0;height:47px;background:rgba(15,118,110,.18)"></div>'
        f'<div class="abs" style="left:8px;right:8px;bottom:56px;height:28px;border-radius:14px;background:{TEAL}"></div></div>')
gtxt = '<ul class="l" style="font-size:15px;line-height:23px"><li>Écran de référence : 393 × 852 pt (iPhone 15/16).</li><li>Marges latérales <b>16 pt</b>; 4 colonnes, gouttière 12 pt.</li><li>Zone d’état 54 pt, indicateur d’accueil 34 pt (zones sûres).</li><li>En-tête 48 pt · barre d’onglets 60 pt · CTA 56 pt · champ 50 pt.</li><li>Cible tactile minimale <b>44 × 44 pt</b>, espacement ≥ 8 pt.</li><li>CTA principal en bas, pleine largeur, au-dessus de l’indicateur.</li></ul>'
P('Espacement, grille, rayons et élévation', '04 · Mise en page', 'Grille de 8 pt avec demi-pas de 4 pt. Les cartes sont à plat avec une bordure lin; l’ombre est réservée à ce qui flotte (feuilles, modales, éléments sur la carte).',
  f'<div class="g" style="grid-template-columns:.7fr 1.25fr 1.45fr;gap:24px;height:100%"><div class="box2"><div class="bt" style="margin-bottom:8px">Espacements</div>{spc}</div>'
  f'<div class="col" style="gap:20px"><div class="box2"><div class="bt" style="margin-bottom:12px">Rayons</div><div class="row" style="gap:14px;flex-wrap:wrap">{rad}</div>{radu}</div><div class="box2"><div class="bt" style="margin-bottom:12px">Élévation</div><div class="row" style="gap:8px;align-items:flex-start">{elev}</div></div></div>'
  f'<div class="box2"><div class="bt" style="margin-bottom:12px">Grille et marges</div><div class="row" style="gap:18px;align-items:flex-start">{grid}{gtxt}</div></div></div>')
# 9 Iconographie
from devassets_icons import ALLI
icg = ''.join(f'<div class="col" style="align-items:center;gap:6px;width:96px"><div style="width:52px;height:52px;border-radius:14px;background:{CARD};border:1.5px solid {LINE};display:flex;align-items:center;justify-content:center">'
              f'<svg width="26" height="26" viewBox="0 0 24 24" fill="{"%s" % INK if n=="star" else "none"}"><path d="{d}" stroke="{INK}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div><span class="mono" style="font-size:11px;color:{T2}">{n}</span></div>' for n, d in sorted(ALLI.items()))
rules = '<ul class="l" style="font-size:15px;line-height:23px"><li>Grille 24 px, zone utile 20 px, trait <b>2 px</b> (2,2–2,4 px à l’état actif), extrémités et angles arrondis.</li><li>Tailles : 16 (dans un badge), 20 (liste), 22 (onglets, en-tête), 24 (autonome).</li><li>Couleur : encre par défaut; sarcelle si actif ou interactif; couleur sémantique dans les bandeaux.</li><li>Toujours avec un libellé visible ou <span class="mono" style="font-size:13px">accessibilityLabel</span>.</li><li>Logos tiers (Apple, Google, Stripe) : versions officielles seulement.</li></ul>'
P('Iconographie', '05 · Icônes', f'{len(ALLI)} icônes linéaires maison dérivées d’un style Lucide, livrées en SVG (currentColor) et en composant React Native.',
  f'<div class="g" style="grid-template-columns:2.3fr 1fr;gap:24px"><div class="row" style="flex-wrap:wrap;gap:10px 4px;align-content:flex-start">{icg}</div><div class="box2">{rules}</div></div>')
# 10 Illustration
ills = ''.join(f'<div class="col" style="align-items:center;gap:6px;flex:1"><div style="height:250px;display:flex;align-items:flex-end;justify-content:center;position:relative;width:100%">'
               f'<div class="abs" style="left:50%;bottom:6px;transform:translateX(-50%);width:200px;height:200px;border-radius:46% 54% 50% 50%;background:{c};opacity:.6"></div><img src="{ill(k)}" style="height:240px;position:relative"/></div><span class="cap" style="text-align:center">{n}</span></div>'
               for k, n, c in [('a-voyageur', 'Voyageur · valise + colis', '#BFE3DB'), ('b-remise', 'Remise expéditeur → voyageur', '#FFC4B2'), ('c-reception', 'Réception · cœur', '#FFC4B2'), ('d-connexion', 'Salut · téléphone', '#BFE3DB'), ('e-inscription', 'Passeport + colis', '#FFE1B0')])
irules = ('<div class="g" style="grid-template-columns:1fr 1fr;gap:20px;margin-top:18px"><div class="box2 do"><div class="bt">Style</div><ul class="l" style="font-size:15px;line-height:23px;margin-top:6px"><li>Trait d’encre libre, légèrement imparfait; aplats limités (sarcelle, corail, sable, peau variée).</li><li>Personnages diversifiés, fictifs, souriants, en action liée au colis ou au voyage.</li><li>Posés sur une tache organique (sarcelle claire ou pêche à 50–60 %) avec grain papier.</li></ul></div>'
          '<div class="box2 dont"><div class="bt">Usage</div><ul class="l" style="font-size:15px;line-height:23px;margin-top:6px"><li>Avec parcimonie : bienvenue, états vides, succès, attente. Une illustration par écran au maximum.</li><li>Jamais sur un écran de formulaire dense, de paiement ou d’erreur bloquante.</li><li>Décoratif : <span class="mono" style="font-size:13px">accessible={false}</span>. Le message est toujours dans le texte.</li></ul></div></div>')
P('Illustration', '06 · Illustration', 'Personnages dessinés à la main, style « carnet de voyage ». Fichiers PNG transparents @1x/@2x/@3x et WebP dans dev-assets/illustrations/.', f'<div class="row" style="gap:12px">{ills}</div>{irules}')
# 11 Composants 1 : boutons + champs
def lab(t): return f'<div class="cap" style="font-size:12.5px;margin-bottom:6px">{t}</div>'
bstates = [('Primaire', 'primary', ''), ('Pressé', 'primary', f'background:{"#0B5B55"}'), ('Focus clavier', 'primary', 'box-shadow:0 0 0 3px #F5F1E8,0 0 0 6px #0F766E'), ('Chargement', 'primary', ''), ('Désactivé', 'disabled', '')]
brow = ''.join(f'<div style="flex:1">{lab(n)}{btn("Continuer" if n!="Chargement" else "<svg width=20 height=20 viewBox=\'0 0 24 24\'><circle cx=12 cy=12 r=9 stroke=\'#fff\' stroke-opacity=.35 stroke-width=3 fill=none /><path d=\'M12 3a9 9 0 0 1 9 9\' stroke=\'#fff\' stroke-width=3 fill=none stroke-linecap=round /></svg>", k, None, 52, s)}</div>' for n, k, s in bstates)
brow2 = ''.join(f'<div style="flex:1">{lab(n)}{btn(t, k, i, h)}</div>' for n, k, t, i, h in [('Secondaire', 'secondary', 'Voir le profil', None, 52), ('Tertiaire / lien', 'ghost', 'Plus tard', None, 44), ('Encre (paiement)', 'ink', 'Payer 32,06 $', None, 52), ('Destructif', 'danger', 'Supprimer', None, 52), ('Destructif secondaire', 'danger2', 'Refuser', None, 52)])
brow3 = ''.join(f'<div style="flex:1">{lab(n)}{x}</div>' for n, x in [('Compact', btn('Chercher', 'primary', 'search', 44, 'padding:0 16px')), ('Icône 44 pt', f'<div class="ibtn">{ic("back", INK)}</div>'), ('Interrupteur', f'<div class="row" style="gap:10px">{toggle(True)}{toggle(False)}</div>'), ('Radio / case', f'<div class="row" style="gap:10px">{radio(True)}{radio(False)}{box(True)}{box(False)}</div>'), ('Segmenté', seg(['Liste', 'Carte'], 0))])
fstates = [('Par défaut (vide)', field('', 'nom@courriel.ca', 'mail', True)), ('Rempli', field('', 'a.kaci@mail.ca', 'mail')), ('Focus', field('', 'a.kaci@mail.', 'mail', False, 'focus')),
           ('Erreur', field('', 'a.kaci@mail', 'mail', False, 'err', 'Vérifiez le format du courriel')), ('Valide', field('', '514 555-0123', 'phone', False, 'ok', '', ic('check', TEAL, 18, 3))), ('Désactivé', field('', 'Montréal (YUL)', 'pin').replace('class="inp" style="', 'class="inp" style="background:#EFE8DA;border-color:#CFC6B4;color:#6F6A60;'))]
frow = ''.join(f'<div style="flex:1;min-width:0">{lab(n)}{x}</div>' for n, x in fstates)
P('Composants · boutons et champs', '07 · Composants', 'Un seul bouton primaire par écran. Libellés verbaux et précis (« Payer 32,06 $ », pas « OK »). Les champs gardent leur étiquette visible au-dessus; l’erreur combine couleur, icône et texte.',
  f'<div class="col" style="gap:20px;zoom:1.12"><div class="box2"><div class="bt" style="margin-bottom:12px">Boutons · états</div><div class="row" style="gap:14px">{brow}</div><div class="row" style="gap:14px;margin-top:14px">{brow2}</div><div class="row" style="gap:14px;margin-top:14px;align-items:flex-end">{brow3}</div></div>'
  f'<div class="box2"><div class="bt" style="margin-bottom:6px">Champs · états</div><div class="cap" style="margin-bottom:10px">Hauteur 50 pt, rayon 14, bordure taupe #7E7A70 (3:1), focus sarcelle 2 px + halo 4 px, texte 16 pt pour éviter le zoom iOS.</div><div class="row" style="gap:12px;align-items:flex-start">{frow}</div></div></div>')
# 12 Composants 2 : puces, cartes, badges, frise, tab bar
import screens as S
chips = f'<div class="row" style="gap:8px;flex-wrap:wrap">{chip("Vêtements", True)}{chip("Cadeau")}{chip("Filtres · 2", True, "sliders")}{chip("Date ± 3 j")}{chip("Désactivé").replace("class=\"chip\" style=\"", "class=\"chip\" style=\"opacity:.45;")}</div>'
badges = f'<div class="row" style="gap:8px;flex-wrap:wrap">{vbadge("mail")}{vbadge("tel")}{vbadge("id")}{vbadge("vol")}<span class="badge" style="background:{TEAL};color:#fff">{ic("shield", "#fff", 13, 2.4)}Confiance 4/4</span></div><div class="row" style="gap:8px;flex-wrap:wrap;margin-top:10px">{status("Embarqué", "teal")}{status("En attente", "warn")}{status("Livré", "ok")}{status("Annulé", "err")}{status("Brouillon", "mute")}{status("En séquestre", "teal")}</div>'
tcard = card(f'<div class="row" style="gap:12px;align-items:flex-start">{avatar("KB", 46)}<div class="col" style="flex:1;gap:4px"><div class="row" style="gap:6px"><span class="b15" style="font:700 16px/20px Inter">Karim B.</span><span class="row" style="gap:3px;font:600 13px/18px Inter">{star(CORAL, 13)}4,9 <span class="t2" style="font-weight:500">(38 avis)</span></span></div><div class="row" style="gap:6px">{vbadge("id")}{vbadge("vol")}</div></div><div class="col" style="align-items:flex-end"><span style="font:800 21px/24px \'Plus Jakarta Sans\'">31 $</span><span class="xs" style="font-weight:500">pour 2 kg</span></div></div>', 'padding:14px')
steps = [('Remis au voyageur', '14 nov. · 06 h 10', 'done'), ('Embarqué', '14 nov. · 07 h 52', 'cur'), ('Atterri', 'Prévu 21 h 40', 'todo')]
tl = ''
for i, (n, ts, s) in enumerate(steps):
    if s == 'done': dot = f'<span style="width:24px;height:24px;border-radius:12px;background:{TEAL};display:flex;align-items:center;justify-content:center;flex:none">{ic("check", "#fff", 14, 3)}</span>'
    elif s == 'cur': dot = f'<span style="width:24px;height:24px;border-radius:12px;background:{CORAL};border:2px solid {INK};display:flex;align-items:center;justify-content:center;flex:none;box-shadow:0 0 0 5px rgba(255,122,89,.28)">{ic("plane", INK, 13, 2.2)}</span>'
    else: dot = f'<span style="width:24px;height:24px;border-radius:12px;background:{CARD};border:2px solid #B9B09E;flex:none"></span>'
    line = '' if i == 2 else f'<i style="position:absolute;left:11px;top:26px;bottom:-2px;width:2px;background:{TEAL if s=="done" else "#D4CAB7"}"></i>'
    tl += f'<div class="row" style="gap:12px;align-items:flex-start;position:relative;height:52px">{line}{dot}<div class="col" style="flex:1;{"background:#FFE9E1;border-radius:12px;padding:6px 10px;margin:-6px 0 0 -4px;" if s=="cur" else ""}"><span style="font:{"800" if s=="cur" else "700"} 15px/20px Inter;color:{INK if s!="todo" else T2}">{n}</span><span class="xs" style="font-weight:500">{ts}</span></div></div>'
tabb = f'<div style="width:393px;border-radius:0 0 18px 18px;overflow:hidden;border:1.5px solid {LINE}">{tabbar(1, False)}</div>'
P('Composants · puces, cartes, badges, frise, onglets', '07 · Composants', 'Les badges de vérification utilisent toujours icône + texte. La frise de suivi met en avant l’étape en cours (corail + halo + « En cours »).',
  f'<div class="g" style="grid-template-columns:1fr 1fr;gap:20px"><div class="col" style="gap:20px"><div class="box2"><div class="bt" style="margin-bottom:10px">Puces (filtre, choix)</div>{chips}<div class="cap" style="margin-top:8px">Hauteur 40–44 pt · sélection = fond sarcelle claire + bordure sarcelle 2 px (pas seulement la couleur).</div></div>'
  f'<div class="box2"><div class="bt" style="margin-bottom:10px">Badges vérifiés et statuts</div>{badges}</div><div class="box2"><div class="bt" style="margin-bottom:10px">Barre d’onglets</div>{tabb}<div class="cap" style="margin-top:8px">5 onglets fixes · actif = pilule sarcelle claire + libellé gras sarcelle + <span class="mono" style="font-size:12px">aria-current</span> · pastille corail = non lu.</div></div></div>'
  f'<div class="col" style="gap:20px"><div class="box2" style="background:{CREAM}"><div class="bt" style="margin-bottom:10px">Carte voyageur</div>{tcard}</div><div class="box2"><div class="bt" style="margin-bottom:14px">Frise de suivi</div>{tl}</div></div></div>')
# 13 Composants 3 : bottom sheet, toast, état vide, modale
toast_ok = f'<div class="row" style="gap:10px;padding:12px 16px;border-radius:16px;background:{INK};color:#fff;box-shadow:0 20px 50px rgba(20,28,40,.35)">{ic("check", "#9FE3D8", 20, 2.6)}<span style="font:600 15px/20px Inter;flex:1">Lien de suivi copié</span><span style="font:700 14px/18px Inter;color:#9FE3D8">Annuler</span></div>'
toast_err = f'<div class="row" style="gap:10px;padding:12px 16px;border-radius:16px;background:{ERR_BG};border:1.5px solid #F2A79E;color:{ERR_FG}">{ic("alert", ERR, 20, 2.2)}<span style="font:600 15px/20px Inter;flex:1">Paiement refusé par la banque</span><span style="font:700 14px/18px Inter">Réessayer</span></div>'
toast_off = f'<div class="row" style="gap:10px;padding:12px 16px;border-radius:16px;background:{SAND};border:1.5px solid {WARN_BD}">{ic("info", WARN_IC, 20, 2.2)}<span style="font:600 15px/20px Inter;flex:1;color:{WARN_FG}">Hors ligne · on réessaie automatiquement</span></div>'
sheet_m = (f'<div style="width:300px;height:330px;border-radius:24px;background:#8C8A86;position:relative;overflow:hidden;flex:none"><div class="abs" style="left:0;right:0;bottom:0;height:240px;background:{CARD};border-radius:22px 22px 0 0;padding:8px 16px">'
           f'<div style="width:40px;height:5px;border-radius:3px;background:#B9B09E;margin:0 auto 10px"></div><div class="row" style="justify-content:space-between"><span class="h2">Filtres</span><span class="link" style="font-size:14px;min-height:0">Réinitialiser</span></div>'
           f'<div class="row" style="gap:6px;margin-top:10px">{chip("Recommandés", True)}{chip("Prix")}</div><div style="margin-top:12px">{seg(["Exacte", "± 3 j", "± 7 j"], 1)}</div><div style="margin-top:14px">{btn("Afficher 8 voyageurs", "primary", None, 48)}</div></div></div>')
empty = (f'<div class="col" style="align-items:center;text-align:center;gap:6px;width:300px"><img src="{ill("a-voyageur")}" style="height:150px"/><span class="h2">Aucun voyageur pour l’instant</span><span class="cap">Expliquez pourquoi, puis proposez une action utile.</span>{btn("Créer l’alerte", "primary", "bell", 48, "width:100%;margin-top:6px")}</div>')
modal = (f'<div style="width:300px;border-radius:24px;background:{CARD};padding:18px;box-shadow:0 20px 50px rgba(20,28,40,.35);display:flex;flex-direction:column;gap:8px">'
         f'<div style="width:44px;height:44px;border-radius:22px;background:{ERR_BG};display:flex;align-items:center;justify-content:center;align-self:center">{ic("alert", ERR, 22, 2.2)}</div><div class="h2" style="text-align:center">Supprimer définitivement?</div><div class="cap" style="text-align:center">Action irréversible.</div>{btn("Supprimer", "danger", None, 46)}{btn("Annuler", "secondary", None, 44)}</div>')
P('Composants · feuilles, notifications, états vides, modales', '07 · Composants', 'Feuille modale : poignée, titre, action de réinitialisation, CTA avec résultat chiffré, fond assombri (scrim 45 %). Toast : 4 s, au-dessus de la barre d’onglets, une action au maximum, annoncé aux lecteurs d’écran.',
  f'<div class="row" style="gap:28px;align-items:flex-start;justify-content:space-between"><div class="col" style="gap:8px"><div class="bt">Bottom sheet</div>{sheet_m}</div>'
  f'<div class="col" style="gap:14px;width:420px"><div class="bt">Toasts</div>{toast_ok}{toast_err}{toast_off}<div class="bt" style="margin-top:14px">Bandeaux</div>{banner("teal", "Votre argent est protégé", "32,06 $ restent en séquestre.")}{banner("warn", "Ne payez jamais en dehors de l’appli.", "")}</div>'
  f'<div class="col" style="gap:8px"><div class="bt">État vide</div>{empty}</div><div class="col" style="gap:8px"><div class="bt">Modale</div>{modal}</div></div>')
# 14 Mouvement
mot = [('Rapide · 150 ms', 'Retours tactiles, interrupteurs, puces, apparition d’icônes'), ('Base · 250 ms', 'Transitions d’écran, ouverture de feuille, toasts'), ('Lent · 400 ms', 'Succès (coche qui se dessine), avion qui avance sur la frise'),
       ('Courbe standard', 'cubic-bezier(0.2, 0, 0, 1) · sortie : (0.3, 0, 1, 1) · ressort RN : amortissement 18, rigidité 220')]
mrules = '<ul class="l" style="font-size:16px;line-height:26px"><li><b>Le mouvement explique</b> : l’avion avance sur la ligne pointillée quand le colis change d’étape; la coche se dessine quand c’est validé.</li><li><b>Jamais bloquant</b> : aucune animation &gt; 400 ms avant de pouvoir agir.</li><li><b>Respecter « Réduire les animations »</b> : remplacer les déplacements par des fondus ou rien (<span class="mono" style="font-size:14px">AccessibilityInfo.isReduceMotionEnabled</span>).</li><li><b>Retour haptique</b> léger sur succès (remise confirmée, paiement) et avertissement sur erreur.</li><li>Pas de clignotement &gt; 3 fois/s, pas de parallaxe décorative.</li><li>Les illustrations restent statiques; seule une petite bulle (cœur, étincelle) peut apparaître.</li></ul>'
curve = f'<svg width="260" height="200" viewBox="0 0 260 200"><rect x="1" y="1" width="258" height="198" rx="16" fill="{CARD}" stroke="{LINE}" stroke-width="1.5"/><path d="M30 170 C 76 170, 30 30, 230 30" stroke="{TEAL}" stroke-width="4" fill="none"/><path d="M30 170 L230 30" stroke="#CFC6B4" stroke-width="1.5" stroke-dasharray="4 5"/><circle cx="30" cy="170" r="6" fill="{INK}"/><circle cx="230" cy="30" r="6" fill="{CORAL}"/><text x="40" y="190" font-family="JetBrains Mono" font-size="12" fill="{T2}">temps →</text></svg>'
P('Mouvement', '08 · Mouvement', 'Calme, utile, rapide. Le mouvement confirme une action ou montre la progression du colis; il n’est jamais décoratif ni nécessaire pour comprendre.',
  f'<div class="g" style="grid-template-columns:1fr 1.2fr;gap:28px"><div class="col" style="gap:14px">' + ''.join(f'<div class="box2" style="padding:16px 18px"><div class="bt" style="font-size:18px">{t}</div><div class="cap">{d}</div></div>' for t, d in mot) + f'<div>{curve}</div></div><div class="box2">{mrules}</div></div>')
# 15 Accessibilité
acc = [('Contraste', 'AA minimum : texte 4,5:1, grand texte et composants 3:1. Le corail ne porte jamais de texte blanc.'), ('Cibles', '44 × 44 pt minimum, 8 pt d’écart. Les icônes de 20 pt sont dans un bouton de 44.'),
       ('Texte dynamique', 'Polices évolutives (allowFontScaling) jusqu’à 200 %. Aucune hauteur fixe sur du texte; les montants et codes ne sont jamais tronqués.'), ('Lecteurs d’écran', 'VoiceOver/TalkBack : libellés en français (« Code de remise : 4, 8, 2, 1 »), rôles (button, tab, checkbox), états (sélectionné, désactivé).'),
       ('Pas que la couleur', 'Statuts = couleur + icône + texte. Erreurs de champ = bordure + icône + message.'), ('Focus et ordre', 'Ordre logique de haut en bas; focus visible 2 px sarcelle + halo sur web et clavier externe.'),
       ('Mouvement', 'Respecter « Réduire les animations »; aucune information transmise seulement par animation.'), ('Formulaires', 'Étiquettes visibles, types de clavier adaptés (email, phone, number), saisie automatique (oneTimeCode, email), erreurs annoncées.'),
       ('Temps', 'Minuteries visibles (renvoi du code, expiration d’une demande) et prolongeables; aucune action irréversible sans confirmation.'), ('Langue', 'Langue déclarée (fr-CA / en-CA); prévoir l’arabe RTL : utiliser start/end, pas left/right; icônes directionnelles miroir.')]
P('Accessibilité', '09 · Accessibilité', 'Objectif WCAG 2.2 niveau AA et lignes directrices Apple/Android. Ce sont des règles de conception, à vérifier aussi en test réel (VoiceOver, TalkBack, texte 200 %).',
  '<div class="g" style="grid-template-columns:1fr 1fr;gap:14px 20px">' + ''.join(f'<div class="row" style="gap:14px;align-items:flex-start;padding:12px 16px;background:{CARD};border:1.5px solid {LINE};border-radius:16px">{iconcircle("check", TSEL, "#0B5B55", 32, 16)}<div class="col"><b style="font:800 17px/22px \'Plus Jakarta Sans\'">{t}</b><span style="font:400 15px/22px Inter;color:{T2}">{d}</span></div></div>' for t, d in acc) + '</div>')
# 16 Voix et ton
tone = [('Rassurant', 'On explique ce qui protège, sans dramatiser.', 'Votre argent est protégé : 32,06 $ restent en séquestre.', 'ATTENTION! Risque de fraude!'),
        ('Direct', 'Verbe d’action, une idée par phrase.', 'Confirmer la remise', 'Procéder à la validation de la transaction'),
        ('Chaleureux', 'Vouvoiement, simple et poli, à la québécoise.', 'Bon retour! · Pas de panique, ça arrive.', 'Erreur 403 : authentification échouée'),
        ('Transparent', 'Montants et délais toujours précis.', 'Réponse sous 48 h · 100 % remboursé en 3 à 5 jours ouvrables', 'Remboursement sous peu')]
gloss = [('courriel', 'e-mail, mail'), ('texto', 'SMS (dans le texte)'), ('égoportrait', 'selfie'), ('clé d’accès', 'passkey'), ('séquestre', 'escrow, dépôt fiduciaire'), ('remise', 'handover, livraison (pour le voyageur)'), ('voyageur / expéditeur / destinataire', 'transporteur, client'), ('Envoi', 'colis (pour la transaction)')]
fmt = '<ul class="l" style="font-size:14.5px;line-height:22px"><li>Montants : <b>32,06 $</b> (virgule décimale, espace insécable avant $).</li><li>Heures : <b>21 h 40</b>; dates : <b>ven. 14 nov.</b></li><li>Ponctuation : espace insécable avant « : » ; « ? » et « ! » collés (usage québécois courant).</li><li>Majuscule initiale seulement dans les titres et boutons.</li><li>Codes aéroport et vols en JetBrains Mono : YUL → ALG, AT 201.</li><li>Écriture inclusive légère : « Ami·e », formulations neutres.</li></ul>'
P('Voix et ton · guide de microcopie FR-CA', '10 · Contenu', 'Volis parle comme un ami fiable qui connaît bien les voyages : clair, chaleureux, précis. Français québécois standard, vouvoiement, termes de l’OQLF.',
  f'<div class="g" style="grid-template-columns:1.5fr 1fr;gap:24px"><div class="col" style="gap:10px">' + ''.join(
      f'<div class="box2" style="padding:12px 16px;display:grid;grid-template-columns:150px 1fr 1fr;gap:14px;align-items:center"><div><b style="font:800 18px/22px \'Plus Jakarta Sans\'">{t}</b><div class="cap" style="font-size:12.5px">{d}</div></div>'
      f'<div class="row" style="gap:8px;align-items:flex-start">{ic("check", SUCC_FG, 18, 3)}<span style="font:500 14.5px/20px Inter">{g}</span></div><div class="row" style="gap:8px;align-items:flex-start">{ic("plus", ERR, 18, 2.6).replace("<path", "<path transform=\'rotate(45 12 12)\'")}<span style="font:500 14.5px/20px Inter;color:{T2};text-decoration:line-through">{b}</span></div></div>' for t, d, g, b in tone)
  + f'</div><div class="col" style="gap:14px"><div class="box2" style="padding:14px 16px"><div class="bt" style="margin-bottom:6px">Lexique</div><table class="t" style="font-size:13.5px"><tr><th>Dire</th><th>Éviter</th></tr>' + ''.join(f'<tr><td><b>{a}</b></td><td style="color:{T2}">{b}</td></tr>' for a, b in gloss) + f'</table></div><div class="box2" style="padding:14px 16px"><div class="bt" style="margin-bottom:6px">Formats</div>{fmt}</div></div></div>')
# 17 Do / don't
SC2 = '/workspace/volis-design/ecrans'
def shot(f, w=150): return f'<img src="file://{SC2}/{f}.png" style="width:{w}px;border-radius:18px;box-shadow:0 8px 20px -10px rgba(30,42,58,.5);flex:none"/>'
dd = [(True, 'Une seule action principale, en bas, pleine largeur.', shot('11-paiement-protege')), (True, 'Statuts : couleur + pastille + libellé, jamais la couleur seule.', f'<div class="col" style="gap:8px">{status("Embarqué", "teal")}{status("En attente", "warn")}{status("Annulé", "err")}</div>'),
      (True, 'Montrer la protection au moment où l’utilisateur paie ou remet le colis.', banner('teal', 'Votre argent est protégé', '32,06 $ en séquestre.')), (True, 'Caveat pour une petite annotation décorative.', f'<span style="font:600 26px/28px Caveat;color:{TEAL};transform:rotate(-3deg);display:block">← montre l’intérieur!</span>'),
      (False, 'Texte blanc sur corail (contraste 2,5:1).', f'<div style="height:48px;border-radius:24px;background:{CORAL};color:#fff;font:700 16px/48px Inter;text-align:center;width:220px">Continuer</div>'), (False, 'Caveat pour un champ, un bouton ou un montant.', f'<div style="height:48px;border-radius:24px;background:{TEAL};color:#fff;font:600 26px/48px Caveat;text-align:center;width:220px">Payer 32,06 $</div>'),
      (False, 'Coordonnées bancaires saisies dans Volis (passer par Stripe).', field('', 'N° de compte, transit…', 'bank', True).replace('class="fld" style="flex:none"', 'class="fld" style="flex:none;width:260px"')), (False, 'Plusieurs illustrations ou une illustration sur un formulaire dense.', f'<div class="row" style="gap:4px">{illus("b-remise", 80)}{illus("c-reception", 80)}{illus("e-inscription", 80)}</div>')]
P('À faire / à éviter', '11 · Règles', '', '<div class="g" style="grid-template-columns:repeat(4,1fr);gap:16px">' + ''.join(
    f'<div class="box2 {"do" if ok else "dont"}" style="display:flex;flex-direction:column;gap:12px;min-height:{330 if i<4 else 280}px"><div class="row" style="gap:8px">{status("À faire" if ok else "À éviter", "ok" if ok else "err", False)}</div>'
    f'<div style="flex:1;display:flex;align-items:center;justify-content:center">{v}</div><div style="font:600 15px/21px Inter">{t}</div></div>' for i, (ok, t, v) in enumerate(dd)) + '</div>')
if __name__ == '__main__':
    out = '/workspace/volis-design/build/charte'; os.makedirs(out, exist_ok=True)
    for i, (t, h) in enumerate(PAGES):
        open(f'{out}/p{i+1:02d}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{PCSS}</style></head><body>{h}</body></html>')
    open(f'{out}/all.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{PCSS}.grain{{display:none}}</style></head><body>{"".join(h for _, h in PAGES)}</body></html>')
    print(len(PAGES))
