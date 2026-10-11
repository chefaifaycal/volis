from kit import *
from fb import photo, person, kv, PARCEL
# ---------- 34 Vol annulé
def vol_annule():
    top = hdr('Imprévu sur votre envoi', SC, True, '', 'VL-4821 · vers Amina K.')
    fl = card(f'<div class="row" style="justify-content:space-between"><span class="row" style="gap:6px;font:700 13px/18px Inter">{ic("plane", T2, 16)}Vol <span class="mono">AT 201</span> · ven. 14 nov.</span>{status("Annulé", "err")}</div>'
              f'<div class="row" style="gap:10px;margin-top:6px"><b class="mono" style="font:700 26px/30px \'JetBrains Mono\';color:#8A8478;text-decoration:line-through">YUL</b><div style="flex:1;border-top:2px dotted #B9B09E"></div><b class="mono" style="font:700 26px/30px \'JetBrains Mono\';color:#8A8478;text-decoration:line-through">ALG</b></div>'
              f'<div class="row sm" style="gap:6px;margin-top:6px">{avatar("KB", 24)}<span style="color:{INK}">Karim B. a signalé l’annulation à 05 h 40.</span></div>', 'padding:12px 14px;margin-top:8px')
    sure = banner('teal', 'Votre argent est protégé', '32,06 $ restent en séquestre. Vous choisissez la suite, sans frais.')
    def opt(on, icn, t, d, extra=''):
        return (f'<div class="row" style="gap:12px;padding:12px 14px;border-radius:16px;background:{CARD};border:{2 if on else 1.5}px solid {TEAL if on else "#CFC4AF"};align-items:flex-start;flex:none">'
                f'{iconcircle(icn, TSEL if on else "#EFE8DA", "#0B5B55" if on else INK, 38, 19)}<div class="col" style="flex:1;gap:2px"><span class="b15" style="font-weight:700">{t}</span><span class="sm">{d}</span>{extra}</div>{radio(on)}</div>')
    alts = f'<div class="row" style="gap:6px;margin-top:6px">{avatar("NA", 26)}{avatar("YM", 26)}<span class="xs" style="font-weight:500">Nadia A. (15 nov.) et 2 autres</span></div>'
    opts = (f'<div class="col" style="gap:8px;flex:none;margin-top:12px"><span class="lab">Que voulez-vous faire?</span>'
            + opt(True, 'swap', 'Réattribuer à un autre voyageur', 'Même trajet, prix égal ou inférieur garanti.', alts)
            + opt(False, 'cal', 'Garder Karim sur son nouveau vol', 'Il propose sam. 15 nov. · AT 203.')
            + opt(False, 'dollar', 'Me faire rembourser', '100 % remboursé sur votre carte en 3 à 5 jours ouvrables.')
            + '</div>')
    note_ = f'<div class="row sm" style="gap:6px;flex:none;margin-top:10px">{ic("info", T2, 15)}Vol seulement retardé? Rien à faire : on vous avertit à chaque changement.</div>'
    return pg(f'{top}{fl}<div style="height:10px;flex:none"></div>{sure}{opts}{note_}<div class="sp"></div>{btn("Choisir un voyageur")}')
# ---------- 35 Litige
def litige():
    top = hdr('Signaler un problème', SC, True, '', 'Envoi VL-4821 · livré le 14 nov.')
    ch = f'<div class="fld" style="flex:none;margin-top:8px"><span class="lab">Quel est le problème?</span><div class="row" style="gap:6px;flex-wrap:wrap">{chip("Colis endommagé", True)}{chip("Contenu manquant")}{chip("Non livré")}{chip("Autre")}</div></div>'
    def ph(lbl, t, bg='#E9DFCC'):
        return (f'<div class="col" style="gap:4px;flex:none;width:84px"><div style="position:relative">{photo(84, 12).replace("#E9DFCC", bg)}'
                f'<span class="abs" style="left:4px;top:4px;background:rgba(30,42,58,.85);color:#fff;font:700 10px/14px Inter;padding:2px 6px;border-radius:6px">{lbl}</span></div><span class="xs" style="font-weight:500">{t}</span></div>')
    add = f'<div class="col" style="gap:4px;flex:none;width:84px"><div style="width:84px;height:84px;border-radius:12px;border:2px dashed #7E7A70;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;color:{TEAL};font:700 12px/16px Inter">{ic("camera", TEAL, 22)}Ajouter</div><span class="xs" style="font-weight:500">Vos photos</span></div>'
    ev = (f'<div class="fld" style="flex:none;margin-top:12px"><span class="lab">Preuves jointes automatiquement</span><div class="row" style="gap:10px;align-items:flex-start">'
          f'{ph("REMISE", "13 nov. 17 h 58")}{ph("SCELLÉ", "13 nov. 18 h 01", "#E2D5BE")}{add}</div>'
          f'<span class="xs" style="font-weight:500">Photos prises à la remise, horodatées et non modifiables.</span></div>')
    desc = f'<div class="fld" style="flex:none;margin-top:12px"><span class="lab">Décrivez ce qui s’est passé</span><div class="inp" style="height:76px;align-items:flex-start;padding-top:12px;font-size:15px;line-height:21px">Le coin de la boîte est écrasé et le cadeau en verre est fêlé.</div></div>'
    cap = card(f'<div class="row" style="gap:8px;margin-bottom:4px">{ic("shield", "#0B5B55", 18, 2.2)}<span style="font:700 14px/18px Inter;color:#0B5B55">Indemnisation possible</span></div>'
               f'{kv("Protection de base Volis", "jusqu’à 100 $")}{kv("Votre assurance Bouclier (option)", "<b>jusqu’à 120 $</b>")}'
               f'<div class="xs" style="font-weight:500;margin-top:2px">Plafond = valeur déclarée. Les fonds de Karim sont gelés pendant l’examen.</div>', 'padding:10px 14px;margin-top:12px;background:#F4FAF8;border-color:#A8D5CC')
    when = f'<div class="row sm" style="gap:6px;flex:none;margin-top:8px">{ic("clock", T2, 15)}Réponse de notre équipe sous 48 h · délai pour signaler : 72 h.</div>'
    return pg(f'{top}{ch}{ev}{desc}{cap}{when}<div class="sp" style="min-height:10px"></div>{btn("Ouvrir un litige", "primary")}')
# ---------- 36 État vide + alerte
def vide():
    route = (f'<div class="row cd" style="flex:1;height:48px;padding:0 6px 0 14px;gap:8px;border-radius:24px">'
             f'<b class="mono" style="font:700 15px/20px \'JetBrains Mono\'">YUL → TLM</b><span class="sm" style="flex:1;white-space:nowrap">· 14 nov. · 2 kg</span>'
             f'<span style="width:36px;height:36px;display:flex;align-items:center;justify-content:center">{ic("edit", TEAL, 18)}</span></div>')
    top = f'<div class="row" style="gap:10px;height:48px;flex:none"><div class="ibtn">{ic("back", INK)}</div>{route}</div>'
    art = f'<div class="row" style="justify-content:center;flex:none;margin-top:10px">{illus("a-voyageur", 180)}</div>'
    t = (f'<div class="col" style="align-items:center;text-align:center;flex:none;margin-top:8px"><span class="h1" style="font-size:23px;line-height:29px">Aucun voyageur pour l’instant</span>'
         f'<span style="font:400 15px/21px Inter;color:{T2};margin-top:6px;max-width:330px">Personne ne part encore vers Tlemcen à ces dates. Les voyages se publient souvent 1 à 3 semaines avant le départ.</span></div>')
    al = card(f'<div class="row" style="gap:10px">{iconcircle("bell", PEACH, INK, 40, 20)}<div class="col" style="flex:1"><span class="b15" style="font-weight:700">Créer une alerte</span><span class="xs" style="font-weight:500">On vous écrit dès qu’un voyageur publie ce trajet.</span></div></div>'
              f'<div style="border-top:1.5px solid {LINE};margin:10px 0 2px"></div>'
              f'<div class="row" style="min-height:46px;gap:10px"><span class="b15" style="flex:1;font-weight:500">Dates flexibles (± 7 jours)</span>{toggle(True)}</div>'
              f'<div class="row" style="min-height:46px;gap:10px;border-top:1.5px solid {LINE}"><span class="b15" style="flex:1;font-weight:500">Aussi vers Oran (ORN)</span>{toggle(False)}</div>', 'padding:12px 14px;margin-top:16px')
    cta = f'<div class="col" style="gap:6px;flex:none">{btn("Créer l’alerte", "primary", "bell")}{btn("Élargir à toute l’Algérie", "ghost", None, 44)}</div>'
    return pg(f'{top}{art}{t}{al}<div class="sp"></div>{cta}', 0, blob(8, 196, 200, 110, '#BFE3DB', .5))
# ---------- 37 Remise hors ligne
def hors_ligne():
    off = (f'<div class="row" style="flex:none;gap:8px;height:40px;padding:0 12px;border-radius:20px;background:{INK};color:#fff;font:600 13px/18px Inter;justify-content:center;margin-top:2px">'
           f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M2 8.8a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0M12 20h.01M3 3l18 18" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>Hors ligne · le code fonctionne sans réseau</div>')
    top = hdr('Remise du colis', SC, True, '', 'Jeu. 13 nov. · Berri-UQAM')
    digits = ''.join(f'<span style="width:50px;height:60px;border-radius:12px;background:{CARD};border:2px solid {INK};display:flex;align-items:center;justify-content:center;font:700 32px/1 \'JetBrains Mono\';color:{INK}">{d}</span>' for d in '4821')
    qrbox = card(f'<div class="col" style="align-items:center;gap:10px"><div class="row" style="gap:6px">{status("Code enregistré sur l’appareil", "ok")}</div>'
                 f'<div style="position:relative;padding:6px;border-radius:12px;background:#fff;border:1.5px solid {LINE}">{qr(160)}<div class="abs" style="left:50%;top:50%;transform:translate(-50%,-50%)">{appicon(28)}</div></div>'
                 f'<span class="xs">ou dictez le code</span><div class="row" style="gap:10px" aria-label="Code 4821">{digits}</div>'
                 f'<span class="xs" style="font-weight:500">Valide jusqu’au 13 nov. 23 h 59 · signé numériquement</span></div>', 'padding:14px;margin-top:10px')
    how = card(f'<span class="b15" style="font-weight:700">Comment ça marche hors ligne</span>'
               + ''.join(f'<div class="row" style="gap:10px;min-height:34px;margin-top:2px"><span style="width:22px;height:22px;border-radius:11px;background:{TSEL};color:#0B5B55;font:800 12px/22px Inter;text-align:center;flex:none">{i+1}</span><span class="sm" style="color:{INK}">{t}</span></div>'
                         for i, t in enumerate(['Le voyageur scanne le code, même sans réseau.', 'Les deux appareils gardent une preuve horodatée.', 'Tout se synchronise au retour du réseau.'])), 'padding:12px 14px;margin-top:10px')
    cta = f'<div class="col" style="gap:6px;flex:none">{btn("Confirmer la remise")}<div class="row xs" style="justify-content:center;gap:6px;font-weight:500">{ic("clock", T2, 13)}Dernière synchro : 17 h 42</div></div>'
    return pg(f'{top}{off}{qrbox}{how}<div class="sp"></div>{cta}')
# ---------- 38 Filtres (bottom sheet)
def filtres():
    import screens as S
    base = S.resultats(False)
    def sec(t, inner, first=False): return f'<div style="flex:none;{"" if first else "border-top:1.5px solid "+LINE+";"}padding:10px 0"><div class="lab" style="margin-bottom:8px">{t}</div>{inner}</div>'
    sl = (f'<div class="row" style="justify-content:space-between;margin-bottom:6px"><span class="sm">Jusqu’à</span><b style="font:800 16px/20px \'Plus Jakarta Sans\'">35 $</b></div>'
          f'<div style="height:6px;border-radius:3px;background:#DCD3C2;position:relative;margin:10px 4px 6px"><i style="position:absolute;left:0;width:62%;height:6px;border-radius:3px;background:{TEAL}"></i><i style="position:absolute;left:62%;top:-11px;width:28px;height:28px;margin-left:-14px;border-radius:14px;background:#fff;border:2.5px solid {TEAL};box-shadow:0 2px 6px rgba(0,0,0,.15)"></i></div>')
    inner = (f'<div class="row" style="justify-content:space-between;height:44px;flex:none"><span class="h2" style="font-size:19px">Filtres</span><span class="link" style="font-size:15px">Réinitialiser</span></div>'
             + sec('Trier par', f'<div class="row" style="gap:6px;flex-wrap:wrap">{chip("Recommandés", True)}{chip("Prix")}{chip("Date")}{chip("Note")}</div>', True)
             + sec('Date de départ', seg(['Date exacte', '± 3 jours', '± 7 jours'], 1))
             + sec('Prix total pour 2 kg', sl)
             + sec('Confiance', f'<div class="row" style="min-height:44px;gap:10px">{ic("id", T2, 20)}<span class="b15" style="flex:1;font-weight:500">ID vérifiée seulement</span>{toggle(True)}</div><div class="row" style="min-height:44px;gap:10px">{ic("plane", T2, 20)}<span class="b15" style="flex:1;font-weight:500">Vol confirmé</span>{toggle(False)}</div>')
             + sec('Note minimale', f'<div class="row" style="gap:6px">{chip("Toutes")}{chip("4,0+")}{chip("4,5+", True)}</div>')
             + f'<div style="flex:none;margin-top:6px">{btn("Afficher 8 voyageurs")}</div>')
    return base.replace('</div></body>', sheet(inner, 118) + '</div></body>', 1)
# ---------- 39 Vue carte
def carte():
    W, H = 393, 852
    land = ('<path d="M-10 0 H403 V852 H-10Z" fill="#EFE7D6"/>'
            '<path d="M-20 470 C 60 430, 120 470, 190 420 S 330 330, 420 300 L 420 380 C 330 410, 260 470, 190 500 S 50 540, -20 560Z" fill="#BFDCE0"/>'
            '<path d="M60 200 C 140 160, 260 170, 330 250 C 360 290, 330 340, 270 360 C 200 385, 150 430, 90 420 C 30 410, 10 340, 20 280 C 25 240, 40 215, 60 200Z" fill="#F7F1E4" stroke="#D8CDB6" stroke-width="2"/>'
            '<path d="M120 640 C 200 610, 300 640, 420 600 L 420 852 L -20 852 L -20 690 C 30 670, 70 660, 120 640Z" fill="#F7F1E4" stroke="#D8CDB6" stroke-width="2"/>')
    streets = ''.join(f'<path d="{d}" stroke="#FFFFFF" stroke-width="{w}" fill="none" stroke-linecap="round"/>' for d, w in [
        ('M70 260 L 320 300', 6), ('M110 210 L 160 410', 5), ('M200 190 L 230 380', 5), ('M40 330 L 300 340', 4), ('M260 200 L 300 350', 4), ('M150 680 L 400 650', 5), ('M220 640 L 260 852', 4)])
    park = '<path d="M170 250 C 190 235, 225 240, 230 262 C 235 285, 200 300, 182 290 C 165 282, 160 262, 170 250Z" fill="#CFE5C8"/>'
    lbl = lambda x, y, t, s=11: f'<text x="{x}" y="{y}" font-family="Inter" font-weight="600" font-size="{s}" fill="#7A7366">{t}</text>'
    txt = lbl(176, 316, 'Plateau') + lbl(84, 386, 'Verdun') + lbl(250, 230, 'Rosemont') + lbl(160, 455, 'Fleuve Saint-Laurent', 12).replace('#7A7366', '#4F7F86') + lbl(280, 700, 'Longueuil')
    svg = f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:0;top:0">{land}{park}{streets}{txt}</svg>'
    def pin(x, y, p, on=False, ini=''):
        bg = INK if on else CARD; c = '#fff' if on else INK
        return (f'<div class="abs" style="left:{x}px;top:{y}px;transform:translate(-50%,-100%);z-index:5;display:flex;flex-direction:column;align-items:center">'
                f'<div class="row" style="gap:5px;height:34px;padding:0 10px 0 4px;border-radius:17px;background:{bg};color:{c};font:800 14px/1 \'Plus Jakarta Sans\';white-space:nowrap;box-shadow:0 4px 10px -3px rgba(30,42,58,.45);border:1.5px solid {INK}">'
                f'<span style="width:26px;height:26px;border-radius:13px;background:{AVC.get(ini, "#BFE3DB")};color:{INK};font:800 10px/26px \'Plus Jakarta Sans\';text-align:center">{ini}</span>{p}</div>'
                f'<i style="width:0;height:0;border-left:6px solid transparent;border-right:6px solid transparent;border-top:7px solid {INK}"></i></div>')
    me = f'<div class="abs" style="left:150px;top:340px;width:20px;height:20px;border-radius:10px;background:#2B6CB0;border:3px solid #fff;box-shadow:0 0 0 10px rgba(43,108,176,.18);z-index:4"></div>'
    pins = pin(196, 300, '31 $', True, 'KB') + pin(100, 260, '29 $', False, 'NA') + pin(290, 290, '26 $', False, 'YM') + pin(318, 430, '33 $', False, 'SL')
    route = (f'<div class="row cd" style="flex:1;height:48px;padding:0 6px 0 14px;gap:8px;border-radius:24px;box-shadow:0 6px 16px -8px rgba(30,42,58,.4)">'
             f'<b class="mono" style="font:700 15px/20px \'JetBrains Mono\'">YUL → ALG</b><span class="sm" style="flex:1;white-space:nowrap">· 14 nov. · 2 kg</span>'
             f'<span style="width:36px;height:36px;display:flex;align-items:center;justify-content:center">{ic("sliders", TEAL, 18)}</span></div>')
    top = f'<div class="row" style="gap:10px;height:48px;flex:none;position:relative;z-index:6"><div class="ibtn" style="box-shadow:0 6px 16px -8px rgba(30,42,58,.4)">{ic("back", INK)}</div>{route}</div>'
    tg = f'<div style="flex:none;margin-top:10px;position:relative;z-index:6;width:220px;align-self:center;box-shadow:0 6px 16px -8px rgba(30,42,58,.4);border-radius:22px">{seg(["Liste", "Carte"], 1)}</div>'
    leg = f'<div class="row" style="flex:none;margin-top:10px;position:relative;z-index:6;align-self:center"><span class="badge" style="background:{CARD};color:{INK};border:1.5px solid {LINE};height:30px">{ic("pin", TEAL, 14)}Points de remise proposés · Montréal</span></div>'
    loc = f'<div class="abs" style="right:16px;top:520px;z-index:6"><div class="ibtn" style="box-shadow:0 6px 16px -8px rgba(30,42,58,.4)">{ic("pin", INK, 20)}</div></div>'
    sel = card(f'<div class="row" style="gap:12px;align-items:flex-start">{avatar("KB", 46)}<div class="col" style="flex:1;gap:4px"><div class="row" style="gap:6px"><span class="b15" style="font:700 16px/20px Inter">Karim B.</span><span class="row" style="gap:3px;font:600 13px/18px Inter">{star(CORAL, 13)}4,9 <span class="t2" style="font-weight:500">(38)</span></span></div>'
               f'<div class="row" style="gap:6px">{vbadge("id")}{vbadge("vol")}</div><span class="sm" style="color:{INK}">Remise : Berri-UQAM · à 1,2 km</span></div>'
               f'<div class="col" style="align-items:flex-end"><span style="font:800 21px/24px \'Plus Jakarta Sans\'">31 $</span><span class="xs" style="font-weight:500">5 kg dispo</span></div></div>'
               f'<div class="row" style="gap:8px;margin-top:10px">{btn("Voir le profil", "secondary", None, 44, "flex:1")}{btn("Demander", "primary", None, 44, "flex:1")}</div>', 'padding:14px;box-shadow:0 12px 26px -10px rgba(30,42,58,.45)')
    body = f'{top}{tg}{leg}<div class="sp"></div><div class="row" style="justify-content:center;gap:5px;flex:none;margin-bottom:8px"><i style="width:18px;height:6px;border-radius:3px;background:{INK}"></i><i style="width:6px;height:6px;border-radius:3px;background:#A39B8A"></i><i style="width:6px;height:6px;border-radius:3px;background:#A39B8A"></i><i style="width:6px;height:6px;border-radius:3px;background:#A39B8A"></i></div>{sel}'
    return pg(body, 0, svg + me + pins + loc, '#EFE7D6')
FC = [('34-vol-annule-reattribuer', vol_annule), ('35-signaler-probleme-litige', litige), ('36-etat-vide-alerte', vide), ('37-remise-hors-ligne', hors_ligne),
      ('38-filtres-bottom-sheet', filtres), ('39-vue-carte', carte)]
