from kit import *
# ---------- 17 Vérification d'identité : intro
def verif_intro():
    top = hdr('', SC, True, '<span class="link" style="font-size:15px">Plus tard</span>')
    art = f'<div class="row" style="justify-content:center;flex:none;margin-top:-6px;position:relative">{illus("e-inscription", 190)}</div>'
    def st(n, icn, t, d):
        return (f'<div class="row" style="gap:12px;min-height:66px;padding:4px 0;{"border-top:1.5px solid "+LINE if n>1 else ""}">{iconcircle(icn)}'
                f'<div class="col" style="flex:1;gap:2px"><span class="b15" style="font-weight:700">{n}. {t}</span><span class="sm">{d}</span></div></div>')
    steps = card(st(1, 'id', 'Pièce d’identité', 'Passeport, permis de conduire ou carte de résident permanent') + st(2, 'camera', 'Égoportrait', 'Une courte vidéo pour confirmer que c’est bien vous') + st(3, 'shield', 'Résultat', 'En général en moins de 5 minutes'), 'padding:4px 14px;margin-top:14px')
    why = f'<div class="row" style="gap:8px;flex:none;margin-top:12px;flex-wrap:wrap">{status("Requis avant le 1er envoi ou voyage", "teal")}{status("≈ 3 minutes", "mute", False)}</div>'
    stripe = (f'<div class="row" style="gap:10px;flex:none;margin-top:12px;padding:10px 12px;border-radius:14px;background:#EEEAF9;border:1.5px solid #C9C2EE">{ic("lock", "#4B42C7", 18, 2.2)}'
              f'<span style="font:400 13px/18px Inter;color:{INK}">Vérification hébergée par <b>Stripe Identity</b>. Volis reçoit seulement le résultat, jamais vos images.</span></div>')
    body = f'{top}{art}{h1("Vérifions votre identité", "C’est ce qui rend Volis sûr : chaque voyageur et chaque expéditeur est vérifié.", 2)}{why}{steps}{stripe}<div class="sp"></div>{btn("Commencer")}'
    return pg(body, None, blob(5, 300, 200, 120, '#BFE3DB', .5))
# ---------- 18 Consentement exprès biométrique
def verif_consent():
    top = hdr('Votre consentement', SC, True, '', 'Étape requise · Loi 25 (Québec)')
    def it(icn, t, d):
        return f'<div class="row" style="gap:12px;align-items:flex-start;padding:9px 0">{iconcircle(icn, TSEL, "#0B5B55", 34, 17)}<div class="col" style="flex:1;gap:1px"><span style="font:700 14px/19px Inter">{t}</span><span style="font:400 13px/18px Inter;color:{T2}">{d}</span></div></div>'
    lst = card(it('camera', 'Ce qui est recueilli', 'Photo de votre pièce, égoportrait vidéo et un gabarit facial (donnée biométrique).')
               + it('shield', 'Pourquoi', 'Comparer votre visage à la photo de la pièce, pour prévenir la fraude et l’usurpation d’identité.')
               + it('globe', 'Qui le traite et où', 'Stripe, notre fournisseur, peut traiter ces données hors du Québec (ex. : États-Unis).')
               + it('clock', 'Combien de temps', 'Le gabarit est supprimé après la vérification. Volis garde seulement le résultat.')
               + it('logout', 'Vos droits', 'Retirer votre consentement en tout temps dans Réglages → Confidentialité.'), 'padding:4px 14px;margin-top:10px')
    alt = (f'<div class="row" style="gap:10px;flex:none;margin-top:10px;padding:10px 12px;border-radius:14px;background:{SAND}">{ic("info", INK, 18, 2.2)}'
           f'<span style="font:400 13px/18px Inter;color:{INK}">Vous préférez sans biométrie? <b style="color:#0B5B55;text-decoration:underline">Vérification manuelle</b> par notre équipe (2 à 3 jours).</span></div>')
    cons = (f'<div class="row" style="gap:12px;flex:none;margin-top:12px;align-items:flex-start;padding:12px;border-radius:14px;background:{CARD};border:2px solid {INK}">{box(False)}'
            f'<span style="font:500 14px/20px Inter">Je consens <b>expressément</b> à ce que Stripe recueille et compare mes données biométriques pour vérifier mon identité.</span></div>')
    foot = f'<div class="row xs" style="gap:6px;justify-content:center;font-weight:500;margin-top:8px">Case non cochée par défaut · <span style="color:{TEAL};text-decoration:underline">Politique de confidentialité</span></div>'
    body = f'{top}<div style="font:400 15px/21px Inter;color:{T2};margin-top:6px;flex:none">La vérification utilise votre visage. Voici exactement ce qui se passe.</div>{lst}{alt}{cons}<div class="sp"></div>{btn("Accepter et continuer vers Stripe", "disabled", "lock")}{foot}'
    return pg(body)
# ---------- 19 Stripe Identity (hébergé)
def verif_stripe():
    behind = f'{hdr("Vérification", SC, True)}'
    PUR = '#635BFF'
    idcard = (f'<div style="position:relative;height:250px;border-radius:16px;background:#1A1F36;overflow:hidden;flex:none;margin-top:14px">'
              f'<div class="abs" style="left:36px;right:36px;top:46px;height:156px;border-radius:14px;border:3px solid #fff;"></div>'
              f'<div class="abs" style="left:52px;top:62px;width:250px;height:124px;border-radius:10px;background:#E8E4D8;display:flex;gap:12px;padding:14px">'
              f'<div style="width:70px;height:92px;border-radius:6px;background:#C9C0AE"></div><div class="col" style="gap:8px;flex:1;padding-top:6px"><i style="height:9px;width:90%;background:#A39B8A;border-radius:4px"></i><i style="height:9px;width:70%;background:#B9B09E;border-radius:4px"></i><i style="height:9px;width:80%;background:#B9B09E;border-radius:4px"></i><i style="height:9px;width:50%;background:#B9B09E;border-radius:4px"></i></div></div>'
              f'<div class="abs" style="left:0;right:0;bottom:16px;text-align:center;font:600 14px/18px Inter;color:#fff">Placez le recto de votre pièce dans le cadre</div></div>')
    inner = (f'<div class="row" style="height:44px;flex:none;justify-content:space-between;border-bottom:1px solid #E3E8EE;margin:0 -16px;padding:0 16px">'
             f'<span style="font:600 16px/20px Inter;color:#0A66D8">Terminé</span><span class="row" style="gap:5px;font:500 14px/18px Inter;color:#1A1F36">{ic("lock", "#1A1F36", 13, 2.4)}verify.stripe.com</span><span style="font:600 15px/20px Inter;color:#0A66D8">aA</span></div>'
             f'<div class="row" style="gap:8px;margin-top:16px;flex:none"><span style="font:800 22px/1 Inter;color:{PUR};letter-spacing:-1px">stripe</span><span style="font:500 13px/18px Inter;color:#697386">Identity</span><span class="sp"></span><span style="font:500 13px/18px Inter;color:#697386">Étape 1 sur 2</span></div>'
             f'<div style="font:700 21px/28px Inter;color:#1A1F36;margin-top:14px;flex:none">Photographiez votre pièce d’identité</div>'
             f'<div style="font:400 14px/20px Inter;color:#425466;margin-top:4px;flex:none">Volis utilise Stripe pour vérifier votre identité. Vos images sont traitées par Stripe.</div>'
             f'{idcard}'
             f'<div class="row" style="gap:8px;margin-top:14px;flex:none">{"".join(f"<span style=\'height:36px;padding:0 12px;border-radius:18px;border:1.5px solid {"#635BFF" if i==0 else "#E3E8EE"};display:flex;align-items:center;font:600 13px/18px Inter;color:#1A1F36\'>{t}</span>" for i,t in enumerate(["Passeport","Permis","Carte RP"]))}</div>'
             f'<div class="row" style="height:52px;border-radius:8px;background:{PUR};color:#fff;font:600 16px/20px Inter;justify-content:center;margin-top:16px;flex:none">Prendre la photo</div>'
             f'<div class="row" style="gap:6px;justify-content:center;margin-top:12px;font:500 12px/16px Inter;color:#697386;flex:none">{ic("lock", "#697386", 12, 2.4)}Hébergé de façon sécurisée par Stripe</div>')
    tag = f'<div class="abs" style="left:16px;top:62px;z-index:45;background:{SAND};border:1.5px solid {INK};border-radius:10px;padding:5px 10px;font:700 12px/16px Inter;color:{INK}">Page externe Stripe (illustratif) — fermer ramène à Volis</div>'
    return pg(behind, None, '', CREAM, tag + sheet(inner, 96))
# ---------- 20-22 résultats
def verif_res(kind):
    top = hdr('', SC, False, f'<div class="ibtn">{ic("plus", INK, 20, 2.2).replace("<path", "<path transform=\'rotate(45 12 12)\'")}</div>')
    if kind == 'ok':
        icon = f'<div style="width:112px;height:112px;border-radius:56px;background:{SUCC_BG};display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 12px rgba(216,240,223,.5)">{ic("check", SUCC_FG, 56, 3)}</div>'
        t, d = 'Identité vérifiée!', 'Merci Camille. Votre profil affiche maintenant le badge « ID vérifiée ».'
        extra = card(f'<div class="row" style="justify-content:space-between"><span class="h2" style="font-size:16px">Niveau de confiance</span>{status("3 sur 4", "teal", False)}</div>'
                     f'<div class="row" style="gap:4px;margin:10px 0 8px">{"".join(f"<i style=\'flex:1;height:6px;border-radius:3px;background:{TEAL if j<3 else DIS}\'></i>" for j in range(4))}</div>'
                     f'<div class="row" style="gap:6px;flex-wrap:wrap">{vbadge("mail")}{vbadge("tel")}{vbadge("id")}<span class="badge" style="background:#EAE2D2;color:{T2}">{ic("plane", T2, 13, 2.2)}Vol : à confirmer</span></div>', 'padding:14px;margin-top:22px')
        extra += card(f'<div class="row" style="gap:12px">{iconcircle("plane", SAND, INK, 40, 20)}<div class="col" style="flex:1"><span class="b15" style="font-weight:700">Prochaine étape (voyageurs)</span><span class="sm">Confirmez un vol pour atteindre 4 sur 4 et être mis en avant.</span></div></div>', 'padding:12px 14px;margin-top:12px')
        cta = btn('Continuer mon envoi', 'primary', None)
        sub = f'<div class="row sm" style="justify-content:center;margin-top:10px">Vérifié le 12 nov. 2026 · 14 h 01</div>'
        art = illus('e-inscription', 120, 'position:absolute;right:6px;bottom:248px')
    elif kind == 'wait':
        icon = (f'<div style="width:112px;height:112px;border-radius:56px;background:{SAND};display:flex;align-items:center;justify-content:center;position:relative">{ic("clock", WARN_IC, 54, 2.4)}'
                f'<svg class="abs" style="inset:-10px" width="132" height="132" viewBox="0 0 132 132"><circle cx="66" cy="66" r="62" stroke="#E0A458" stroke-width="4" fill="none" stroke-dasharray="120 300" stroke-linecap="round"/></svg></div>')
        t, d = 'Vérification en cours', 'Stripe analyse vos documents. C’est souvent moins de 5 minutes, parfois jusqu’à 24 h.'
        extra = (card(f'<div class="col" style="gap:0">{listrow("bell", "On vous avertit dès que c’est prêt", "", True, INK, False, 46)}{listrow("package", "Vous pouvez préparer votre envoi", "", False, INK, False, 46)}{listrow("lock", "Le paiement attend la vérification", "", False, INK, False, 46)}</div>', 'padding:2px 14px;margin-top:22px'))
        extra += f'<div class="row" style="justify-content:center;gap:6px;flex:none;margin-top:14px">{ic("help", TEAL, 18)}<span class="link" style="min-height:44px">Ça prend plus de 24 h? Contactez-nous</span></div>'
        cta = btn('Retour à l’accueil', 'secondary')
        sub = f'<div class="row sm" style="justify-content:center;margin-top:10px">Soumis à 14 h 01 · réf. <span class="mono" style="margin-left:4px">vs_••••8K2</span></div>'
        art = ''
    else:
        icon = f'<div style="width:112px;height:112px;border-radius:56px;background:{ERR_BG};display:flex;align-items:center;justify-content:center">{ic("alert", ERR, 52, 2.4)}</div>'
        t, d = 'On n’a pas pu vérifier votre identité', 'Pas de panique, ça arrive. Voici les causes les plus fréquentes :'
        reasons = ''.join(f'<div class="row" style="gap:10px;min-height:36px">{ic(i_, ERR, 18, 2.2)}<span class="b15" style="font-weight:500;font-size:14.5px">{r}</span></div>' for i_, r in [('image', 'Photo floue ou reflets sur la pièce'), ('cal', 'Pièce d’identité expirée'), ('user', 'Visage partiellement caché')])
        extra = card(reasons, 'padding:8px 14px;margin-top:18px') + card(f'<span class="b15" style="font-weight:700">Conseils pour réussir</span><div class="sm" style="margin-top:4px;color:{INK}">Lumière naturelle · pièce posée à plat · sans étui · retirez lunettes et casquette.</div>', 'padding:12px 14px;margin-top:10px;background:#FFF7EE') + f'<div class="row" style="gap:6px;justify-content:center;flex:none;margin-top:10px">{status("Essai 1 sur 3", "mute", False)}</div>'
        cta = f'<div class="col" style="gap:8px;flex:none">{btn("Réessayer", "primary", "camera")}{btn("Demander une vérification manuelle", "ghost", None, 48)}</div>'
        sub = ''
        art = ''
    body = (f'{top}<div class="col" style="align-items:center;text-align:center;flex:none;margin-top:30px">{icon}'
            f'<div class="h1" style="margin-top:26px;font-size:25px;line-height:31px;max-width:330px">{t}</div><div style="font:400 15px/22px Inter;color:{T2};margin-top:8px;max-width:330px">{d}</div></div>{extra}<div class="sp"></div>{cta}{sub}')
    return pg(body, None, blob(9, 196, 250, 150, {'ok': '#BFE3DB', 'wait': '#FFE1B0', 'err': '#FFC4B2'}[kind], .45))
# ---------- 23 mot de passe oublié
def mdp():
    top = hdr('', SC, True)
    body = (f'{top}{h1("Mot de passe oublié?", "Entrez le courriel de votre compte. On vous envoie un lien pour en choisir un nouveau.", 8)}{sp(22)}'
            f'{field("Courriel", "camille.t@exemple.com", "mail", False, "focus")}{sp(14)}{btn("Envoyer le lien")}'
            f'<div class="row" style="justify-content:center;margin-top:8px;flex:none"><span class="link">Utiliser plutôt une clé d’accès</span></div>'
            f'<div class="sp"></div>{banner("info", "", "Pour votre sécurité, on ne confirme jamais si un courriel est associé à un compte.")}{sp(10)}'
            f'<div class="row" style="justify-content:center;gap:4px;flex:none" class="sm"><span class="sm">Vous vous en souvenez?</span><span class="link" style="font-size:14px">Se connecter</span></div>')
    kb = keyboard_alpha()
    return pg(body.replace('<div class="sp"></div>', sp(18), 1).replace(f'{banner("info", "", "Pour votre sécurité, on ne confirme jamais si un courriel est associé à un compte.")}{sp(10)}', ''), None, '', CREAM, kb)
def keyboard_alpha():
    rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    k = lambda c, w=33: f'<span style="width:{w}px;height:42px;border-radius:6px;background:#FFFFFF;box-shadow:0 1px 0 #8E8A80;display:flex;align-items:center;justify-content:center;font:400 21px/1 Inter;color:#000">{c}</span>'
    r1 = ''.join(k(c) for c in rows[0]); r2 = ''.join(k(c) for c in rows[1])
    r3 = k('⇧', 42).replace('#FFFFFF', '#ABA69C') + ''.join(k(c) for c in rows[2]) + k('⌫', 42).replace('#FFFFFF', '#ABA69C')
    r4 = k('123', 88).replace('#FFFFFF', '#ABA69C').replace('21px', '16px') + k('@', 40) + k('espace', 150).replace('21px', '16px') + k('.', 40) + k('OK', 88).replace('#FFFFFF', TEAL).replace('color:#000', 'color:#fff').replace('21px', '16px')
    rw = lambda r, pad=0: f'<div class="row" style="gap:5px;justify-content:center;padding:0 {pad}px">{r}</div>'
    return (f'<div class="abs" style="left:0;right:0;bottom:0;height:292px;background:#D8D3C8;z-index:39;padding:8px 3px 0;display:flex;flex-direction:column;gap:11px">'
            f'{rw(r1)}{rw(r2)}{rw(r3)}{rw(r4)}<div style="margin-top:auto;height:30px;display:flex;justify-content:center;align-items:center"><div style="width:134px;height:5px;border-radius:3px;background:#000"></div></div></div>')
# ---------- 24 lien envoyé
def mdp_ok():
    top = hdr('', SC, True)
    art = f'<div class="row" style="justify-content:center;flex:none;margin-top:6px">{illus("d-connexion", 210)}</div>'
    body = (f'{top}{art}<div class="col" style="align-items:center;text-align:center;flex:none;margin-top:14px"><div class="h1">Vérifiez vos courriels</div>'
            f'<div style="font:400 15px/22px Inter;color:{T2};margin-top:8px;max-width:320px">Si un compte existe pour <b style="color:{INK}">camille.t@exemple.com</b>, vous recevrez un lien valide 30 minutes.</div></div>'
            f'{sp(18)}{banner("info", "", "Pour votre sécurité, on ne confirme jamais si un courriel est associé à un compte. Pensez à vérifier vos indésirables.")}'
            f'<div class="sp"></div><div class="col" style="gap:8px;flex:none">{btn("Ouvrir mon application Courriel", "primary", "mail")}{btn("Renvoyer le lien dans 0:45", "disabled", None, 48)}</div>'
            f'<div class="row" style="justify-content:center;flex:none"><span class="link">Changer d’adresse</span></div>')
    return pg(body, None, blob(3, 196, 240, 150, '#BFE3DB', .5))
# ---------- 25 vérification téléphone SMS
def sms():
    top = hdr('', SC, True)
    cells = ''
    for i, d in enumerate('482   '):
        cur = i == 3
        cells += (f'<span style="width:48px;height:58px;border-radius:12px;background:{CARD};border:{2 if (d.strip() or cur) else 1.5}px solid {TEAL if cur else (INK if d.strip() else "#7E7A70")};{"box-shadow:0 0 0 4px #D6ECE8;" if cur else ""}display:flex;align-items:center;justify-content:center;font:700 28px/1 \'JetBrains Mono\';position:relative">'
                  f'{d.strip()}{"<i style=\'width:2px;height:28px;background:%s\'></i>" % TEAL if cur else ""}</span>')
        if i == 2: cells += f'<span style="width:10px;height:3px;background:#A39B8A;border-radius:2px;flex:none"></span>'
    code = f'<div class="row" style="gap:6px;justify-content:center;flex:none;margin-top:22px" aria-label="Code à 6 chiffres">{cells}</div>'
    body = (f'{top}{h1("Entrez le code reçu par texto", "Envoyé au <b style=\'color:#1E2A3A\'>+1 (514) 555-0123</b> · <span style=\'color:#0F766E;font-weight:600\'>Modifier</span>", 8)}{code}'
            f'<div class="row" style="justify-content:center;gap:6px;flex:none;margin-top:16px" class="sm"><span class="sm">Pas reçu?</span><span class="sm" style="font-weight:600">Renvoyer dans <span class="mono">0:32</span></span></div>'
            f'<div class="row" style="justify-content:center;flex:none"><span class="link" style="font-size:14px">Recevoir un appel à la place</span></div>')
    sug = (f'<div class="abs" style="left:0;right:0;bottom:292px;height:44px;background:#E2DDD2;z-index:39;display:flex;align-items:center;justify-content:center;border-top:1px solid #CFC9BD">'
           f'<span style="font:500 15px/20px Inter;color:#000">Depuis Messages</span><span style="font:600 15px/20px \'JetBrains Mono\';margin-left:8px;color:#000">482 913</span></div>')
    keys = [('1', ''), ('2', 'ABC'), ('3', 'DEF'), ('4', 'GHI'), ('5', 'JKL'), ('6', 'MNO'), ('7', 'PQRS'), ('8', 'TUV'), ('9', 'WXYZ'), ('', ''), ('0', ''), ('⌫', '')]
    kk = ''.join(f'<span style="height:46px;border-radius:6px;{"background:#fff;box-shadow:0 1px 0 #8E8A80;" if n not in ("", "⌫") else ""}display:flex;flex-direction:column;align-items:center;justify-content:center;color:#000">'
                 f'<b style="font:400 24px/26px Inter">{n}</b><i style="font:600 9px/10px Inter;letter-spacing:2px;font-style:normal">{l}</i></span>' for n, l in keys)
    kb = (f'<div class="abs" style="left:0;right:0;bottom:0;height:292px;background:#D8D3C8;z-index:39;padding:6px 6px 0">'
          f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:7px">{kk}</div><div style="position:absolute;bottom:8px;left:0;right:0;display:flex;justify-content:center"><div style="width:134px;height:5px;border-radius:3px;background:#000"></div></div></div>')
    note_ = f'<div class="abs" style="left:16px;right:16px;bottom:350px;z-index:5">{banner("teal", "", "Le code remplit le champ automatiquement. On vérifie votre numéro une seule fois; il reste masqué pour les autres membres.")}</div>'
    return pg(body, None, '', CREAM, note_ + sug + kb)
FA = [('17-verif-identite-intro', verif_intro), ('18-verif-identite-consentement-biometrique', verif_consent), ('19-verif-identite-stripe', verif_stripe),
      ('20-verif-identite-verifiee', lambda: verif_res('ok')), ('21-verif-identite-en-attente', lambda: verif_res('wait')), ('22-verif-identite-echec', lambda: verif_res('err')),
      ('23-mot-de-passe-oublie', mdp), ('24-mot-de-passe-lien-envoye', mdp_ok), ('25-verif-telephone-sms', sms)]
