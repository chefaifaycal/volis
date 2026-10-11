from kit import *
from fb import photo, person, kv
PART = 'Bouclier Assurances'
# ---------- 40 Assurance optionnelle (feuille depuis paiement)
def assurance():
    import screens as S
    base = upd_paiement(False)
    inner = (f'<div class="row" style="justify-content:space-between;height:44px;flex:none"><span class="h2" style="font-size:19px">Assurance colis (option)</span><div class="ibtn" style="width:36px;height:36px">{ic("plus", INK, 18, 2.2).replace("<path", "<path transform=\'rotate(45 12 12)\'")}</div></div>'
             f'<div class="row" style="gap:10px;flex:none"><div style="width:44px;height:44px;border-radius:12px;background:#E3ECF8;display:flex;align-items:center;justify-content:center;flex:none">{ic("shield", INFO_FG, 22, 2.2)}</div>'
             f'<div class="col" style="flex:1"><span class="b15" style="font-weight:700">Offerte par {PART}</span><span class="xs" style="font-weight:500">Assureur partenaire (fictif) · Volis agit comme intermédiaire</span></div></div>'
             + card(f'{kv("Valeur déclarée", "120,00 $")}{kv("Couverture", "<b>jusqu’à 120 $</b> (= valeur déclarée)")}{kv("Plafond par envoi", "1 000 $")}{kv("Prime (3 % de la valeur, min. 2 $)", "3,60 $")}', 'padding:8px 14px;margin-top:12px')
             + f'<div class="col" style="gap:6px;flex:none;margin-top:12px"><span class="lab">Couvert</span>'
             + ''.join(f'<div class="row" style="gap:8px">{ic("check", SUCC_FG, 16, 3)}<span class="sm" style="color:{INK}">{t}</span></div>' for t in ['Perte ou vol pendant le transport', 'Dommages constatés à la réception (photos)', 'Non-livraison confirmée après enquête'])
             + f'<span class="lab" style="margin-top:6px">Non couvert</span>'
             + ''.join(f'<div class="row" style="gap:8px">{ic("plus", ERR, 16, 2.6).replace("<path", "<path transform=\'rotate(45 12 12)\'")}<span class="sm" style="color:{INK}">{t}</span></div>' for t in ['Objets interdits ou mal déclarés', 'Saisie par la douane', 'Emballage insuffisant (objets fragiles)']) + '</div>'
             + f'<div class="row" style="gap:8px;flex:none;margin-top:10px;padding:10px 12px;border-radius:12px;background:{SAND}">{ic("info", INK, 16, 2.2)}<span class="xs" style="color:{INK};font-weight:500">Sans l’option : protection de base Volis incluse, jusqu’à 100 $.</span></div>'
             + f'<div class="xs" style="flex:none;margin-top:8px;font-weight:500"><span style="color:{TEAL};text-decoration:underline">Résumé de la police (PDF)</span> · Volis reçoit une commission de l’assureur.</div>'
             + f'<div class="row" style="gap:10px;flex:none;margin-top:12px">{btn("Sans assurance", "secondary", None, 52, "flex:1")}{btn("Ajouter · 3,60 $", "primary", None, 52, "flex:1.3")}</div>')
    return base.replace('</div></body>', sheet(inner, 120) + '</div></body>', 1)
# ---------- 10 & 11 mis à jour
def upd_creer():
    import screens as S
    h = S.creer_envoi(False)
    old = '<span class="lab">Valeur déclarée</span>'
    i = h.index(old); j = h.index('</div></div>', i) + len('</div></div>')
    seg_ = h[i:j]
    new = seg_[:-6] + f'<span class="row" style="gap:5px;font:500 13px/18px Inter;color:{T2}">{ic("info", T2, 14)}Maximum 1 000 $ · sert de plafond d’indemnisation</span></div>'
    h = h.replace(seg_, new, 1)
    h = h.replace('<span class="sm">Ouvert puis fermé. 1 à 4 photos.</span>', '<span class="sm">Ouvert, puis fermé. 1 à 4 photos.</span>')
    h = h.replace('Batteries au lithium en vrac, liquides de plus de 100 ml, médicaments sans ordonnance, argent comptant, aliments périssables, armes et substances illégales.', 'Batteries au lithium en vrac, liquides de plus de 100 ml, argent comptant, aliments périssables, armes, substances illégales. <b style="color:#0B5B55;text-decoration:underline">Voir la liste</b>')
    h = h.replace('{ch("Livres", False)}', '')
    return h
def upd_paiement(on=True):
    top = hdr('Paiement protégé', SC, True, '', 'Étape 4 sur 4')
    summ = card(f'<div class="row" style="gap:12px">{avatar("KB", 40)}<div class="col" style="flex:1;gap:2px"><span class="b15" style="font-weight:700">Karim B. <span class="t2" style="font-weight:500">· 4,9 ★</span></span>'
                f'<span class="sm"><b class="mono" style="color:{INK}">YUL → ALG</b> · ven. 14 nov. · 2,0 kg</span></div>{ic("chev", T2, 20)}</div>', 'padding:10px 14px;margin-top:6px')
    if on:
        ins = (f'<div class="row" style="flex:none;margin-top:10px;gap:12px;padding:12px 14px;border-radius:16px;background:#F1F5FB;border:2px solid {INFO_FG}">'
               f'{ic("shield", INFO_FG, 22, 2.2)}<div class="col" style="flex:1;gap:1px"><span class="b15" style="font-weight:700">Assurance ajoutée · 3,60 $</span>'
               f'<span class="xs" style="font-weight:500">Couvre 120 $ (valeur déclarée) · {PART} · <span style="color:{INFO_FG};text-decoration:underline">Détails</span></span></div>{toggle(True)}</div>')
    else:
        ins = (f'<div class="row" style="flex:none;margin-top:10px;gap:12px;padding:12px 14px;border-radius:16px;background:{CARD};border:1.5px solid #CFC4AF">'
               f'{ic("shield", INFO_FG, 22, 2.2)}<div class="col" style="flex:1;gap:1px"><span class="b15" style="font-weight:700">Assurer mon colis? (option)</span>'
               f'<span class="xs" style="font-weight:500">3,60 $ · couvre jusqu’à la valeur déclarée · <span style="color:{INFO_FG};text-decoration:underline">Détails</span></span></div>{toggle(False)}</div>')
    if on:
        fees = card(f'{rowkv("Transport (2 kg × 12 $)", "24,00 $")}{rowkv("Frais de service Volis (15 %)", "3,60 $")}{rowkv("Assurance colis (option)", "3,60 $")}{rowkv("Taxes (TPS, TVQ, taxe sur prime)", "0,86 $")}'
                    f'<div style="border-top:1.5px solid {LINE};margin:4px 0"></div>{rowkv("Total", "32,06 $", True)}', 'padding:6px 14px 4px;margin-top:10px')
    else:
        fees = card(f'{rowkv("Transport (2 kg × 12 $)", "24,00 $")}{rowkv("Frais de service Volis (15 %)", "3,60 $")}{rowkv("Taxes (TPS, TVQ sur les frais)", "0,54 $")}'
                    f'<div style="border-top:1.5px solid {LINE};margin:4px 0"></div>{rowkv("Total", "28,14 $", True)}', 'padding:6px 14px 4px;margin-top:10px')
    tot = '32,06' if on else '28,14'
    esc = (f'<div class="row" style="flex:none;margin-top:10px;gap:10px;padding:10px 12px;border-radius:16px;background:{MINT}">{ic("lock", "#0B5B55", 20, 2.2)}'
           f'<span style="font:400 13px/18px Inter;color:{INK}"><b style="color:#0B5B55">Séquestre :</b> vous payez maintenant, les fonds sont bloqués et libérés au voyageur seulement après la remise au destinataire.</span></div>')
    def pm(icn_html, label, sub, on):
        return (f'<div class="row" style="gap:12px;height:54px;padding:0 14px;border-radius:14px;background:{CARD};border:{2 if on else 1.5}px solid {TEAL if on else "#CFC4AF"}">'
                f'{icn_html}<div class="col" style="flex:1"><span class="b15" style="font-weight:700">{label}</span><span class="xs" style="font-weight:500">{sub}</span></div>{radio(on)}</div>')
    ap = f'<span style="width:44px;height:30px;border-radius:6px;background:{INK};display:flex;align-items:center;justify-content:center;gap:2px;color:#fff;font:600 12px/1 Inter">{I0["apple"]("#fff", 13)}Pay</span>'
    vc = f'<span style="width:44px;height:30px;border-radius:6px;background:#E9DFCC;display:flex;align-items:center;justify-content:center">{ic("card", INK, 20)}</span>'
    pms = f'<div class="col" style="gap:8px;flex:none;margin-top:10px"><span class="lab">Moyen de paiement</span>{pm(ap, "Apple Pay", "Visa •••• 4242", True)}{pm(vc, "Carte de crédit ou débit", "Ajouter une carte", False)}</div>'
    cta = (f'<div class="col" style="gap:6px;flex:none"><div class="cta" style="background:{INK}">{I0["apple"]("#fff", 18)}Payer {tot} $</div>'
           f'<div class="row xs" style="gap:6px;justify-content:center;font-weight:500">{ic("lock", T2, 13)}Remboursement intégral si le colis n’est pas remis.</div></div>')
    return pg(f'{top}{summ}{ins}{fees}{esc}{pms}<div class="sp" style="min-height:8px"></div>{cta}')
# ---------- 41 Versements
def versements():
    top = hdr('Versements', SC, True, f'<div class="ibtn">{ic("help", INK, 20)}</div>')
    bal = (f'<div style="flex:none;margin-top:6px;padding:16px;border-radius:20px;background:{INK};color:#fff">'
           f'<span class="row" style="gap:8px;font:700 14px/18px Inter;color:#E6EEF5">{ic("wallet", "#E6EEF5", 18)}Solde disponible</span>'
           f'<div style="font:800 36px/42px \'Plus Jakarta Sans\';margin-top:6px">145,00 $</div>'
           f'<div class="row" style="gap:6px;margin-top:6px;font:500 13px/18px Inter;color:#C9D3DE">{ic("bank", "#C9D3DE", 15)}Desjardins •••• 6789 · géré par Stripe</div></div>')
    def opt(on, t, d, fee):
        return (f'<div class="row" style="gap:12px;padding:12px 14px;border-radius:16px;background:{CARD};border:{2 if on else 1.5}px solid {TEAL if on else "#CFC4AF"};flex:none">{radio(on)}'
                f'<div class="col" style="flex:1"><span class="b15" style="font-weight:700">{t}</span><span class="xs" style="font-weight:500">{d}</span></div><b style="font:700 14px/18px Inter;color:{INK}">{fee}</b></div>')
    ch = (f'<div class="col" style="gap:8px;flex:none;margin-top:12px"><span class="lab">Choisir le type de virement</span>'
          + opt(True, 'Standard', '2 à 3 jours ouvrables', 'Gratuit') + opt(False, 'Instantané', 'En quelques minutes · 1,5 % (min. 0,50 $)', '2,18 $') + '</div>')
    def h(t, d, a, s):
        return f'<div class="row" style="gap:12px;min-height:56px;border-top:1.5px solid {LINE}"><div class="col" style="flex:1"><span class="b15" style="font-weight:600">{t}</span><span class="xs" style="font-weight:500">{d}</span></div><div class="col" style="align-items:flex-end;gap:3px"><b style="font:700 15px/20px Inter">{a}</b>{s}</div></div>'
    hist = (f'<div style="flex:none;margin-top:12px">{sect("Historique", SC)}</div>' + card(
        h('Virement standard', 'Demandé le 10 nov. · arrivée prévue 13 nov.', '60,00 $', status('En cours', 'warn')).replace('border-top:1.5px solid ' + LINE, '', 1)
        + h('Virement instantané', '2 nov. · frais 0,90 $', '59,10 $', status('Déposé', 'ok'))
        + h('Envoi VL-4821 · Camille T.', 'Libéré après la livraison', '24,00 $', status('En séquestre', 'teal')), 'padding:2px 14px;margin-top:4px'))
    cta = f'<div class="col" style="gap:4px;flex:none">{btn("Virer 145,00 $")}<div class="row" style="justify-content:center"><span class="link" style="font-size:14px">Modifier mon compte bancaire sur Stripe ↗</span></div></div>'
    return pg(f'{top}{bal}{ch}{hist}<div class="sp" style="min-height:8px"></div>{cta}', None)
# ---------- 42 Configurer les versements avec Stripe
def stripe_payout():
    top = hdr('Recevoir mes gains', SC, True)
    art = f'<div class="row" style="justify-content:center;flex:none;margin-top:4px">{illus("a-voyageur", 150)}</div>'
    t = h1('Configurez vos versements', 'Pour recevoir l’argent de vos voyages, ajoutez votre compte bancaire chez notre partenaire de paiement.', 8, 25)
    def st(n, t_, d):
        return f'<div class="row" style="gap:12px;align-items:flex-start;min-height:52px;padding-top:8px;{"border-top:1.5px solid "+LINE if n>1 else ""}"><span style="width:26px;height:26px;border-radius:13px;background:{TSEL};color:#0B5B55;font:800 13px/26px Inter;text-align:center;flex:none">{n}</span><div class="col" style="flex:1"><span class="b15" style="font-weight:700">{t_}</span><span class="sm">{d}</span></div></div>'
    steps = card(st(1, 'Vous êtes redirigé vers Stripe', 'Page sécurisée hébergée par Stripe') + st(2, 'Identité et compte bancaire', 'Saisis directement chez Stripe, pas dans Volis') + st(3, 'Retour automatique dans Volis', 'Vos gains sont versés après chaque livraison'), 'padding:4px 14px 8px;margin-top:14px')
    priv = (f'<div class="row" style="gap:10px;flex:none;margin-top:12px;padding:10px 12px;border-radius:14px;background:#EEEAF9;border:1.5px solid #C9C2EE">{ic("lock", "#4B42C7", 18, 2.2)}'
            f'<span style="font:400 13px/18px Inter;color:{INK}">Volis ne voit jamais vos coordonnées bancaires. Elles sont gérées par <b>Stripe Connect</b>.</span></div>')
    cta = (f'<div class="col" style="gap:4px;flex:none"><div class="cta" style="background:#635BFF;font-size:16px;gap:6px">Configurer mes versements avec Stripe {ic("share", "#fff", 16, 2.2).replace("<path", "<path transform=\'rotate(45 12 12)\'")}</div>'
           f'<div class="row" style="justify-content:center"><span class="link" style="font-size:14px">Plus tard</span></div></div>')
    return pg(f'{top}{art}{t}{steps}{priv}<div class="sp"></div>{cta}', None, blob(2, 196, 170, 110, '#BFE3DB', .5))
# ---------- 43 Ajouter un destinataire
def destinataire():
    top = hdr('Destinataire', SC, True, '', 'Envoi VL-4821 · YUL → ALG')
    f1 = field('Prénom et nom', 'Amina Kaci', 'user')
    f2 = (f'<div class="fld" style="flex:none"><span class="lab">Téléphone</span><div class="row" style="gap:8px"><div class="inp" style="width:122px;gap:6px;padding:0 10px"><span style="font-weight:600;white-space:nowrap">DZ +213</span>{ic("down", INK, 14)}</div>'
          f'<div class="inp" style="flex:1;border:2px solid {TEAL};box-shadow:0 0 0 4px #D6ECE8">5 55 12 34 56</div></div><span class="xs" style="font-weight:500">Sert à recevoir le lien de suivi et le code de réception.</span></div>')
    f3 = field('Ville de réception', 'Alger · Bab Ezzouar', 'pin')
    rel = f'<div class="fld" style="flex:none"><span class="lab">Lien avec vous (facultatif)</span><div class="row" style="gap:6px">{chip("Famille", True)}{chip("Ami·e")}{chip("Moi-même")}{chip("Autre")}</div></div>'
    link = card(f'<div class="row" style="gap:10px">{iconcircle("share", PEACH, INK, 40, 19)}<div class="col" style="flex:1"><span class="b15" style="font-weight:700">Lien de suivi</span><span class="mono" style="font:600 13px/18px \'JetBrains Mono\';color:{TEAL}">volis.app/s/7KQ2-48</span></div>'
                f'<span class="row" style="height:36px;padding:0 12px;border-radius:18px;border:1.5px solid {TEAL};color:{TEAL};font:700 13px/18px Inter;gap:4px">Copier</span></div>'
                f'<div class="row" style="min-height:44px;gap:10px;margin-top:4px;border-top:1.5px solid {LINE}"><span class="b15" style="flex:1;font-weight:500">Envoyer par texto à Amina</span>{toggle(True)}</div>'
                f'<div class="xs" style="font-weight:500">Amina voit le statut et l’heure d’arrivée, sans compte. Le nom complet du voyageur reste masqué.</div>', 'padding:12px 14px')
    return pg(f'{top}<div class="col" style="gap:12px;flex:none;margin-top:6px">{f1}{f2}{f3}{rel}{link}</div><div class="sp"></div>{btn("Enregistrer et partager")}')
# ---------- 44 Centre d'aide
def aide():
    top = hdr('Aide et sécurité', SC, True)
    srch = f'<div class="inp" style="flex:none;margin-top:6px;border-radius:25px;border-color:#B9B09E">{ic("search", T2, 18)}<span style="color:#6F6A60;font-weight:400">Rechercher (ex. : remboursement)</span></div>'
    cats = [('package', 'Envoyer', PEACH), ('plane', 'Voyager', MINT), ('lock', 'Paiement et séquestre', '#E3ECF8'), ('shield', 'Sécurité', SAND), ('alert', 'Litiges', '#FDE7E4'), ('user', 'Mon compte', '#EAE2D2')]
    grid = '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;flex:none;margin-top:12px">' + ''.join(
        f'<div class="col" style="height:92px;border-radius:16px;background:{b};padding:10px;justify-content:space-between">{ic(i_, INK, 22)}<span style="font:700 13px/16px Inter">{t}</span></div>' for i_, t, b in cats) + '</div>'
    arts = card(listrow('help', 'Que se passe-t-il si mon vol est annulé?', '', True) + listrow('help', 'Quand le voyageur est-il payé?') + listrow('help', 'Comment fonctionne la vérification d’identité?')
                + listrow('alert', 'Objets interdits et règles douanières', '', False, ERR_FG), 'padding:0 14px;margin-top:4px')
    contact = (f'<div class="row" style="gap:10px;flex:none;margin-top:12px">{btn("Écrire au soutien", "secondary", "chat", 48, "flex:1")}'
               f'{btn("Urgence sécurité", "danger2", "alert", 48, "flex:1")}</div><div class="row xs" style="justify-content:center;margin-top:6px;flex:none;font-weight:500">Réponse moyenne : 2 h · 7 j sur 7 · français, anglais, arabe</div>')
    return pg(f'{top}{srch}{grid}<div style="flex:none;margin-top:12px">{sect("Questions fréquentes", SC)}</div>{arts}{contact}', 4)
# ---------- 45 Objets interdits
def interdits():
    top = hdr('Objets interdits', SC, True, '', 'Règles Volis + règles du pays d’arrivée')
    def it(icn, t, d, c=ERR, bg=ERR_BG):
        return f'<div class="row" style="gap:12px;min-height:52px;padding:6px 0;border-top:1.5px solid {LINE}">{iconcircle(icn, bg, c, 36, 18)}<div class="col" style="flex:1"><span class="b15" style="font-weight:600;font-size:14.5px">{t}</span><span class="xs" style="font-weight:500">{d}</span></div></div>'
    no = card(f'<div class="row" style="gap:8px;padding:10px 0 6px">{status("Toujours interdit", "err")}</div>'
              + it('bolt', 'Batteries au lithium en vrac, cigarettes électroniques', 'Risque d’incendie en soute')
              + it('drop', 'Liquides inflammables, aérosols, parfums &gt; 100 ml', 'Règles de l’aviation civile')
              + it('dollar', 'Argent comptant, cartes-cadeaux, bijoux de valeur', 'Non assurable')
              + it('leaf', 'Cannabis, drogues, médicaments sans ordonnance', 'Illégal à l’arrivée, même si légal au Canada')
              + it('alert', 'Armes, répliques, objets tranchants', ''), 'padding:0 14px 4px;margin-top:6px')
    cond = card(f'<div class="row" style="gap:8px;padding:10px 0 6px">{status("Sous conditions", "warn")}</div>'
                + it('doc', 'Médicaments avec ordonnance', 'Copie de l’ordonnance + emballage d’origine', WARN_IC, WARN_BG)
                + it('cookie', 'Aliments secs scellés', 'Emballage commercial non ouvert', WARN_IC, WARN_BG)
                + it('bolt', 'Électronique avec batterie intégrée', 'Déclarée, éteinte, max. 2 appareils', WARN_IC, WARN_BG), 'padding:0 14px 4px;margin-top:10px')
    tip = f'<div class="row sm" style="gap:6px;flex:none;margin-top:10px">{ic("info", T2, 15)}En cas de doute, le voyageur peut refuser le colis.</div>'
    return pg(f'{top}{no}{cond}{tip}', None)
# ---------- 46 Réglages
def reglages():
    top = hdr('Réglages', SC, True)
    def grp(t, rows): return f'<div class="xs" style="margin-top:12px;flex:none;letter-spacing:.5px">{t}</div>' + card(rows, 'padding:0 14px;margin-top:6px')
    g1 = grp('PRÉFÉRENCES', listrow('globe', 'Langue', 'Français (Canada)', True, INK, True, 48) + listrow('dollar', 'Devise', '$ CA', False, INK, True, 48) + listrow('bell', 'Notifications', 'Texto, push', False, INK, True, 48))
    g2 = grp('PAIEMENT', listrow('card', 'Moyens de paiement', 'Apple Pay', True, INK, True, 48) + listrow('bank', 'Versements', 'via Stripe', False, INK, True, 48))
    g3 = grp('CONFIDENTIALITÉ ET SÉCURITÉ', listrow('lock', 'Clé d’accès et mot de passe', '', True, INK, True, 48) + listrow('shield', 'Consentements (biométrie)', 'Accordé', False, INK, True, 48)
             + listrow('user', 'Visibilité du profil', 'Membres', False, INK, True, 48) + listrow('doc', 'Télécharger mes données', '', False, INK, True, 48))
    g4 = card(listrow('logout', 'Se déconnecter', '', True, INK, False, 48) + listrow('alert', 'Supprimer mon compte', '', False, ERR, True, 48), 'padding:0 14px;margin-top:12px')
    v = f'<div class="row xs" style="justify-content:center;margin-top:10px;flex:none;font-weight:500">Volis 1.0 (42) · Conditions · Confidentialité</div>'
    return pg(f'{top}{g1}{g2}{g3}{g4}{v}', None)
# ---------- 47 Supprimer mon compte (étape 1)
def supprimer():
    top = hdr('Supprimer mon compte', SC, True)
    blk = banner('warn', 'Avant de supprimer', 'Vous avez 1 envoi en cours (VL-4821) et 145,00 $ de solde. Terminez l’envoi et virez votre solde d’abord.')
    def it(icn, t, c=INK): return f'<div class="row" style="gap:10px;min-height:40px">{ic(icn, c, 18, 2.2)}<span class="sm" style="color:{INK};flex:1">{t}</span></div>'
    what = card(f'<span class="b15" style="font-weight:700">Ce qui sera supprimé</span>' + it('user', 'Profil, photo, avis rédigés (anonymisés)') + it('chat', 'Messages et préférences') + it('id', 'Résultat de vérification d’identité'), 'padding:12px 14px;margin-top:12px')
    keep = card(f'<span class="b15" style="font-weight:700">Ce qu’on doit conserver</span>' + it('doc', 'Reçus et transactions : 6 ans (obligations fiscales)', T2) + it('alert', 'Dossiers de litige ouverts, jusqu’à leur fermeture', T2), 'padding:12px 14px;margin-top:10px')
    why = f'<div class="fld" style="flex:none;margin-top:12px"><span class="lab">Pourquoi partez-vous? (facultatif)</span><div class="row" style="gap:6px;flex-wrap:wrap">{chip("Je n’en ai plus besoin")}{chip("Trop cher")}{chip("Autre compte", True)}{chip("Autre")}</div></div>'
    cta = f'<div class="col" style="gap:4px;flex:none">{btn("Continuer la suppression", "danger2")}<div class="row" style="justify-content:center"><span class="link">Garder mon compte</span></div></div>'
    return pg(f'{top}{blk}{what}{keep}{why}<div class="sp"></div>{cta}', None)
# ---------- 48 Confirmation suppression (modale)
def supprimer_conf():
    base = reglages()
    modal = (f'<div class="abs" style="inset:0;background:rgba(20,28,40,.5);z-index:40"></div>'
             f'<div class="abs" style="left:20px;right:20px;top:200px;z-index:41;background:{CARD};border-radius:24px;padding:20px;box-shadow:0 20px 50px rgba(20,28,40,.35);display:flex;flex-direction:column">'
             f'<div style="width:52px;height:52px;border-radius:26px;background:{ERR_BG};display:flex;align-items:center;justify-content:center;align-self:center">{ic("alert", ERR, 26, 2.2)}</div>'
             f'<div class="h2" style="font-size:20px;line-height:26px;text-align:center;margin-top:12px">Supprimer définitivement?</div>'
             f'<div style="font:400 14px/20px Inter;color:{T2};text-align:center;margin-top:6px">Cette action est irréversible. Vous recevrez un courriel de confirmation; vous avez 30 jours pour changer d’idée.</div>'
             f'<div class="fld" style="margin-top:14px"><span class="lab">Tapez SUPPRIMER pour confirmer</span><div class="inp" style="border:2px solid {ERR}"><span class="mono" style="font-weight:700">SUPPRIMER</span><span class="sp"></span>{ic("check", ERR, 18, 3)}</div></div>'
             f'<div class="col" style="gap:8px;margin-top:16px">{btn("Supprimer mon compte", "danger", None, 52)}{btn("Annuler", "secondary", None, 48)}</div></div>')
    return base.replace('</div></body>', modal + '</div></body>', 1)
# ---------- 49 Attestation douane renforcée (voyageur)
def douane():
    top = hdr('Avant d’accepter le colis', SC, True, '', 'Remise de Camille T. · VL-4821')
    warn = (f'<div class="row" style="gap:12px;flex:none;margin-top:6px;padding:14px;border-radius:16px;background:{INK};color:#fff;align-items:flex-start">{ic("shield", "#FFD3C4", 24, 2.2)}'
            f'<div class="col" style="gap:4px"><span style="font:800 16px/21px \'Plus Jakarta Sans\'">Vous êtes responsable de ce que vous transportez</span>'
            f'<span style="font:400 13px/18px Inter;color:#D5DCE4">À la douane, c’est votre valise. Inspectez le colis et refusez au moindre doute; aucune pénalité.</span></div></div>')
    decl = card(f'<div class="row" style="justify-content:space-between"><span class="b15" style="font-weight:700">Contenu déclaré</span><span class="xs mono">2,0 kg</span></div>'
                f'<div class="sm" style="color:{INK};margin-top:4px">3 chandails, 1 foulard, 1 boîte de chocolats scellée (cadeau)</div>'
                f'<div class="row" style="gap:8px;margin-top:8px">{photo(56)}{photo(56).replace("#E9DFCC", "#E2D5BE")}<span class="xs" style="font-weight:500;flex:1">Photos de l’expéditeur · valeur déclarée 120 $</span></div>', 'padding:12px 14px;margin-top:10px')
    rows = (checkrow('J’ai vu le contenu, ouvert devant moi') + checkrow('Il correspond à la déclaration') + checkrow('Aucun objet interdit ni emballage suspect')
            + checkrow('Je déclarerai ces articles à la douane d’arrivée si requis', False))
    chk = card(rows, 'padding:6px 14px;margin-top:10px')
    info = f'<div class="row sm" style="gap:6px;flex:none;margin-top:10px">{ic("info", T2, 15)}<span>Algérie : cadeaux personnels tolérés; quantités commerciales taxées. <span style="color:{TEAL};font-weight:600">En savoir plus</span></span></div>'
    cta = f'<div class="row" style="gap:10px;flex:none">{btn("Refuser", "danger2", None, 56, "flex:1")}{btn("J’accepte le colis", "disabled", None, 56, "flex:1.6")}</div>'
    return pg(f'{top}{warn}{decl}{chk}{info}<div class="sp"></div>{cta}', None)
# ---------- 50 Live Activity écran verrouillé
def live():
    wall = (f'<div class="abs" style="inset:0;background:linear-gradient(170deg,#0F766E 0%,#0B5B55 55%,#1E2A3A 100%)"></div>'
            f'<div class="abs" style="left:0;top:0;opacity:.5">{blobsvg(393,852,[(3,320,640,170,"#FF7A59",.35),(7,60,520,140,"#DCEFEA",.18)])}</div>')
    di = (f'<div class="abs" style="left:50%;top:11px;transform:translateX(-50%);width:150px;height:37px;border-radius:19px;background:#000;z-index:10;display:flex;align-items:center;justify-content:space-between;padding:0 10px">'
          f'{appicon(22)}<span style="font:700 13px/1 \'JetBrains Mono\';color:#9FE3D8">2 h 10</span></div>')
    clock = (f'<div class="col" style="align-items:center;color:#fff;margin-top:40px;flex:none"><span class="row" style="gap:6px;font:600 17px/22px Inter;color:#E6EEF5">{ic("lock", "#E6EEF5", 15, 2.4)}vendredi 14 novembre</span>'
             f'<span style="font:700 96px/100px \'Plus Jakarta Sans\';letter-spacing:-3px;color:#F5F1E8">9:41</span></div>')
    prog = (f'<div style="position:relative;height:24px;margin-top:12px"><div class="abs" style="left:0;right:0;top:11px;height:4px;border-radius:2px;background:rgba(255,255,255,.25)"></div>'
            f'<div class="abs" style="left:0;width:58%;top:11px;height:4px;border-radius:2px;background:#FF7A59"></div>'
            f'<span class="abs" style="left:58%;top:0;transform:translateX(-50%) rotate(45deg)">{ic("plane", "#fff", 22, 2.2)}</span></div>')
    la = (f'<div style="flex:none;margin-top:auto;margin-bottom:12px;padding:14px 16px;border-radius:26px;background:rgba(14,22,32,.62);backdrop-filter:blur(20px);color:#fff">'
          f'<div class="row" style="gap:10px">{appicon(36)}<div class="col" style="flex:1"><span style="font:700 15px/19px Inter">Colis embarqué · <span class="mono">AT 201</span></span><span style="font:500 13px/17px Inter;color:#C9D3DE">Karim B. transporte VL-4821</span></div>'
          f'<div class="col" style="align-items:flex-end"><span style="font:800 18px/22px \'Plus Jakarta Sans\'">21 h 40</span><span style="font:500 11px/14px Inter;color:#C9D3DE">arrivée</span></div></div>'
          f'<div class="row" style="justify-content:space-between;margin-top:10px"><b class="mono" style="font:700 15px/1 \'JetBrains Mono\'">YUL</b><span style="font:600 12px/1 Inter;color:#9FE3D8">À l’heure · 2 h 10 restantes</span><b class="mono" style="font:700 15px/1 \'JetBrains Mono\'">ALG</b></div>{prog}</div>')
    notif = (f'<div class="row" style="flex:none;gap:10px;padding:12px 14px;border-radius:22px;background:rgba(245,241,232,.82);backdrop-filter:blur(20px);margin-bottom:14px">{appicon(36)}'
             f'<div class="col" style="flex:1"><div class="row" style="justify-content:space-between"><span style="font:700 14px/18px Inter;color:{INK}">Volis</span><span style="font:500 12px/16px Inter;color:{T2}">il y a 5 min</span></div>'
             f'<span style="font:400 14px/19px Inter;color:{INK}">Paiement sécurisé : 32,06 $ restent en séquestre jusqu’à la livraison.</span></div></div>')
    bot = (f'<div class="row" style="justify-content:space-between;flex:none;padding:0 30px;margin-bottom:6px">'
           + ''.join(f'<div style="width:50px;height:50px;border-radius:25px;background:rgba(14,22,32,.5);display:flex;align-items:center;justify-content:center">{ic(i_, "#fff", 22)}</div>' for i_ in ('bolt', 'camera')) + '</div>')
    lab = f'<div class="abs" style="left:16px;top:300px;z-index:9;background:{SAND};border:1.5px solid {INK};border-radius:10px;padding:5px 10px;font:700 12px/16px Inter;color:{INK};transform:rotate(-2deg)">Live Activity iOS · îlot dynamique + écran verrouillé</div>'
    h = page(False, f'<div class="ct" style="padding-top:0">{clock}{la}{notif}{bot}</div>', None, wall + di + lab, '#0B5B55')
    h = h.replace(f'color:{INK}"><span class="t">9:41</span>', 'color:#fff"><span class="t" style="visibility:hidden">9:41</span>', 1)
    for k in ('signal', 'wifi', 'battery'): h = h.replace(I0[k](INK), I0[k]('#fff'))
    h = h.replace(f'<div class="hi" style="background:transparent"><div style="background:{INK}">', '<div class="hi" style="background:transparent"><div style="background:#fff">')
    h = h.replace('class="sb" style="color:', 'class="sb" style="padding-left:30px;padding-right:22px;color:', 1)
    return h
FD = [('10-creer-envoi', upd_creer), ('11-paiement-protege', upd_paiement), ('40-assurance-optionnelle', assurance), ('41-versements', versements), ('42-versements-configurer-stripe', stripe_payout),
      ('43-ajouter-destinataire', destinataire), ('44-centre-aide', aide), ('45-objets-interdits', interdits), ('46-reglages', reglages),
      ('47-supprimer-compte', supprimer), ('48-supprimer-compte-confirmation', supprimer_conf), ('49-attestation-douane-voyageur', douane), ('50-live-activity-ecran-verrouille', live)]
