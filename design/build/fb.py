from kit import *
PARCEL = (f'<svg width="56" height="48" viewBox="0 0 76 64"><path d="M8 20 L38 10 L68 20 L68 52 L38 62 L8 52Z" fill="#D9A86C" stroke="{INK}" stroke-width="2.4"/><path d="M8 20 L38 30 L68 20 M38 30 L38 62" stroke="{INK}" stroke-width="2.4" fill="none"/>'
          f'<path d="M22 15 L52 25 L52 35" stroke="{CORAL}" stroke-width="7" fill="none"/></svg>')
def photo(s=64, r=12):
    return f'<div style="width:{s}px;height:{s}px;border-radius:{r}px;background:#E9DFCC;display:flex;align-items:center;justify-content:center;flex:none">{PARCEL.replace("width=\"56\" height=\"48\"", f"width=\"{s*.72:.0f}\" height=\"{s*.62:.0f}\"")}</div>'
def person(ini, name, sub, right=''):
    return (f'<div class="row" style="gap:12px">{avatar(ini, 44)}<div class="col" style="flex:1;gap:2px"><span class="b15" style="font-weight:700">{name}</span>'
            f'<span class="row xs" style="gap:4px;font-weight:500">{sub}</span></div>{right}</div>')
def kv(k, v): return f'<div class="row" style="justify-content:space-between;min-height:30px"><span class="sm">{k}</span><span style="font:600 14px/20px Inter;color:{INK};text-align:right">{v}</span></div>'
# ---------- 26 Détail demande (voyageur)
def demande():
    top = hdr('Nouvelle demande', SC, True, '', 'Pour votre vol YUL → ALG · 14 nov.')
    exp = f'<div class="row" style="flex:none;margin-top:6px">{status("Expire dans 23 h 12 min", "warn")}</div>'
    who = card(person('CT', 'Camille T.', f'{star(CORAL, 12)}4,8 · 6 avis · {ic("shield", "#0B5B55", 12, 2.4)}<span style="color:#0B5B55">ID vérifiée</span>', f'<div class="ibtn" style="width:44px;height:44px">{ic("chat", TEAL, 19)}</div>'), 'padding:12px 14px;margin-top:10px')
    par = card(f'<div class="row" style="gap:12px;align-items:flex-start">{photo(72)}{photo(72).replace("#E9DFCC", "#E2D5BE")}<div class="col" style="flex:1;gap:4px"><span class="b15" style="font-weight:700">Vêtements, cadeau</span><span class="sm">2 photos · ouvert et fermé</span></div></div>'
               f'<div style="border-top:1.5px solid {LINE};margin:10px 0 4px"></div>{kv("Poids", "2,0 kg")}{kv("Dimensions", "30 × 20 × 15 cm")}{kv("Valeur déclarée", "120 $")}{kv("Destinataire", "Amina K. · Alger")}{kv("Remise proposée", "Jeu. 13 nov. · Berri-UQAM")}', 'padding:12px 14px;margin-top:10px')
    gain = (f'<div class="row" style="flex:none;margin-top:10px;padding:12px 14px;border-radius:16px;background:{MINT};gap:12px">{iconcircle("wallet", "#FFFDF8", "#0B5B55", 40, 20)}'
            f'<div class="col" style="flex:1"><span style="font:700 14px/18px Inter;color:#0B5B55">Vous recevrez</span><span class="xs" style="color:#24504B">Versé après la remise au destinataire</span></div><b style="font:800 22px/26px \'Plus Jakarta Sans\'">24,00 $</b></div>')
    cap = f'<div class="row" style="gap:8px;flex:none;margin-top:10px"><span class="xs" style="flex:1">Capacité après acceptation : <b style="color:{INK}">3 kg sur 5</b></span></div><div class="row" style="gap:3px;flex:none;margin-top:4px"><i style="flex:2;height:6px;border-radius:3px;background:{TEAL}"></i><i style="flex:3;height:6px;border-radius:3px;background:#DCD3C2"></i></div>'
    insp = f'<div class="row sm" style="gap:6px;flex:none;margin-top:10px">{ic("shield", TEAL, 15)}Vous pourrez inspecter le colis à la remise et refuser au besoin.</div>'
    cta = f'<div class="row" style="gap:10px;flex:none">{btn("Refuser", "secondary", None, 56, "flex:1")}{btn("Accepter", "primary", "check", 56, "flex:1.6")}</div>'
    return pg(f'{top}{exp}{who}{par}{gain}{cap}{insp}<div class="sp"></div>{cta}')
# ---------- 27-29 Détail envoi (expéditeur)
def envoi(state):
    top = hdr('Envoi VL-4821', SC, True, f'<div class="ibtn">{ic("help", INK, 20)}</div>', 'Vers Amina K. · Alger')
    if state == 'wait':
        ban = banner('warn', 'En attente de Karim', 'Il a jusqu’à demain 14 h 05 pour répondre. On vous avertit dès qu’il répond.', 'clock')
        pay = card(f'{kv("Montant pré-autorisé", "32,06 $")}<div class="row xs" style="gap:6px;font-weight:500;margin-top:2px">{ic("lock", T2, 13)}Rien n’est débité tant que Karim n’a pas accepté.</div>', 'padding:10px 14px;margin-top:10px')
        cta = f'<div class="col" style="gap:6px;flex:none">{btn("Écrire à Karim", "secondary", "chat")}{btn("Annuler la demande", "ghost", None, 44, "color:"+ERR)}</div>'
        st = 1
    elif state == 'ok':
        ban = banner('ok', 'Karim a accepté votre envoi!', 'Paiement sécurisé en séquestre. Prochaine étape : convenir de la remise.', 'check')
        pay = card(f'{kv("En séquestre", "<span style=\'color:#0B5B55\'>32,06 $</span>")}{kv("Remise", "Jeu. 13 nov. · 18 h · Berri-UQAM")}{kv("Vol", "<span class=\'mono\'>AT 201</span> · ven. 14 nov. 08 h 15")}', 'padding:8px 14px;margin-top:10px')
        cta = f'<div class="col" style="gap:8px;flex:none">{btn("Préparer la remise", "primary", "qr")}{btn("Ajouter le destinataire", "ghost", "plus", 44)}</div>'
        st = 2
    else:
        ban = banner('err', 'Karim n’a pas pu accepter', 'Motif : « Plus assez de place dans ma valise. » La pré-autorisation est annulée, aucuns frais.', 'alert')
        alts = ''.join(f'<div class="row" style="gap:10px;min-height:56px;{"border-top:1.5px solid "+LINE if i else ""}">{avatar(a, 36)}<div class="col" style="flex:1"><span class="b15" style="font-weight:700">{n}</span><span class="xs" style="font-weight:500">{d}</span></div><b style="font:800 17px/20px \'Plus Jakarta Sans\'">{p}</b></div>'
                       for i, (a, n, d, p) in enumerate([('NA', 'Nadia A.', 'Sam. 15 nov. · 3 kg · ID vérifiée', '29 $'), ('YM', 'Yanis M.', 'Lun. 17 nov. · 8 kg · ID vérifiée', '26 $')]))
        pay = f'<div style="flex:none;margin-top:12px">{sect("Autres voyageurs sur ce trajet", SC)}</div>' + card(alts, 'padding:4px 14px;margin-top:4px')
        cta = btn('Voir tous les voyageurs', 'primary', 'search')
        st = 0
    trav = card(person('KB', 'Karim B.', f'{star(CORAL, 12)}4,9 (38 avis) · YUL → ALG · 14 nov.', f'<div class="ibtn">{ic("chat", TEAL, 19)}</div>'), 'padding:12px 14px;margin-top:10px' + (';opacity:.6' if state == 'no' else ''))
    par = card(f'<div class="row" style="gap:12px">{photo(52)}<div class="col" style="flex:1"><span class="b15" style="font-weight:700">Vêtements, cadeau</span><span class="sm">2,0 kg · 30 × 20 × 15 cm · 120 $ déclarés</span></div></div>', 'padding:10px 14px;margin-top:10px')
    labs = ['Demande envoyée', 'Réponse du voyageur', 'Remise', 'Livraison']
    steps = ''
    for i, l in enumerate(labs):
        if state == 'no' and i == 1: c, t = ERR, 'Refusée'
        elif i < st: c, t = TEAL, l
        elif i == st and state != 'no': c, t = CORAL, l
        else: c, t = '#CFC6B4', l
        steps += f'<div class="col" style="flex:1;gap:5px"><i style="height:6px;border-radius:3px;background:{c}"></i><span style="font:{"700" if i<=st or (state=="no" and i==1) else "500"} 11.5px/15px Inter;color:{ERR_FG if c==ERR else (INK if i<=st else T2)}">{t if not (state=="no" and i==1) else "Refusée"}</span></div>'
    prog = f'<div class="row" style="gap:5px;flex:none;margin-top:12px;align-items:flex-start">{steps}</div>'
    body = f'{top}{prog}<div style="height:12px;flex:none"></div>{ban}{trav}{par}{pay}<div class="sp"></div>{cta}'
    return pg(body, None)
# ---------- 30 Mes envois
def env_card(code, dest, route, st_html, sub, seg_n=None, bar=None, avatar_='KB'):
    segbar = ''
    if seg_n is not None:
        segbar = '<div class="row" style="gap:3px;margin-top:8px">' + ''.join(f'<i style="flex:1;height:5px;border-radius:3px;background:{TEAL if j<seg_n else "#DCD3C2"}"></i>' for j in range(7)) + '</div>'
    return card(f'<div class="row" style="gap:12px;align-items:flex-start">{photo(48, 12)}<div class="col" style="flex:1;min-width:0;gap:3px">'
                f'<div class="row" style="justify-content:space-between;gap:6px"><span class="b15" style="font-weight:700;white-space:nowrap">{dest}</span>{st_html}</div>'
                f'<span class="sm"><b class="mono" style="color:{INK}">{route}</b> · {sub}</span><span class="mono xs" style="font-weight:500">{code}</span></div></div>{segbar}', 'padding:12px 14px')
def mes_envois():
    top = f'<div class="row" style="height:48px;flex:none;justify-content:space-between"><span class="h1" style="font-size:26px">Mes envois</span>{btn("Nouvel envoi", "primary", "plus", 44, "padding:0 16px")}</div>'
    tabs = f'<div style="flex:none;margin-top:10px">{seg(["En cours (3)", "Terminés (5)"], 0)}</div>'
    cards = (f'<div class="col" style="gap:10px;flex:none;margin-top:12px">'
             + env_card('VL-4821', 'Amina K. · Alger', 'YUL → ALG', status('Embarqué', 'teal'), 'avec Karim B.', 4)
             + env_card('VL-4907', 'Yacine D. · Oran', 'YUL → ORN', status('En attente', 'warn'), 'demande à Yanis M.')
             + env_card('VL-4930', 'Leïla S. · Casablanca', 'YUL → CMN', status('Brouillon', 'mute'), 'étape 2 sur 4')
             + '</div>')
    past = f'<div style="flex:none;margin-top:14px">{sect("Récemment terminés", SC, "Tout voir")}</div>' + f'<div class="col" style="gap:10px;flex:none;margin-top:4px">' + env_card('VL-4410', 'Amina K. · Alger', 'YUL → ALG', status('Livré', 'ok'), '2 oct. · avis laissé') + '</div>'
    return pg(f'{top}{tabs}{cards}{past}', 1)
# ---------- 31 Mes voyages
def mes_voyages():
    top = f'<div class="row" style="height:48px;flex:none;justify-content:space-between"><span class="h1" style="font-size:26px">Mes voyages</span>{btn("Publier", "primary", "plus", 44, "padding:0 16px")}</div>'
    tabs = f'<div style="flex:none;margin-top:10px">{seg(["À venir (1)", "Passés (4)"], 0)}</div>'
    trip = card(f'<div class="row" style="justify-content:space-between"><span class="xs mono" style="color:{TEAL};letter-spacing:1px;font-weight:700">VEN. 14 NOV. · AT 201</span>{status("Publié", "ok")}</div>'
                f'<div class="row" style="gap:10px;margin-top:8px"><div class="col"><b class="mono" style="font:700 26px/30px \'JetBrains Mono\'">YUL</b><span class="xs" style="font-weight:500">Montréal · 08 h 15</span></div>'
                f'<div style="flex:1;border-top:2px dotted {INK};position:relative;margin-bottom:14px"><span style="position:absolute;left:50%;top:-12px;transform:translateX(-50%);background:{CARD};padding:0 4px">{ic("plane", TEAL, 20)}</span></div>'
                f'<div class="col" style="align-items:flex-end"><b class="mono" style="font:700 26px/30px \'JetBrains Mono\'">ALG</b><span class="xs" style="font-weight:500">Alger · 21 h 40</span></div></div>'
                f'<div class="row" style="justify-content:space-between;margin-top:12px"><span class="sm" style="color:{INK}"><b>2 kg réservés</b> sur 5 kg</span><span class="sm">12 $/kg</span></div>'
                f'<div class="row" style="gap:3px;margin-top:6px"><i style="flex:2;height:8px;border-radius:4px;background:{TEAL}"></i><i style="flex:1;height:8px;border-radius:4px;background:{CORAL}"></i><i style="flex:2;height:8px;border-radius:4px;background:#DCD3C2"></i></div>'
                f'<div class="row xs" style="gap:12px;margin-top:6px;font-weight:500"><span class="row" style="gap:4px"><i style="width:8px;height:8px;border-radius:4px;background:{TEAL}"></i>Accepté</span><span class="row" style="gap:4px"><i style="width:8px;height:8px;border-radius:4px;background:{CORAL}"></i>En attente (1 kg)</span><span class="row" style="gap:4px"><i style="width:8px;height:8px;border-radius:4px;background:#DCD3C2"></i>Libre</span></div>', 'padding:14px')
    reqs = ''.join(f'<div class="row" style="gap:10px;min-height:60px;{"border-top:1.5px solid "+LINE if i else ""}">{avatar(a, 38)}<div class="col" style="flex:1"><span class="b15" style="font-weight:700">{n}</span><span class="xs" style="font-weight:500">{d}</span></div>{s}</div>'
                   for i, (a, n, d, s) in enumerate([('CT', 'Camille T.', '2,0 kg · vêtements, cadeau · 24 $', status('Accepté', 'ok')), ('SL', 'Sarah L.', '1,0 kg · documents · 12 $', f'<span class="row" style="height:36px;padding:0 14px;border-radius:18px;background:{TEAL};color:#fff;font:700 13px/18px Inter">Répondre</span>')]))
    rq = f'<div style="flex:none;margin-top:14px">{sect("Demandes pour ce vol", SC)}</div>' + card(reqs, 'padding:2px 14px;margin-top:4px')
    gain = (f'<div class="row" style="flex:none;margin-top:12px;padding:12px 14px;border-radius:16px;background:{MINT};gap:12px">{ic("wallet", "#0B5B55", 20)}'
            f'<span style="flex:1;font:600 14px/18px Inter;color:#0B5B55">Gain prévu pour ce voyage</span><b style="font:800 20px/24px \'Plus Jakarta Sans\'">36,00 $</b></div>')
    tip = f'<div class="row sm" style="gap:6px;flex:none;margin-top:10px">{ic("info", T2, 15)}Les détails de votre vol restent privés jusqu’à l’acceptation.</div>'
    return pg(f'{top}{tabs}<div style="height:12px;flex:none"></div>{trip}{rq}{gain}{tip}', 2)
# ---------- 32 Notifications
def notifs():
    top = hdr('Notifications', SC, True, '<span class="link" style="font-size:14px">Tout lire</span>')
    def n(icn, bg, c, t, d, tm, unread=False):
        dot = f'<i style="width:9px;height:9px;border-radius:5px;background:{CORAL};flex:none;margin-top:6px"></i>' if unread else '<i style="width:9px;flex:none"></i>'
        return (f'<div class="row" style="gap:12px;align-items:flex-start;padding:12px 0;border-top:1.5px solid {LINE}">{iconcircle(icn, bg, c, 40, 19)}'
                f'<div class="col" style="flex:1;gap:2px"><span style="font:{"700" if unread else "600"} 14.5px/19px Inter">{t}</span><span style="font:400 13px/18px Inter;color:{T2}">{d}</span><span class="xs" style="font-weight:500;color:#6F6A60;margin-top:2px">{tm}</span></div>{dot}</div>')
    g1 = (f'<div class="xs" style="margin-top:8px;flex:none;letter-spacing:.5px">AUJOURD’HUI</div><div class="col" style="flex:none">'
          + n('plane', TSEL, '#0B5B55', 'Votre colis est embarqué', 'VL-4821 · vol AT 201 vers Alger, arrivée prévue 21 h 40.', 'Il y a 12 min', True)
          + n('alert', WARN_BG, WARN_IC, 'Vol retardé de 45 min', 'AT 201 part maintenant à 09 h 00. Rien à faire de votre côté.', 'Il y a 1 h', True)
          + n('chat', '#EAE2D2', INK, 'Karim B. vous a écrit', '« Bien reçu, colis scellé dans ma valise! »', '06 h 14')
          + '</div>')
    g2 = (f'<div class="xs" style="margin-top:12px;flex:none;letter-spacing:.5px">CETTE SEMAINE</div><div class="col" style="flex:none">'
          + n('lock', TSEL, '#0B5B55', 'Paiement sécurisé', '32,06 $ en séquestre jusqu’à la livraison.', 'Mer. 12 nov.')
          + n('shield', SUCC_BG, SUCC_FG, 'Identité vérifiée', 'Votre badge « ID vérifiée » est actif.', 'Mer. 12 nov.')
          + n('user', PEACH, INK, 'Nouvelle demande', 'Sarah L. veut envoyer 1 kg de documents.', 'Mar. 11 nov.')
          + '</div>')
    pref = f'<div class="row" style="justify-content:center;flex:none;margin-top:4px"><span class="link" style="font-size:14px">{ic("sliders", TEAL, 16)}&nbsp;Gérer mes préférences</span></div>'
    return pg(f'{top}{g1}{g2}{pref}', None)
# ---------- 33 Livraison confirmée + notation
def notation():
    top = hdr('', SC, False, f'<div class="ibtn">{ic("plus", INK, 20, 2.2).replace("<path", "<path transform=\'rotate(45 12 12)\'")}</div>')
    art = f'<div class="row" style="justify-content:center;flex:none;margin-top:-40px;position:relative;z-index:1">{illus("c-reception", 150)}</div>'
    hd = (f'<div class="col" style="align-items:center;text-align:center;flex:none;margin-top:4px"><span class="h1" style="font-size:25px">Colis livré!</span>'
          f'<span style="font:400 14px/20px Inter;color:{T2};margin-top:4px">Amina K. a confirmé la réception à 22 h 15.<br>Le paiement de Karim est maintenant libéré.</span></div>')
    stars = ''.join(star(CORAL if i < 4 else '#FFFDF8', 40) for i in range(5))
    rate = (card(f'<div class="col" style="align-items:center;gap:6px">{person("KB", "Notez Karim B.", "Votre avis aide toute la communauté").replace("flex:1;gap:2px", "gap:2px")}'
                 f'<div class="row" style="gap:6px;margin-top:6px" aria-label="4 étoiles sur 5">{stars}</div><span class="xs">Très bien</span></div>'
                 f'<div class="row" style="gap:6px;flex-wrap:wrap;justify-content:center;margin-top:10px">{chip("Ponctuel", True)}{chip("Soigneux", True)}{chip("Bonne communication")}{chip("Flexible")}</div>'
                 f'<div class="inp" style="height:64px;align-items:flex-start;padding-top:12px;margin-top:10px"><span style="color:#6F6A60;font-weight:400;font-size:15px">Un mot pour les prochains expéditeurs (facultatif)</span></div>', 'padding:12px 14px;margin-top:10px'))
    blind = (f'<div class="row" style="gap:10px;flex:none;margin-top:10px;padding:10px 12px;border-radius:14px;background:{INFO_BG}">{ic("lock", INFO_FG, 18, 2.2)}'
             f'<span style="font:400 13px/18px Inter;color:{INK}"><b>Avis en double aveugle :</b> le vôtre reste caché jusqu’à ce que Karim publie le sien, ou dans 14 jours.</span></div>')
    cta = f'<div class="col" style="gap:4px;flex:none">{btn("Publier mon avis")}<div class="row" style="justify-content:center"><span class="link" style="color:{ERR}">Signaler un problème</span></div></div>'
    return pg(f'{top}{art}{hd}{rate}{blind}<div class="sp" style="min-height:12px"></div>{cta}', None, blob(4, 196, 170, 120, '#FFC4B2', .5))
FB = [('26-demande-detail-voyageur', demande), ('27-envoi-detail-en-attente', lambda: envoi('wait')), ('28-envoi-detail-accepte', lambda: envoi('ok')), ('29-envoi-detail-refuse', lambda: envoi('no')),
      ('30-mes-envois', mes_envois), ('31-mes-voyages', mes_voyages), ('32-notifications', notifs), ('33-livraison-confirmee-notation', notation)]
