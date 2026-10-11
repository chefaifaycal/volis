---
title: "Cahier des charges — Application Volis"
subtitle: "Version 1.0 · 11 octobre 2026 · préparé pour Faycal Chefai"
lang: fr-CA
---

> **Avertissement.** Ce cahier des charges est un document de travail préparé pour Faycal Chefai. Les passages juridiques, fiscaux et financiers sont une **synthèse informative** : ils ne constituent ni un avis juridique, ni un avis fiscal, ni un avis financier. Ils doivent être validés par un avocat membre du Barreau du Québec, et par un comptable pour la fiscalité, avant le lancement. Les informations sur des services tiers (Stripe, Supabase, Expo, Apple, Google) reflètent leur documentation à la date du document et peuvent changer. Les montants, taux et délais cités en exemple ne sont pas des engagements.

# Introduction

## Objet du document

Ce cahier des charges décrit l’application **Volis** (nom de travail) : une plateforme de mise en relation entre des **expéditeurs** qui veulent faire livrer un colis à l’étranger et des **voyageurs** vérifiés qui ont de la place dans leurs bagages sur un vol. Le paiement est retenu (séquestre) jusqu’à la remise au destinataire. Le document sert de référence commune pour la conception, le développement, l’estimation et la validation juridique de la première version de l’application (iOS, Android et web).

## Contexte

- **Porteur du projet :** Faycal Chefai (Trois-Rivières, Québec).
- **Marché de départ :** diaspora installée au Québec qui envoie des colis vers sa famille (premiers corridors illustrés : Montréal YUL → Alger ALG, Tlemcen, Oran, Casablanca). Le service s’adresse aux particuliers (consommateurs au sens de la LPC).
- **Promesse :** un envoi plus rapide et moins cher que les transporteurs, avec trois garanties visibles : identité vérifiée (Stripe Identity), paiement retenu jusqu’à la livraison (Stripe Connect) et preuves de remise horodatées.
- **Plateformes :** application mobile Expo / React Native (iOS, Android) et web; backend Supabase hébergé au Canada (région Canada (Central), `ca-central-1`), selon la partie B.
- **Direction visuelle retenue :** concept 1 « Carnet de voyage », avec le logo « Colis caché » et l’icône d’appli « Signature » (charte graphique fournie à part).

## Structure du document

| Partie | Contenu | Préparée par |
|---|---|---|
| **A. Spécifications fonctionnelles et UX** | Rôles, navigation, parcours et histoires utilisateur avec critères d’acceptation, inventaire des 50 écrans, états et cas limites, accessibilité, localisation, événements analytiques, exigences UX de monétisation. | Équipe UI/UX |
| **B. Volet technique et sécurité** | Stack, architecture, modèle de données, machine d’états, webhooks Stripe, exigences de sécurité testables (SEC-01 à SEC-25), durées de conservation, monétisation technique, exigences non fonctionnelles, jalons et risques. | Équipe technique |
| **C. Volet légal de la monétisation** | Sources de revenus, prix et transparence (LPC, Loi sur la concurrence), commission, assurance, versements, séquestre et litiges, marketing et données, clauses des conditions d’utilisation, points à faire valider. | Équipe juridique |

Chaque partie garde sa propre numérotation. Les renvois prennent la forme « partie B, 4.1 » ou, dans le texte des équipes, « volet technique 4.1 » et « volet légal 2 ».

## Conventions de lecture

- **« À confirmer »** : point qui n’a pas été vérifié dans une source officielle ou qui dépend d’un fournisseur (Stripe, Supabase, assureur).
- **« À décider (par Faycal) »** : choix d’affaires ouvert : montants, taux, délais, plafonds. Les valeurs visibles dans les maquettes sont **illustratives**.
- **« À faire valider par l’avocat / le comptable »** : point juridique ou fiscal qui doit être validé avant le lancement.
- Les noms de personnes, numéros de vol, codes et montants des exemples sont **fictifs**.
- Les identifiants **US-xx** (histoires utilisateur, partie A) et **SEC-xx** (exigences de sécurité, partie B) servent à la traçabilité dans les tickets et les tests.

## Documents associés

- Maquettes : `volis-ecrans-concept1.pdf` (50 écrans) et planches par parcours.
- Charte graphique : `volis-charte-graphique.pdf` (17 pages).
- Ressources développeurs : `volis-dev-assets-partie1…3.zip` (tokens, thème React Native, icônes, illustrations, logos, icônes d’appli, polices, inventaire des écrans).


# Partie A — Spécifications fonctionnelles et UX

*Préparé par l’équipe UI/UX — 11 octobre 2026*

> **Portée de cette section.** Elle décrit ce que l’application doit faire du point de vue de l’utilisateur : rôles, parcours, histoires utilisateur, critères d’acceptation, états et cas limites, accessibilité, localisation et événements analytiques. Elle s’appuie sur les 50 maquettes du concept 1 « Carnet de voyage » (`volis-design/ecrans/`, numérotées 01 à 50) et sur la charte graphique (`volis-charte-graphique.pdf`). La technique (machine d’états, Stripe, sécurité) relève du volet technique; le cadre légal, du volet légal. Les renvois sont indiqués entre parenthèses.
>
> **Convention.** Les montants, taux, délais et plafonds visibles dans les maquettes (commission de 15 %, 1,5 % pour le versement instantané, protection de base de 100 $, valeur déclarée maximale de 1 000 $, délai de signalement de 72 h, etc.) sont **illustratifs**. Ils restent **à décider par Faycal**, puis à faire valider par l’équipe juridique quand c’est nécessaire. Tous les noms et numéros sont fictifs.

## 1. Rôles et principes

### 1.1 Rôles

| Rôle | Description | Compte requis | Vérification |
|---|---|---|---|
| **Visiteur** | Parcourt les trajets et les prix sans compte (« Explorer sans compte », écran 05). | Non | — |
| **Expéditeur** | Crée un envoi, choisit un voyageur, paie en séquestre, remet le colis, suit la livraison, laisse un avis. | Oui | Courriel + téléphone; identité (Stripe Identity) avant le 1er paiement (SEC-15). |
| **Voyageur** | Publie un voyage, accepte ou refuse les demandes, inspecte et transporte le colis, reçoit ses gains via Stripe Connect. | Oui | Courriel + téléphone + identité; vol confirmé (billet vérifié) pour le badge « Vol confirmé »; compte Stripe Connect avant le 1er versement. |
| **Destinataire** | Reçoit le colis à l’arrivée. Suit l’envoi par un lien web et donne le code de réception. | Non (lien de suivi) | Téléphone (reçoit le texto) |
| **Agent soutien / modération** (interne) | Traite les litiges, signalements, vérifications manuelles. | Outil interne | MFA obligatoire |

Un même compte peut être expéditeur et voyageur. Le rôle n’est pas un réglage : il découle de l’action (« J’envoie un colis » / « Je voyage », écran 07). Le choix de rôle à l’inscription (écran 06) sert seulement à personnaliser l’accueil.

### 1.2 Principes UX (rappel de la charte)

1. **Confiance visible au bon moment** : identité vérifiée, séquestre et preuves de remise sont rappelés à chaque décision (paiement, remise, acceptation).
2. **Une action principale par écran**, en bas, pleine largeur, libellée par un verbe précis (« Payer 32,06 $ »).
3. **Prix tout inclus, détail avant paiement** (volet légal 2; volet technique 4.1) : le prix affiché dans les listes inclut tous les frais obligatoires; seules les taxes s’ajoutent.
4. **Jamais de données bancaires ni biométriques dans nos écrans** : Stripe Identity et Stripe Connect sont hébergés (SEC-10, SEC-11).
5. **Accessible par défaut** : WCAG 2.2 AA, cibles 44 pt, texte dynamique (section 6).

## 2. Navigation et architecture de l’information

- **Barre d’onglets** (5 onglets fixes) : Accueil · Envois · Voyages · Messages · Profil. L’onglet actif est indiqué par une pilule sarcelle claire, un libellé gras et `accessibilityState.selected`. Une pastille corail signale du non lu (Messages, Notifications).
- **Piles de navigation** par onglet; les flux transactionnels (créer un envoi, paiement, remise, vérification) s’ouvrent en plein écran sans barre d’onglets, avec retour et un indicateur d’étape.
- **Feuilles modales** (bottom sheets) pour les choix secondaires : filtres (38), assurance (40), tri. Fermeture par glissement, bouton « Fermer » et geste retour Android.
- **Liens profonds** (SEC-23) : `volis://envoi/{id}`, `volis://voyage/{id}`, `volis://remise/{id}`, retour Stripe Identity et Stripe Connect par Universal Links / App Links. Le lien de suivi destinataire est une page web (`volis.app/s/{code}`).

## 3. Parcours et histoires utilisateur

Format : **US-xx** « En tant que…, je veux…, afin de… » puis critères d’acceptation (CA) vérifiables. Les écrans sont cités par leur numéro.

### 3.1 Parcours A — Accueil, inscription et connexion (écrans 01–06, 23–25)

**US-01 — Découvrir le service.** En tant que visiteur, je veux comprendre en trois écrans comment fonctionne Volis afin de décider si je m’inscris.
- CA1 : le splash (01) dure au plus le temps de chargement (masqué dès que les polices et la session sont prêtes, max. 2 s).
- CA2 : 3 écrans d’onboarding (02–04), pagination annoncée (« 1 sur 3 »), lien « Passer » sur chacun, glissement et boutons.
- CA3 : l’onboarding ne s’affiche qu’au premier lancement.

**US-02 — Créer un compte.** En tant que nouvel utilisateur, je veux m’inscrire avec Apple, Google ou mon courriel afin de commencer rapidement.
- CA1 : « Continuer avec Apple » est proposé sur iOS à côté de Google : la règle Apple 4.8 exige une option de connexion équivalente qui protège la vie privée dès qu’une connexion tierce est offerte.
- CA2 : champs prénom, nom, courriel, téléphone (+1 par défaut, indicatif modifiable), mot de passe avec règles visibles, case des conditions non cochée par défaut (06).
- CA3 : le téléphone est validé par un code SMS à 6 chiffres (25) : remplissage automatique (`oneTimeCode`), renvoi après 30 s, option d’appel vocal, 5 essais puis blocage temporaire (SEC-14).
- CA4 : la vérification d’identité n’est pas exigée à l’inscription; elle est demandée avant la 1re transaction (US-10).

**US-03 — Se connecter.** CA1 : connexion Apple, Google, clé d’accès (passkey) ou courriel + mot de passe (05). CA2 : flux PKCE via le navigateur système, aucune WebView (SEC-01). CA3 : message d’erreur générique (« Courriel ou mot de passe incorrect ») sans révéler l’existence du compte.

**US-04 — Récupérer mon mot de passe.** CA1 : saisie du courriel (23) puis écran de confirmation neutre (24) : « Si un compte existe, un lien vous a été envoyé ». CA2 : bouton « Ouvrir Courriel », renvoi possible après 60 s. CA3 : le lien expire (durée à décider) et ne contient aucun jeton réutilisable (SEC-23).

### 3.2 Parcours B — Vérification d’identité (écrans 17–22)

**US-10 — Vérifier mon identité.** En tant qu’utilisateur, je veux faire vérifier mon identité afin d’envoyer ou de transporter un colis.
- CA1 : l’intro (17) explique les 3 étapes et la durée (~2 min) avant tout traitement.
- CA2 : **consentement exprès et distinct** à la biométrie (18) : quoi, pourquoi, qui (Stripe), où (hors Québec, le cas échéant), durée (gabarit supprimé après la vérification), droits; case non cochée par défaut; bouton désactivé tant qu’elle ne l’est pas; alternative « vérification manuelle sans biométrie » toujours offerte (Loi 25; SEC-10). Le consentement est horodaté avec la version du texte (table `consents`).
- CA3 : la capture se fait sur la page hébergée Stripe Identity (19), présentée comme une page externe (barre d’adresse visible).
- CA4 : trois résultats : **Vérifiée** (20), **En cours d’examen** (21, notification à la fin), **Échec** (22, raison lisible issue de `last_error.reason`, conseils, nombre d’essais restants, voie manuelle).
- CA5 : Volis ne stocke que `identity_status` et l’ID de session; la session est effacée (redact) dès la vérification (SEC-10, tableau 3.1).

### 3.3 Parcours C — Recherche et réservation (écrans 07–11, 36, 38–40)

**US-20 — Chercher un voyageur.** En tant qu’expéditeur, je veux trouver un voyageur pour mon trajet afin d’envoyer mon colis.
- CA1 : recherche De / À (aéroport ou ville), date (exacte ou flexible), poids (07).
- CA2 : résultats (08) en cartes : nom abrégé (prénom + initiale), note et nombre d’avis, badges de vérification, date, kg disponibles, **prix total pour le poids saisi, frais inclus** (taxes en sus).
- CA3 : tri (recommandés, prix, date, note) et filtres en feuille (38) : dates ± 3/7 j, prix max, « ID vérifiée seulement », « Vol confirmé », note minimale; le bouton affiche le nombre de résultats (« Afficher 8 voyageurs »).
- CA4 : vue carte (39) : épingles par point de remise proposé (jamais l’adresse du voyageur), carte du voyageur sélectionné.
- CA5 : **aucun résultat** (36) : explication, « Créer une alerte » (dates flexibles, destinations proches), suggestion d’élargir.

**US-21 — Évaluer un voyageur.** CA1 : profil (09) : vérifications par niveau (courriel, téléphone, identité, vol), statistiques (livraisons, ponctualité, délai de réponse), avis récents. CA2 : numéro de vol et heure précise **masqués** jusqu’à l’acceptation. CA3 : boutons « Signaler » et « Bloquer » accessibles depuis le menu.

**US-22 — Décrire mon colis.** En tant qu’expéditeur, je veux déclarer le contenu, le poids et la valeur de mon colis afin d’obtenir un prix et d’être couvert.
- CA1 : formulaire en 4 étapes (Trajet, Colis, Voyageur, Paiement) avec indicateur (10).
- CA2 : 1 à 4 photos (ouvert puis fermé), poids, dimensions, catégorie de contenu, **valeur déclarée** avec plafond affiché près du champ (« sert de plafond d’indemnisation », volet légal 4).
- CA3 : rappel des objets interdits avec lien vers la liste complète (45); contrôle à la saisie **et** côté serveur.
- CA4 : attestation du contenu obligatoire, horodatée (table `parcels`).

**US-23 — Payer en séquestre.** En tant qu’expéditeur, je veux payer en sachant que l’argent est retenu jusqu’à la livraison afin de ne pas prendre de risque.
- CA1 : écran de paiement (11) avec résumé, **détail figé par le serveur** : transport, frais de service Volis, assurance (si choisie), taxes, total (volet technique 4.1).
- CA2 : l’assurance est une **option distincte, non cochée par défaut**, avec prix à part, couverture, plafond, exclusions et divulgation de la rémunération reçue de l’assureur (40; volet légal 4). Si l’option A (« recommandation ») est retenue, la feuille 40 devient une redirection vers l’assureur et l’assurance disparaît du total Volis.
- CA3 : Apple Pay / Google Pay / carte via PaymentSheet (aucun champ de carte maison, SEC-11).
- CA4 : le statut « Payé / retenu » n’apparaît qu’à la réception du webhook (`payment_intent.succeeded`); entre-temps : « Paiement en cours de confirmation ».
- CA5 : échec de paiement : message de la banque traduit, CTA « Réessayer » ou « Changer de moyen de paiement »; la réservation reste « Réservée ».

### 3.4 Parcours D — Demande, remise et suivi (écrans 12–14, 26–30, 33, 37, 43, 50)

**US-30 — Envoyer une demande.** CA1 : la demande expire si le voyageur ne répond pas (délai visible, ex. 24 h) (27). CA2 : rien n’est débité tant que la demande n’est pas acceptée (pré-autorisation affichée). CA3 : en cas de refus (29), le motif est affiché s’il est fourni, sans frais, avec d’autres voyageurs pour le même trajet.

**US-31 — Répondre à une demande (voyageur).** CA1 : détail (26) : expéditeur vérifié, contenu et photos, poids, gain net, capacité restante, délai pour répondre. CA2 : « Refuser » demande un motif facultatif (liste). CA3 : « Accepter » est désactivé si la capacité est dépassée.

**US-32 — Ajouter le destinataire.** CA1 : nom, téléphone international, ville (43). CA2 : lien de suivi généré et partageable; texto envoyé au destinataire avec son accord. CA3 : la page de suivi ne montre ni le nom complet ni le téléphone du voyageur.

**US-33 — Discuter en sécurité.** CA1 : messagerie par réservation (14), bannière « Ne payez jamais en dehors de l’appli ». CA2 : numéros de téléphone et courriels détectés et masqués; liens externes signalés. CA3 : signaler un message → masqué en attente de modération (SEC-16). CA4 : carte « Remise proposée » (lieu public, date, heure) acceptable en un geste.

**US-34 — Remettre le colis au voyageur.** En tant qu’expéditeur et voyageur, nous voulons une preuve de remise afin d’éviter tout litige.
- CA1 : le voyageur doit d’abord remplir l’**attestation douane renforcée** (49) : contenu vu ouvert, conforme, sans objet interdit; il peut refuser sans pénalité.
- CA2 : l’expéditeur affiche un QR et un code à 4 chiffres (13); le voyageur scanne ou saisit le code; photo du colis scellé; les deux confirment.
- CA3 : **mode hors ligne** (37) : le code signé est stocké sur l’appareil, la remise est horodatée localement puis synchronisée.
- CA4 : transition « Payée / retenue » → « Remise au voyageur » seulement après confirmation des deux parties (volet technique 2.5).

**US-35 — Suivre mon colis.** CA1 : frise (12) : Accepté → Paiement sécurisé → Remis au voyageur → Embarqué → Atterri → Remis au destinataire → Fonds libérés; étape en cours mise en avant. CA2 : statut du vol (à l’heure, retardé, annulé). CA3 : **Live Activity iOS / notification persistante Android** (50) pendant le vol : trajet, progression, heure d’arrivée; désactivable.

**US-36 — Confirmer la livraison et noter.** CA1 : le destinataire donne son code ou le voyageur prend une photo; l’expéditeur est notifié (33). CA2 : avis **en double aveugle** : chacun voit l’avis de l’autre seulement après avoir publié le sien ou après 14 jours. CA3 : note obligatoire, commentaire facultatif, qualités en puces. CA4 : « Signaler un problème » reste accessible pendant le délai de contestation.

**US-37 — Voir mes envois.** CA1 : liste (30) avec onglets « En cours » / « Terminés », statut en badge texte + couleur, progression. CA2 : brouillons reprenables.

### 3.5 Parcours E — Côté voyageur (écrans 15, 26, 31, 49)

**US-40 — Publier un voyage.** CA1 : trajet, date, vol (numéro facultatif, billet joint en privé pour le badge « Vol confirmé »), capacité en kg, catégories acceptées, prix par kg avec suggestion (15). CA2 : le billet n’est jamais visible par les expéditeurs. CA3 : publication modifiable tant qu’aucune demande n’est acceptée.

**US-41 — Gérer mes voyages.** CA1 : liste (31) : capacité acceptée / en attente / libre, demandes à traiter, gain prévu. CA2 : annuler un voyage avec demandes acceptées déclenche le parcours de réattribution pour chaque expéditeur (US-50).

### 3.6 Parcours F — Imprévus, litiges et aide (écrans 34, 35, 44, 45)

**US-50 — Vol retardé ou annulé.** En tant qu’expéditeur, je veux savoir quoi faire si le vol est annulé afin de ne pas perdre mon argent.
- CA1 : notification immédiate; écran (34) avec le vol annulé, rappel « Votre argent est protégé ».
- CA2 : trois choix : réattribuer à un autre voyageur (prix égal ou inférieur), garder le voyageur sur son nouveau vol, remboursement total.
- CA3 : un simple retard ne demande aucune action; on avertit à chaque changement.
- CA4 : sans choix de l’expéditeur dans un délai (à décider), remboursement automatique.

**US-51 — Ouvrir un litige.** CA1 : motif (endommagé, manquant, non livré, autre), description, photos de l’utilisateur + **preuves automatiques** (photos de remise horodatées) (35). CA2 : indemnisation possible affichée : protection de base (sans assurance) ou couverture de l’assurance, plafonnée à la valeur déclarée. CA3 : délai de signalement et délai de réponse affichés; transfert au voyageur gelé pendant l’examen (`legal_holds`, SEC-25). CA4 : la décision est notifiée avec explication et recours.

**US-52 — Trouver de l’aide.** CA1 : centre d’aide (44) avec recherche, catégories, FAQ, contact soutien (délai moyen affiché) et **urgence sécurité** distincte. CA2 : liste des objets interdits et sous conditions (45), aussi accessible depuis la création d’envoi et l’attestation douane.

### 3.7 Parcours G — Profil, argent et réglages (écrans 16, 32, 41, 42, 46–48)

**US-60 — Recevoir mes gains.** En tant que voyageur, je veux retirer mon argent afin d’être payé pour mes trajets.
- CA1 : première fois : configuration via **Stripe Connect hébergé** (42); Volis ne voit jamais les coordonnées bancaires.
- CA2 : écran Versements (41) : solde disponible, montants en séquestre, choix **Standard (gratuit, toujours offert)** ou **Instantané** avec frais affichés avant la confirmation (volet technique 4.3; volet légal 5). Si une marge Volis existe, elle est libellée « frais Volis ».
- CA3 : historique avec statuts « En séquestre », « En cours », « Déposé », « Échoué » (webhooks `payout.*`).

**US-61 — Gérer mes notifications.** CA1 : centre (32) groupé par jour; non lu signalé par un point + texte masqué pour lecteur d’écran (« non lu »). CA2 : préférences par canal (push, texto, courriel) et par type; les notifications transactionnelles critiques (paiement, remise, litige) ne peuvent pas être toutes désactivées.

**US-62 — Réglages et confidentialité.** CA1 : langue (fr-CA, en-CA; arabe à évaluer), devise, notifications, moyens de paiement, versements, clé d’accès, consentements (retrait possible), visibilité du profil, **télécharger mes données** (JSON, SEC-19) (46).

**US-63 — Supprimer mon compte.** En tant qu’utilisateur, je veux supprimer mon compte depuis l’appli (règle Apple 5.1.1(v)).
- CA1 : écran d’explication (47) : ce qui est supprimé, ce qui est conservé et combien de temps (paiements 6 ans après l’année fiscale, preuves de litige 3 ans, consentements 3 ans après la fermeture : tableau 3.1 du volet technique).
- CA2 : blocages explicites : envoi en cours, litige ouvert, solde non viré, avec action pour chacun.
- CA3 : ré-authentification (SEC-02) puis confirmation forte (48 : saisir « SUPPRIMER »). Délai de grâce (ex. 30 jours) **à décider**; courriel de confirmation.
- CA4 : après suppression : session révoquée, profil anonymisé, avis conservés sous « Membre supprimé ».

## 4. Inventaire des écrans

Inventaire complet (id, fichier, parcours, objectif, composants clés, onglet) : `dev-assets/screens/inventaire-ecrans.csv`. Résumé :

| Parcours | Écrans | Histoires |
|---|---|---|
| A · Accueil, connexion et compte | 01 Splash · 02–04 Onboarding · 05 Connexion · 06 Inscription · 23 Mot de passe oublié · 24 Lien envoyé · 25 Code SMS | US-01 à US-04 |
| B · Vérification d’identité | 17 Intro · 18 Consentement biométrique · 19 Stripe Identity · 20 Vérifiée · 21 En attente · 22 Échec | US-10 |
| C · Recherche et réservation | 07 Accueil · 08 Résultats · 38 Filtres · 39 Carte · 36 Aucun résultat · 09 Profil voyageur · 10 Créer un envoi · 11 Paiement · 40 Assurance | US-20 à US-23 |
| D · Envoi, remise et suivi | 30 Mes envois · 27/28/29 Détail (en attente / accepté / refusé) · 43 Destinataire · 14 Messages · 13 Remise · 37 Remise hors ligne · 12 Suivi · 50 Live Activity · 33 Livraison et avis | US-30 à US-37 |
| E · Côté voyageur | 15 Publier · 31 Mes voyages · 26 Demande reçue · 49 Attestation douane | US-31, US-34, US-40, US-41 |
| F · Imprévus, litiges et aide | 34 Vol annulé · 35 Litige · 44 Centre d’aide · 45 Objets interdits | US-50 à US-52 |
| G · Profil, argent et réglages | 16 Profil / Portefeuille · 41 Versements · 42 Stripe Connect · 32 Notifications · 46 Réglages · 47–48 Suppression | US-60 à US-63 |

**Écrans à concevoir en phase 2** (non maquettés) : édition du profil, modifier / annuler un voyage, ajout d’une carte (feuille Stripe), reçu détaillé, page web de suivi destinataire, mise à jour forcée (SEC-21), outil interne de modération.

## 5. États et cas limites

### 5.1 États transverses (tous les écrans de données)

| État | Traitement |
|---|---|
| Chargement | Squelettes aux dimensions du contenu (pas de spinner plein écran au-delà de 300 ms); boutons en état « chargement » pendant une action. |
| Vide | Illustration + explication + action utile (36). Jamais un écran blanc. |
| Erreur réseau | Toast « Hors ligne · on réessaie automatiquement »; données en cache affichées avec la date de dernière synchro; actions d’argent bloquées hors ligne (sauf code de remise, 37). |
| Erreur serveur | Message humain + « Réessayer »; identifiant de corrélation dans « Détails » pour le soutien. |
| Permission refusée | Expliquer l’utilité, proposer « Ouvrir les réglages »; ne pas redemander en boucle (SEC-24). |
| Session expirée | Ré-authentification en feuille, retour à l’écran en cours sans perte de saisie. |
| Version obsolète | Écran de mise à jour bloquant (SEC-21). |

### 5.2 Cas limites métier

| Cas | Comportement attendu |
|---|---|
| Deux expéditeurs dépassent ensemble la capacité du voyageur | La 2e acceptation est refusée par le serveur (verrou de version); message « capacité atteinte ». |
| Paiement confirmé par l’app mais webhook absent | Statut « Paiement en cours de confirmation »; relance serveur; jamais « Payé » sans webhook. |
| Le voyageur ne se présente pas à la remise | Bouton « Il n’est pas venu » après l’heure + 30 min → réattribution ou remboursement (comme 34). |
| Colis non conforme à la déclaration | Le voyageur refuse à l’attestation (49) : aucune pénalité pour lui; l’expéditeur est remboursé selon la politique (frais non remboursables à décider, volet légal 6). |
| Saisie ou refus par la douane | Litige spécial; non couvert par l’assurance (40); le voyageur fournit la preuve de la douane. |
| Destinataire injoignable à l’arrivée | Le voyageur garde le colis 48 h (à décider), messagerie à trois, puis procédure de retour. |
| Rétrofacturation bancaire | Réservation → « Litige » quel que soit l’état; transfert gelé; preuves assemblées automatiquement (volet technique 4.6). |
| Vérification d’identité en échec définitif | Voie manuelle; impossible de payer ou de transporter tant qu’elle n’est pas réglée. |
| Suppression demandée avec envoi en cours | Bloquée avec explication (47). |
| Changement de fuseau horaire | Heures affichées dans le fuseau du lieu de l’événement, avec mention (« 21 h 40, heure d’Alger »). |

## 6. Accessibilité

Objectif : **WCAG 2.2 niveau AA**, lignes directrices Apple et Android. Critères vérifiables :

1. Contraste : texte ≥ 4,5:1, grand texte et composants ≥ 3:1 (tableau de la charte, page 6). Texte blanc interdit sur corail.
2. Cibles tactiles ≥ 44 × 44 pt, espacées de 8 pt.
3. Texte dynamique jusqu’à 200 % sans perte d’information : montants, codes et statuts jamais tronqués; mise en page en colonne à grande taille.
4. Lecteurs d’écran : chaque élément interactif a un libellé français, un rôle et un état; les illustrations sont décoratives (`accessible={false}`); les codes sont lus chiffre par chiffre; les montants sont lus en entier (« trente-deux dollars et six cents »).
5. Statuts et erreurs : couleur + icône/pastille + texte; erreurs de formulaire annoncées (`accessibilityLiveRegion` / `announceForAccessibility`).
6. Ordre de focus logique; focus visible sur web et clavier externe.
7. « Réduire les animations » respecté; aucune information transmise seulement par le mouvement.
8. Minuteries visibles et prolongeables (code SMS, expiration de demande).
9. Formulaires : étiquettes visibles, `textContentType`/`autoComplete` corrects, clavier adapté.
10. Tests : audit VoiceOver + TalkBack de chaque parcours avant chaque version majeure; vérification automatique (axe sur web, `eslint-plugin-react-native-a11y`).

## 7. Localisation

- **Langue par défaut : français (Canada)**; anglais (Canada) au lancement; arabe (RTL) à évaluer selon les corridors (Algérie, Maroc). Toutes les chaînes dans des fichiers de traduction (i18next + `expo-localization`); aucune chaîne en dur.
- **Formats fr-CA** : `32,06 $`, `21 h 40`, `ven. 14 nov.`, séparateur de milliers espace insécable (`1 000 $`). Utiliser `Intl.NumberFormat('fr-CA', { style: 'currency', currency: 'CAD' })` et `Intl.DateTimeFormat`.
- **Termes** : courriel, texto, égoportrait, clé d’accès, séquestre (guide de ton, charte p. 16). Vouvoiement.
- **Pluriels et genres** gérés par ICU MessageFormat (« 1 voyageur », « 8 voyageurs »).
- **RTL** : utiliser `start`/`end`, icônes directionnelles miroir, codes et montants restent LTR.
- **Fuseaux** : stocker en UTC, afficher dans le fuseau pertinent avec la ville.
- **Expansion** : prévoir +30 % de longueur (anglais → français); boutons sur deux lignes interdits, préférer un libellé plus court.
- Les reçus et contrats sont en français (volet légal 2).

## 8. Événements analytiques suggérés

Respect de la Loi 25 : consentement explicite pour les mesures non essentielles; aucun nom, courriel, téléphone, adresse, contenu de message ou montant exact lié à une personne dans les événements (SEC-13). Identifiant pseudonyme, propriétés catégorielles.

| Événement | Déclencheur | Propriétés |
|---|---|---|
| `onboarding_completed` / `onboarding_skipped` | Fin ou « Passer » (02–04) | `step` |
| `signup_started` / `signup_completed` | 06 | `method` (apple, google, email), `role_hint` |
| `phone_verified` | 25 | `attempts` |
| `identity_started` / `identity_consent_given` / `identity_result` | 17, 18, 20–22 | `result` (verified, processing, failed), `reason_code` |
| `search_performed` | 07 | `corridor` (YUL-ALG), `date_flex`, `weight_bucket` |
| `search_no_results` / `alert_created` | 36 | `corridor` |
| `filters_applied` / `map_opened` | 38, 39 | `filters_count`, `sort` |
| `traveler_profile_viewed` | 09 | `trust_level` |
| `shipment_draft_step` | 10 | `step` (1–4) |
| `insurance_viewed` / `insurance_added` | 40, 11 | `value_bucket` |
| `checkout_started` / `payment_succeeded` / `payment_failed` | 11 | `method`, `error_code` |
| `request_sent` / `request_accepted` / `request_declined` / `request_expired` | 26–29 | `decline_reason` |
| `handover_completed` | 13, 37 | `offline` (bool) |
| `customs_attestation_refused` | 49 | `reason` |
| `flight_disruption_choice` | 34 | `choice` (reassign, keep, refund) |
| `dispute_opened` | 35 | `reason` |
| `delivery_confirmed` / `review_submitted` | 33 | `rating`, `tags_count` |
| `trip_published` | 15 | `corridor`, `capacity_bucket` |
| `payout_onboarding_started` / `payout_requested` | 42, 41 | `type` (standard, instant) |
| `account_deletion_started` / `account_deleted` | 47, 48 | `reason` |

Indicateurs clés : conversion recherche → paiement, délai de 1re réponse du voyageur, taux d’acceptation, taux de litige pour 100 livraisons, réussite de la vérification d’identité, part des versements instantanés, NPS après livraison.

## 9. Monétisation : exigences UX

Le cadre légal est dans le volet légal (sections 1 à 6) et la mise en œuvre dans le volet technique (section 4). Les règles d’interface :

1. **Prix tout inclus partout** : les cartes de résultats, le profil voyageur et la carte affichent le prix pour le poids saisi, **frais de service inclus**, avec la mention « frais inclus » ; seules les taxes s’ajoutent au paiement. Exemple des maquettes : transport 24,00 $ + frais 3,60 $ = **27,60 $** affiché (08, 09, 39).
2. **Détail avant paiement** (11) : transport, frais de service Volis (taux affiché), assurance si choisie, taxes (TPS, TVQ, taxe sur la prime), total. Le bouton reprend le total exact (« Payer 32,06 $ »). Sans assurance, le total de l’exemple est de 28,14 $.
3. **Assurance optionnelle** (40) : jamais présélectionnée, jamais obligatoire; prix séparé; couvert / non couvert; plafond = valeur déclarée; nom de l’assureur partenaire; divulgation de la rémunération reçue par Volis; lien vers le résumé de la police. Les mots « assuré » ou « garanti » ne s’affichent que si l’assurance est choisie (volet légal 2).
4. **Protection de base** : sans assurance, le plafond d’indemnisation Volis est affiché près de la valeur déclarée (10) et dans le litige (35). Le texte ne doit pas laisser croire à une exclusion de responsabilité (volet légal 4).
5. **Gain du voyageur** affiché net (26, 31) : ce qu’il recevra, sans ambiguïté sur la commission.
6. **Versement instantané** (41) : frais visibles avant le choix; standard gratuit toujours offert et présélectionné.
7. **Remboursements** : montant et délai affichés au moment du choix (34 : « 100 % remboursé en 3 à 5 jours ouvrables »); frais non remboursables indiqués avant le paiement s’il y en a.
8. **Mises en avant ou abonnement** (phase ultérieure) : étiquette « Commandité » sur toute annonce mise en avant; prix et renouvellement clairs; résiliation en 2 gestes depuis Réglages.
9. **Reçus** en français, accessibles depuis le détail de l’envoi et le portefeuille.


# Partie B — Volet technique et sécurité

*Préparé pour Faycal Chefai (Trois-Rivières, QC) — 11 octobre 2026*

> **Portée de cette section.** Ce document couvre la partie technique du cahier des charges de Volis (application de mise en relation entre expéditeurs de colis et voyageurs, sur iOS, Android et web). Il est assemblé avec la partie A (spécifications fonctionnelles et UX) et la partie C (volet légal de la monétisation) du présent cahier des charges. Les aspects légaux et fiscaux relèvent de l'équipe juridique et d'un avocat membre du Barreau du Québec. Ils ne sont repris ici que pour en déduire des exigences techniques.
>
> **Sources :** fiche « Projet Volis — Fiche de recherche » (11 octobre 2026), « Guide sécurité et architecture mobile » (déjà fourni), documentation officielle Expo, Stripe et OWASP MASVS v2.1.0. **Convention :** tout ce qui n'a pas été vérifié dans une source officielle est marqué **« à confirmer »**. Aucun montant, taux ni objectif chiffré n'est fixé ici : ils restent **à décider par Faycal**.

## 1. Stack technique justifiée

### 1.1 Vue d'ensemble

| Besoin | Choix | Justification | Statut |
|---|---|---|---|
| App iOS, Android, web | **Expo (React Native) + Expo Router + TypeScript** | Un seul code pour les trois plateformes, routage par fichiers commun au mobile et au web, maquettes déjà prêtes pour cette approche, TypeScript pour typer le domaine et les contrats d'API. | Retenu (fiche de recherche) |
| Backend | **Supabase** (recommandé, voir 1.2) | Auth, PostgreSQL, sécurité par ligne (RLS), stockage, temps réel et fonctions serveur réunis, ce qui convient à une petite équipe. | Recommandé |
| Vérification d'identité | **Stripe Identity** (pièce d'identité + égoportrait) | Vérification déléguée à Stripe ; Volis ne stocke que le statut et l'ID de session. | Retenu |
| Paiements de la place de marché | **Stripe Connect, « separate charges and transfers »** | Le paiement est encaissé sur le compte de la plateforme puis transféré au voyageur seulement quand le serveur confirme la remise. Une pré-autorisation de carte en ligne expire généralement après 7 jours (doc Stripe), ce qui ne suffit pas pour un trajet. Connect gère le KYC des voyageurs. | Retenu |
| Notifications push | **Expo Notifications** (service push d'Expo vers APNs et FCM) | Une seule API pour iOS et Android ; jetons d'appareil enregistrés côté serveur. | Retenu |
| Cartes et géolocalisation | `expo-location` + composant de carte (par ex. `react-native-maps` sur mobile ; équivalent web à choisir) | La localisation n'est demandée qu'en contexte, désactivée par défaut (Loi 25, MASVS-PRIVACY-1). Géocodage via le backend pour ne pas exposer de clé facturée. | Fournisseur de cartes **à confirmer** |
| Photos de remise et de litige | **Supabase Storage**, compartiments privés, URL signées de courte durée | Pas d'accès public ; métadonnées EXIF (dont GPS) retirées avant stockage. | Retenu |
| Messagerie entre utilisateurs | Table `messages` dans PostgreSQL + **Supabase Realtime** | Messages liés à une réservation, protégés par RLS, modérables. | Retenu |
| Internationalisation | `expo-localization` + bibliothèque i18n (par ex. i18next) ; `I18nManager` pour l'arabe (droite à gauche) ; `Intl` pour les nombres et devises | Français (par défaut au Québec), anglais, arabe en RTL ; montants en unités mineures entières + code devise ISO 4217. | Bibliothèque i18n **à confirmer** |
| Analytics et monitoring | **Sentry** (plantages, performance) ; outil d'analytics produit **à confirmer** | Données personnelles masquées avant envoi ; analytics non essentielles uniquement après consentement. | Partiellement retenu |
| CI/CD | **GitHub Actions** (lint, tests, analyses de sécurité) + **EAS Build / EAS Submit** (builds signés et envoi aux stores) ; EAS Update pour les correctifs JavaScript **à confirmer** | Pipeline reproductible, signature gérée hors du dépôt. | Retenu |

### 1.2 Backend : Supabase ou Node/NestJS + PostgreSQL

| Critère | Supabase | Node/NestJS + PostgreSQL |
|---|---|---|
| Mise en route | Rapide : Auth, base, stockage, temps réel et fonctions fournis | Plus lente : tout est à assembler (auth, stockage, temps réel, hébergement) |
| Autorisation | RLS dans PostgreSQL, au niveau des lignes, plus des contrôles dans les fonctions serveur | Gardes et contrôles dans le code de chaque route |
| Webhooks Stripe | Edge Function (Deno) avec vérification de signature | Route NestJS dédiée ; écosystème Node standard |
| Logique métier complexe | Fonctions SQL et Edge Functions ; demande de la rigueur pour ne pas disperser la logique | Très flexible, architecture en modules |
| Exploitation | Service géré ; dépendance à un fournisseur | Plus de contrôle, plus de travail d'exploitation (mises à jour, sauvegardes, montée en charge) |
| Hébergement au Canada | Région **Canada (Central)**, code `ca-central-1` (vérifié dans la doc Supabase « Available regions ») | Selon l'hébergeur choisi : **à confirmer** |

**Recommandation : Supabase** pour le MVP. La plateforme fournit les briques nécessaires à Volis (Auth avec PKCE et MFA, RLS, stockage privé, temps réel pour la messagerie). La logique sensible reste côté serveur :

- La machine d'états des livraisons et la libération des fonds se font uniquement dans des fonctions serveur (Edge Functions ou fonctions PostgreSQL `SECURITY DEFINER`), jamais depuis l'app.
- L'app n'a aucun droit d'écriture direct sur les tables `payments`, `transfers` et `deliveries.status`.
- **Région : Canada (Central), `ca-central-1`** (existence vérifiée dans la doc Supabase, https://supabase.com/docs/guides/platform/regions). Il faut choisir cette **région précise** à la création du projet, et non la région générale « Americas », qui déploie dans une région AWS de la zone (par ex. Virginie du Nord). Ce choix est **recommandé, pas exigé par la loi** : il allège l'évaluation des transferts hors Québec dans l'ÉFVP, puisque la base, le stockage et l'authentification restent au Canada. Selon l'équipe juridique, il ne reste alors que Stripe à justifier. **À faire valider par l'avocat.** Point technique à signaler à l'équipe juridique : d'autres fournisseurs reçoivent aussi des données (Sentry, service push d'Expo, éventuel outil d'analytics, assureur partenaire) et doivent figurer dans l'ÉFVP. Les Edge Functions peuvent être invoquées dans `ca-central-1` (doc Supabase « Regional Invocations ») : à configurer.
- Pour garder une porte de sortie, les règles métier sont écrites en TypeScript pur (couche domaine partagée) et la base reste du PostgreSQL standard. Une migration vers NestJS + PostgreSQL resterait possible si les besoins dépassent les Edge Functions.

> **Règle d'or (fiche de recherche) :** c'est le serveur qui décide de libérer un paiement, jamais l'application.

## 2. Architecture

### 2.1 Schéma du système

![Figure B-1 — Schéma du système](/workspace/volis/assemblage/diagramme-B1.png){width=16.5cm}

### 2.2 Couches côté application

Conformément au guide (architecture « Clean Architecture pragmatique ») :

| Couche | Contenu dans Volis | Règles |
|---|---|---|
| **UI (MVVM)** | Écrans Expo Router ; hooks jouant le rôle de ViewModel (`useTripSearchViewModel`, etc.) qui exposent un état d'écran immuable ; flux unidirectionnel | L'UI n'appelle jamais le réseau ni le stockage directement. Elle affiche les statuts fournis par le serveur. |
| **Domaine (optionnel)** | Types métier (`Delivery`, `Booking`, `Money`), règles pures (transitions d'états permises côté affichage, calcul de l'affichage du détail de prix reçu du serveur) | TypeScript pur, sans dépendance React Native ; testé unitairement. |
| **Data (repositories)** | `TripsRepository`, `BookingsRepository`, `PaymentsRepository`, `MessagesRepository`… ; client Supabase, client HTTP des Edge Functions, cache (TanStack Query), stockage sécurisé | Point unique pour les jetons, la validation des réponses, la gestion des erreurs et le cache hors-ligne. |

### 2.3 Structure de dossiers type

```text
volis/
  app/                         # routes Expo Router (iOS, Android, web)
    (auth)/  connexion.tsx, inscription.tsx
    (tabs)/  trajets/, envois/, messages/, profil/
    reservation/[id].tsx
    litige/[id].tsx
    _layout.tsx                # fournisseurs (i18n, thème, requêtes, session)
  src/
    features/                  # une fonctionnalité = écrans + ViewModels + composants
      trips/  shipments/  bookings/  payments/  identity/
      messaging/  disputes/  reviews/  account/  payouts/
    domain/                    # types et règles pures (sans React Native)
    data/
      api/                     # client Supabase, client Edge Functions, intercepteurs
      repositories/
      secure/                  # wrapper expo-secure-store
      cache/                   # persistance hors-ligne (non sensible)
    ui/                        # design system (thème « Carnet de voyage » / « Scrapbook »)
    i18n/                      # fr, en, ar (RTL)
    test/                      # fakes, utilitaires
  supabase/
    migrations/                # schéma SQL versionné + politiques RLS
    functions/                 # Edge Functions (stripe-webhook, release-funds, …)
    tests/                     # tests RLS et tests de fonctions
  .github/workflows/           # CI
  eas.json  app.config.ts
```

### 2.4 Modèle de données principal

| Entité | Champs principaux (indicatifs) | Remarques |
|---|---|---|
| `users` (profils) | `id` (= Auth), nom affiché, langue, pays, `identity_status`, `stripe_identity_session_id`, `stripe_account_id` (voyageur), `stripe_customer_id` (expéditeur), dates de consentement, `deleted_at` | **Aucune image biométrique ni donnée bancaire.** |
| `trips` (annonces de trajet) | `id`, `traveler_id`, origine, destination, dates, capacité déclarée, restrictions, statut | Publiées par les voyageurs. |
| `shipment_requests` (demandes d'envoi) | `id`, `sender_id`, origine, destination, fenêtre de dates, statut | Publiées par les expéditeurs. |
| `parcels` (colis) | `id`, `shipment_request_id`, description, dimensions/poids déclarés, `declared_value` + devise, attestation du contenu (horodatée), photos de dépôt | Liste d'objets interdits vérifiée à la saisie et côté serveur. |
| `bookings` (réservations) | `id`, `trip_id`, `parcel_id`, `sender_id`, `traveler_id`, prix convenu (détail : transport, commission, assurance, taxes, total), `status` (machine d'états 2.5), `version` | Le détail de prix est calculé et figé par le serveur. |
| `payments` | `id`, `booking_id`, `stripe_payment_intent_id`, `stripe_charge_id`, montant, devise, statut, `transfer_group` | Écrit uniquement par le serveur. |
| `transfers` | `id`, `booking_id`, `stripe_transfer_id`, destination, montant, statut, éventuelle annulation (`reversal`) | Créé seulement par la fonction de libération des fonds. |
| `insurance_policies` | `id`, `booking_id`, partenaire, référence de police, statut | Selon l'intégration avec l'assureur partenaire (**à confirmer**). |
| `disputes` (litiges) | `id`, `booking_id`, ouvert par, motif, description, statut, décision, `stripe_dispute_id` éventuel | Couvre les litiges internes et les rétrofacturations. |
| `dispute_evidence` | `id`, `dispute_id`, chemin de stockage, type, auteur | Photos dans un compartiment privé. |
| `delivery_proofs` | `id`, `booking_id`, type (remise au voyageur, livraison), photo, code de confirmation, horodatage | Preuves de remise. |
| `reviews` (avis) | `id`, `booking_id`, auteur, cible, note, commentaire, statut de modération | Un avis par partie et par réservation. |
| `conversations` / `messages` | `id`, `booking_id`, participants ; `message.id`, auteur, contenu, statut de modération, signalé | Accessibles seulement aux participants (RLS). |
| `reports` (signalements) | `id`, auteur, cible (utilisateur, message, photo, annonce), motif, statut | Alimente la modération et l'anti-fraude. |
| `legal_holds` | ressource visée, motif (litige, rétrofacturation), ouvert le, levé le | Suspend la purge (voir 3.1). |
| `consents` | utilisateur, finalité, version du texte, accordé le, retiré le | Preuves de consentement (voir 3.1). |
| `stripe_events` | `event_id` (unique), type, reçu le, traité le, résultat | Idempotence des webhooks. |
| `audit_log` | acteur, action, ressource, horodatage, identifiants techniques | **Sans données personnelles en clair.** |
| `security_incidents` | date, description, données touchées, évaluation du risque, mesures, avis transmis | Registre des incidents (Loi 25). |

### 2.5 Machine d'états d'une livraison

![Figure B-2 — Machine d’états d’une livraison](/workspace/volis/assemblage/diagramme-B2.png){width=9.5cm}

Règles :

- Chaque transition est faite par une fonction serveur qui vérifie l'état courant, le rôle de l'appelant et la version de la ligne (verrou optimiste). Les transitions non prévues sont refusées.
- `PayeeRetenue` n'est atteint que sur réception du webhook Stripe, jamais sur un retour de l'app.
- `FondsLiberes` déclenche un `Transfer` Stripe avec `source_transaction` (doc Stripe : le transfert est accepté mais n'est exécuté que lorsque les fonds du paiement sont disponibles).
- Une rétrofacturation (`charge.dispute.created`) fait passer la réservation en `Litige`, quel que soit son état. Si le transfert a déjà été fait, une annulation de transfert (reversal) peut être nécessaire selon les conditions (**à confirmer avec l'équipe juridique**, section 6 du volet légal).
- La durée maximale pendant laquelle les fonds peuvent rester sur le solde de la plateforme avant le transfert est **à confirmer avec Stripe**. Les délais de contestation et de libération sont **à décider**.

### 2.6 Webhooks Stripe à traiter

Deux points de terminaison distincts : un pour les événements du compte plateforme, un pour les événements des comptes connectés (Connect). Les deux vérifient la signature et sont idempotents (voir SEC-08).

| Événement | Point de terminaison | Action |
|---|---|---|
| `payment_intent.succeeded` | Plateforme | Réservation → `PayeeRetenue` ; enregistrer `charge_id`. |
| `payment_intent.payment_failed` | Plateforme | Informer l'expéditeur ; la réservation reste `Reservee`. |
| `payment_intent.canceled` | Plateforme | Réservation annulée si applicable. |
| `charge.refunded` | Plateforme | Réservation → `Remboursee` ; reçu de remboursement. |
| `charge.dispute.created` / `charge.dispute.updated` / `charge.dispute.closed` | Plateforme | Ouvrir ou mettre à jour le litige ; préparer les preuves de remise ; suspendre le transfert. |
| `radar.early_fraud_warning.created` | Plateforme | Signal de fraude : suspendre le transfert, révision manuelle. |
| `transfer.created` / `transfer.reversed` | Plateforme | Mettre à jour `transfers`. Noms exacts des événements de transfert disponibles dans la version d'API retenue : **à confirmer**. |
| `identity.verification_session.verified` | Plateforme | `identity_status = verified`. |
| `identity.verification_session.requires_input` | Plateforme | `identity_status = requires_input` ; afficher `last_error.reason`. |
| `identity.verification_session.processing` / `canceled` | Plateforme | Mettre à jour le statut. |
| `identity.verification_session.redacted` | Plateforme (abonnement explicite requis selon la doc Stripe) | Confirmer l'effacement des données chez Stripe. |
| `account.updated` | Connect | Mettre à jour les capacités du voyageur (`charges_enabled`, `payouts_enabled`, exigences en attente). |
| `payout.created` / `payout.paid` / `payout.failed` | Connect | Statuts des versements affichés au voyageur (« en cours → déposé ») ; alerte en cas d'échec. |
| `customer.subscription.*`, `invoice.paid`, `invoice.payment_failed` | Plateforme | Seulement si un abonnement est lancé (Stripe Billing, voir 4.5). |

Version de l'API Stripe épinglée et mise à jour volontairement (procédure de test en staging).

## 3. Sécurité — exigences testables

Référentiels : OWASP MASVS v2.1.0, OWASP API Security Top 10 (2023), guide « Guide sécurité et architecture mobile » (sections 2.2 à 2.9). Profil visé : **MAS-L1 au minimum, plus MASVS-NETWORK-2 et MASVS-RESILIENCE à évaluer**, car l'app manipule de l'argent (recommandation du guide). Le niveau final est **à confirmer** après la modélisation des menaces (STRIDE).

| ID | Exigence | Référence | Critère de vérification |
|---|---|---|---|
| SEC-01 | Authentification par **Supabase Auth avec flux PKCE** (ou fournisseur OIDC avec code d'autorisation + PKCE via le navigateur système). Aucune WebView de connexion. | MASVS-AUTH-1 ; RFC 8252, RFC 7636 | Revue de config ; test : le flux implicite est refusé. |
| SEC-02 | **MFA optionnelle** (TOTP ou passkeys, **à confirmer**) proposée aux utilisateurs ; **ré-authentification** avant les opérations sensibles (changement de courriel, export, suppression du compte, ajout de méthode de versement). | MASVS-AUTH-3 | Test E2E : opération sensible refusée sans ré-authentification récente. |
| SEC-03 | **Jetons d'accès courts**, refresh token avec rotation et révocation côté serveur à la déconnexion et au changement de mot de passe. Durées exactes : **à décider**. | MASVS-AUTH-1 ; RFC 9700 | Test : refresh token réutilisé → session révoquée. |
| SEC-04 | **Autorisation côté serveur sur chaque ressource** : RLS activée sur toutes les tables exposées, politiques par rôle (expéditeur, voyageur, admin) ; aucune table sans politique. | MASVS-AUTH ; API1/API3/API5 | Tests RLS automatisés en CI : l'utilisateur A ne lit ni ne modifie les données de B ; requête qui liste les tables sans RLS = vide. |
| SEC-05 | **Stockage sécurisé** : jetons uniquement dans `expo-secure-store` (Keychain iOS / Keystore Android) ; rien de sensible dans AsyncStorage ni dans le cache persistant ; purge à la déconnexion. Sur le web : cookies `HttpOnly`/`Secure` ou stratégie équivalente (**à confirmer**). | MASVS-STORAGE-1/2 | Inspection de l'appareil (MASTG) ; MobSF sans constat critique. |
| SEC-06 | **Aucun secret dans l'app** : seules les clés publiques (URL Supabase, clé anonyme, clé publiable Stripe) sont embarquées. Clé secrète Stripe, clé `service_role` Supabase et secrets des webhooks uniquement côté serveur. | Guide 2.4 ; M1 | gitleaks en CI ; décompilation du bundle sans secret trouvé. |
| SEC-07 | **HTTPS partout** ; aucune exception ATS / cleartext ; décision écrite sur le pinning (déconseillé par Android Developers, à évaluer avec MASVS-NETWORK-2). | MASVS-NETWORK-1/2 | Vérification du manifeste et de l'Info.plist ; test d'interception. |
| SEC-08 | **Webhooks Stripe** : vérification de signature (`Stripe-Signature`, secret par point de terminaison) sur le corps brut ; rejet si la signature ou l'horodatage est invalide ; **idempotence** par `event.id` unique (table `stripe_events`) ; traitement tolérant au désordre des événements (relecture de l'objet chez Stripe si besoin). | API8/API10 | Tests : événement non signé → 400 ; même événement reçu deux fois → un seul effet. |
| SEC-09 | **Idempotence des appels sortants** vers Stripe (clé d'idempotence pour les paiements, remboursements et transferts). | Doc Stripe | Test : double clic ou nouvel essai réseau → un seul paiement ou transfert. |
| SEC-10 | **Aucune image biométrique stockée** par Volis : seulement `identity_status` et l'ID de session Stripe. Durée de conservation minimale configurée chez Stripe ; **effacement (redact) de la session Stripe Identity dès que la vérification est faite** (voir 3.1 ; la doc Stripe indique que l'effacement peut prendre jusqu'à 4 jours et émet `identity.verification_session.redacted`). | MASVS-PRIVACY-1 ; Loi 25 | Revue du schéma ; tests : aucun champ ni fichier d'image d'identité. |
| SEC-11 | **Données bancaires jamais saisies dans nos écrans** : onboarding hébergé Stripe ou composants intégrés ; Volis ne stocke que l'ID du compte connecté. Paiement par carte via PaymentSheet / Payment Element (les données de carte ne transitent pas par nos serveurs). | Fiche de recherche ; volet légal 5 | Revue de code ; aucun champ de numéro de compte ou de carte dans l'app. |
| SEC-12 | **Chiffrement au repos** de la base, du stockage et des sauvegardes (fourni par l'hébergeur, **à confirmer** dans sa documentation) ; chiffrement supplémentaire au niveau des colonnes pour les champs les plus sensibles si nécessaire. | MASVS-CRYPTO ; Loi 25 | Attestation de l'hébergeur ; revue de config. |
| SEC-13 | **Journalisation sans données personnelles** : identifiants techniques seulement ; masquage (scrubbing) dans Sentry ; aucun jeton, courriel, adresse ou contenu de message dans les journaux. Durées de conservation des journaux **à décider**. | MASVS-STORAGE-2 ; guide 5.4 | Test : recherche de motifs (courriel, jeton) dans les journaux = 0. |
| SEC-14 | **Limitation de débit** sur l'authentification, la réinitialisation, l'envoi de messages, la création d'annonces et les fonctions coûteuses ; quotas par utilisateur, IP et appareil. Seuils **à décider**. | API4/API6 | Test de charge ciblé : dépassement → 429. |
| SEC-15 | **Anti-fraude** : Stripe Radar sur les paiements ; **vérification d'identité obligatoire avant la première transaction** (expéditeur et voyageur, périmètre **à confirmer**) ; signalements d'utilisateurs ; suspension du transfert en cas d'alerte ; attestation d'app (Play Integrity / App Attest) à évaluer. | API6 ; MASVS-RESILIENCE | Test : réservation refusée sans `identity_status = verified`. |
| SEC-16 | **Modération** des photos et des messages : signalement depuis l'app, file de modération, blocage d'un utilisateur ; analyse automatique (service **à confirmer**). | MASVS-PLATFORM-3 ; exigences des stores sur le contenu des utilisateurs (**à confirmer**) | Test E2E : message signalé → masqué en attente de révision. |
| SEC-17 | **Photos** : compartiments privés ; URL signées de courte durée ; EXIF retiré ; types et tailles de fichiers validés côté serveur. | MASVS-CODE-4 ; PRIVACY | Test : URL d'une photo d'une autre réservation → refusée. |
| SEC-18 | **Sauvegardes** : sauvegardes automatiques et restauration testée ; fréquence et durée de rétention **à décider** selon l'offre de l'hébergeur. | Guide 5.5 | Exercice de restauration documenté avant le lancement. |
| SEC-19 | **Suppression du compte dans l'app** (exigée par Apple, règle 5.1.1(v)) et **export des données** dans un format structuré (portabilité, Loi 25). Les données soumises à une obligation de conservation (paiements, preuves de litige, consentements, registre des incidents) sont conservées selon le tableau 3.1, puis détruites ou anonymisées. | MASVS-PRIVACY-4 | Test E2E : suppression → session révoquée, données effacées ou anonymisées, export JSON disponible. |
| SEC-20 | **Plan de réponse aux incidents** : détection → confinement (révocation des jetons, désactivation de fonctions, version minimale) → correctif → évaluation du préjudice → avis à la CAI et aux personnes si risque de préjudice sérieux → **registre des incidents** (`security_incidents`). | Guide 5.5 ; Loi 25 | Exercice sur table avant le lancement. |
| SEC-21 | **Mise à jour forcée** : version minimale renvoyée par le backend, qui bloque les versions vulnérables. | MASVS-CODE-2 | Test : version inférieure au minimum → écran de mise à jour. |
| SEC-22 | **Tests de sécurité** : SAST (CodeQL ou Semgrep) et SCA (Dependabot/Renovate, `npm audit`, OSV-Scanner) à chaque PR ; scan de secrets ; analyse **MobSF** des builds de release ; **test d'intrusion par un tiers avant le lancement** (MASVS/MASTG + API). | MASVS-CODE-3 ; guide 2.6–2.7 | CI verte sans vulnérabilité critique ; rapport de pentest avec constats corrigés. |
| SEC-23 | **Liens profonds** validés comme des entrées non fiables ; Universal Links / App Links pour les retours d'onboarding Stripe et d'authentification ; aucun jeton dans un lien. | MASVS-PLATFORM-1 | Test : lien forgé → aucune action sensible sans confirmation. |
| SEC-24 | **Permissions minimales**, demandées en contexte (localisation, caméra, photos, notifications) ; sélecteur de photos du système de préférence. | MASVS-PRIVACY-1 | Revue des permissions déclarées ; fiches vie privée des stores cohérentes. |
| SEC-25 | **Purge et conservation automatisées** : tâches planifiées (par ex. `pg_cron` ou fonction planifiée, **à confirmer**) qui appliquent les durées du tableau 3.1, puis détruisent ou anonymisent les données ; **gel légal** (`legal_hold`) qui suspend la purge des éléments liés à un litige ou à une rétrofacturation en cours ; journal des purges sans données personnelles. | MASVS-PRIVACY-4 ; Loi 25 (art. 23) | Test automatisé en CI : données fictives datées → purgées ou anonymisées à l'échéance ; données sous gel légal → conservées ; session Identity vérifiée → redact demandé. |

### 3.1 Durées de conservation et purge (SEC-19, SEC-25)

> **À faire valider par l'avocat.** Durées fournies par l'équipe juridique. Le point de départ de chaque délai doit être stocké explicitement (date de fin d'année fiscale, date de livraison, date de prise de connaissance de l'incident, date de fermeture du compte).

| Données | Durée de conservation | Fondement (selon l'équipe juridique) | Mise en œuvre technique |
|---|---|---|---|
| Paiements, factures, commissions | 6 ans après la fin de l'année fiscale concernée | Lois fiscales fédérale et québécoise | Tables `payments`, `transfers`, reçus ; purge annuelle après l'échéance. Les objets chez Stripe suivent les règles de Stripe. |
| Preuves de litige (photos de remise, confirmations, messages liés) | 3 ans après la livraison ; **prolongé si un litige est en cours** | Prescription, C.c.Q. art. 2925 | `delivery_proofs`, `dispute_evidence`, messages rattachés ; gel légal actif tant que le litige ou la rétrofacturation n'est pas clos. |
| Registre des incidents de confidentialité | 5 ans à partir de la prise de connaissance de l'incident | Règlement de la Loi 25 | `security_incidents.discovered_at` comme point de départ. |
| Preuves de consentement | Toute la durée du compte, puis 3 ans | Équipe juridique | Table `consents` (finalité, version du texte, date, retrait) ; purge 3 ans après la fermeture du compte. |
| Géolocalisation et messages **sans litige** | Supprimés dès la fin de la livraison et du délai de contestation | Minimisation (Loi 25) | Purge déclenchée par la transition vers « Fonds libérés » (délai de contestation écoulé), sauf gel légal. |
| Session Stripe Identity | Effacée dès que la vérification est faite | Minimisation (Loi 25) ; biométrie | Appel `redact` à la réception de `identity.verification_session.verified` ; Volis ne garde que `identity_status` et l'ID de session. Traitement après un échec définitif : **à faire valider par l'avocat**. |

**Après ces délais : destruction ou anonymisation** (Loi 25, art. 23). L'anonymisation doit être irréversible ; sinon, on détruit.

Exigences techniques (SEC-25) :

- **Tâches de purge planifiées**, idempotentes, exécutées côté serveur, avec un journal (catégorie, nombre d'éléments, date) sans données personnelles. Les fichiers du stockage sont supprimés en même temps que leurs lignes.
- **Gel légal** : table `legal_holds` (ressource, motif, ouvert le, levé le), posé automatiquement à `charge.dispute.created` et à l'ouverture d'un litige interne, levé à la clôture. Toute purge vérifie l'absence de gel.
- **Sauvegardes** : leur durée de rétention doit rester compatible avec ces délais (une donnée purgée disparaît des sauvegardes à leur expiration) : **à confirmer** selon l'offre Supabase.
- **Test automatisé** en CI (critère de SEC-25).

## 4. Monétisation — partie technique

> Cette section décrit **comment** implémenter les sources de revenus. Le **cadre légal** (prix tout inclus, divulgation, assurance, taxes, remboursements, rétrofacturations, abonnements) est traité dans la section de l'équipe juridique, « Volet légal de la monétisation » (`cahier-legal-monetisation.md`), à laquelle ce texte renvoie. **Tous les montants et taux (commission, marge, primes, prix d'abonnement) restent à décider par Faycal.**

### 4.1 Prix tout inclus et détail avant paiement

Voir volet légal, section 2.

- Le **serveur calcule** le détail du prix et le fige dans la réservation (`bookings`) : prix du transport, commission Volis, assurance si choisie, TPS/TVQ, total. L'app ne fait qu'afficher ce détail. Elle ne recalcule rien qui serve à facturer.
- Le prix affiché dans les listes et les fiches inclut tous les frais obligatoires. Seules les taxes s'ajoutent, conformément au volet légal.
- L'écran de confirmation (équipe UI) affiche le détail reçu du serveur. Le `PaymentIntent` est créé pour **exactement** le total figé ; toute différence bloque le paiement.
- Les montants sont stockés en unités mineures entières avec leur code de devise. Arrondis et règles de calcul des taxes : **à confirmer avec le comptable**.
- **Reçus en français** (volet légal 2) générés par le serveur avec les numéros de TPS/TVQ dès l'inscription ; copie du contrat transmise à l'utilisateur (gabarit fourni par l'équipe juridique).

### 4.2 Commission de la plateforme

Voir volet légal, sections 1 et 3.

- Avec **separate charges and transfers**, il n'y a pas d'`application_fee_amount` standard sur le transfert. La plateforme **transfère au voyageur un montant inférieur au paiement**, et la différence reste sur son solde (doc Stripe « Collect fees when using separate charges and transfers »). La commission Volis = total payé − taxes perçues par Volis − part versée au voyageur − assurance reversée au partenaire. La formule exacte des taxes est **à confirmer avec le comptable**.
- Stripe propose une fonction de « funds segregation » (aperçu privé) qui permet un `application_fee_amount` sur le transfert. Elle est optionnelle et sur demande auprès de Stripe : **à confirmer**.
- Les frais de traitement Stripe sont débités du solde de la plateforme. Ils doivent être pris en compte dans le calcul, mais **pas** affichés comme « frais de Stripe » s'ils contiennent une marge (volet légal 5).
- Stripe recommande ce type de paiement seulement si la plateforme assume les soldes négatifs de ses comptes connectés (doc Stripe). Cela a un impact sur la configuration de Connect et sur la gestion des risques.
- Le modèle de comptabilité interne (registre `payments` / `transfers` / commission) permet de rapprocher chaque réservation avec les rapports Stripe.

### 4.3 Frais de versement instantané

Voir volet légal, section 5.

- Stripe permet de monétiser les versements instantanés de Connect par des **frais d'application** (méthode recommandée par Stripe) ou par un débit du compte, configurables avec le **Platform Pricing Tool**. Stripe facture aussi des frais à la plateforme pour chaque versement instantané (voir la grille tarifaire de Stripe Connect). Applicabilité exacte à la configuration de Volis : **à confirmer avec Stripe**.
- L'écran de versement montre les frais **avant** que le voyageur choisisse. Le **virement standard sans frais Volis reste toujours offert**. Si une marge s'ajoute aux frais de Stripe, elle est libellée comme frais Volis.
- Admissibilité : seulement si le compte connecté a une carte de débit admissible. Le statut est lu chez Stripe (`account.updated`) et non déduit par l'app.
- Statuts « en cours → déposé » alimentés par `payout.*` (point de terminaison Connect).

### 4.4 Assurance optionnelle via un partenaire

Voir volet légal, section 4. Le partenaire, son API et le mode de distribution (option A « recommandation » ou option B « distribution sans représentant ») sont **à confirmer**.

- **Option A** : lien ou redirection vers l'assureur, qui vend et encaisse lui-même. Côté technique : lien de recommandation suivi, puis retour éventuel d'un statut de police par API ou webhook du partenaire (**à confirmer**). Aucun encaissement de prime par Volis.
- **Option B** : intégration API avec l'assureur (devis, émission, annulation). Le traitement de la prime (encaissée par Volis puis reversée, ou par l'assureur) est **à confirmer avec l'avocat et l'assureur** avant toute conception du flux de paiement.
- Exigences d'interface reprises du volet légal : case **non cochée d'avance**, prix montré à part, limites, exclusions et plafond affichés près de la valeur déclarée ; jamais obligatoire.
- Données transmises à l'assureur : minimales, couvertes par l'ÉFVP et le consentement (Loi 25).

### 4.5 Mises en avant ou abonnement (plus tard)

Voir volet légal, section 6 (contrats à exécution successive).

- **Mise en avant d'une annonce** : achat ponctuel par un `PaymentIntent` de la plateforme (sans transfert) ; durée et prix **à décider**.
- **Abonnement** : **Stripe Billing** (produits, prix, abonnements, portail client) ; webhooks `customer.subscription.*` et `invoice.*`. Le serveur contrôle les droits (jamais une simple valeur « premium » dans l'app, voir guide 2.2.3).
- Avis avant renouvellement, résiliation et prix clair : selon le volet légal.
- Si un achat se fait dans l'app mobile pour un contenu ou une fonction numérique, les règles des stores sur les achats intégrés peuvent s'appliquer : **à confirmer** avant de concevoir ces offres.

### 4.6 Remboursements et litiges

Voir volet légal, section 6.

- Remboursement total ou partiel par `Refund` sur le paiement de la plateforme. S'il a déjà eu lieu, un transfert peut être annulé (reversal) selon les conditions acceptées par le voyageur (**à confirmer avec l'équipe juridique**).
- Quels frais sont remboursés : paramétrable côté serveur selon la politique de remboursement finale (volet légal).
- **Rétrofacturations** : à `charge.dispute.created`, le serveur assemble les preuves (photos de remise, confirmations horodatées, messages pertinents) pour la réponse à Stripe. Perte assumée selon les conditions (volet légal 6).
- **Encaissement des fonds** : le modèle « separate charges and transfers » fait transiter l'argent par le solde Stripe de Volis. Statut au regard de la Loi sur les activités associées aux paiements de détail : **à confirmer par l'avocat** (volet légal 6). Ne pas modifier ce flux sans cet avis.

## 5. Exigences non fonctionnelles

Les objectifs chiffrés ci-dessous sont **à définir** avec Faycal avant le MVP. Ce document fixe les indicateurs à mesurer, pas leurs seuils.

| Domaine | Exigence | Mesure |
|---|---|---|
| Performance | Démarrage, temps d'affichage des listes de trajets et temps de réponse des API mesurés en continu ; pagination de toutes les listes ; images redimensionnées côté serveur. | Sentry Performance ; seuils **à définir**. |
| Disponibilité | Objectif de disponibilité **à définir** ; dégradation contrôlée si Stripe ou le push est indisponible (les webhooks sont rejoués par Stripe, idempotence SEC-08). | Surveillance de disponibilité ; alertes. |
| Accessibilité | **WCAG 2.2 niveau AA** pour l'app et le web : contrastes, tailles des cibles, libellés des lecteurs d'écran (VoiceOver, TalkBack), navigation au clavier sur le web, respect de la taille de texte du système, mise en page RTL correcte en arabe. | Audit d'accessibilité avant le lancement ; tests automatisés sur le web (**outil à confirmer**). |
| Hors-ligne partiel | Lecture des réservations, de l'historique et des messages déjà chargés hors connexion ; prise de photos de remise mise en file d'attente et envoyée au retour du réseau ; **aucune transition de paiement ni de statut validée hors ligne** (le serveur reste l'arbitre). Cache local sans données sensibles, purgé à la déconnexion. | Tests E2E en mode avion. |
| Compatibilité | Versions minimales d'iOS et d'Android : **à confirmer** selon la version du SDK Expo retenue. Navigateurs web : versions récentes des principaux navigateurs (**liste à confirmer**). | Matrice d'appareils de test. |
| Conformité stores 2026 | **Google Play : cibler l'API 36 (Android 16)** pour toute nouvelle app ou mise à jour depuis le 31 août 2026. **Apple : builds avec Xcode 26 et le SDK iOS 26** depuis le 28 avril 2026. Compatibilité de la version du SDK Expo retenue avec ces exigences : **à confirmer**. Fiches Sécurité des données (Google) et étiquettes de confidentialité + privacy manifest (Apple) exactes. | Vérification à chaque release (pages officielles « Target API level requirements » et « Upcoming Requirements »). |
| Internationalisation | fr, en, ar (RTL) ; formats de date, nombre et devise selon la langue ; textes légaux en français disponibles en priorité. | Revue linguistique ; tests visuels RTL. |
| Maintenabilité | TypeScript strict ; lint et formatage ; tests unitaires (domaine, ViewModels), tests RLS, tests E2E des parcours critiques (inscription, vérification, réservation, paiement, remise, litige). | Couverture des parcours critiques en CI. |

## 6. Environnements, jalons et risques

### 6.1 Environnements

| Environnement | Backend | Stripe | App | Données |
|---|---|---|---|---|
| **dev** | Supabase local (CLI) ou projet de dev | Mode test, Stripe CLI pour les webhooks | Build de développement (Expo) | Fictives |
| **staging** | Projet Supabase séparé (même région que la prod), mêmes migrations | Mode test (ou bac à sable), webhooks réels de test | Profil EAS « preview » ; TestFlight et piste de test interne Google Play | Fictives ; aucune donnée réelle |
| **prod** | Projet Supabase de production, région **Canada (Central)** `ca-central-1`, accès restreint | **Mode production** (live), clés et secrets distincts | Profil EAS « production » ; App Store et Google Play | Réelles ; ÉFVP et sauvegardes en place |

Règles : secrets distincts par environnement dans les secrets de la CI et d'EAS ; migrations SQL appliquées dans l'ordre dev → staging → prod ; aucune copie de données de prod vers les autres environnements.

### 6.2 Plan de livraison en jalons

Les dates sont **à définir**. L'ordre tient compte des préalables légaux de la fiche de recherche (notamment la déclaration de la banque biométrique à la CAI au moins 60 jours avant la mise en service).

| Jalon | Contenu | Préalables |
|---|---|---|
| **J0 — Cadrage** | Modèle de menaces STRIDE ; inventaire des données ; début de l'ÉFVP ; choix définitifs (cartes, analytics, i18n) ; compte Stripe et Connect configurés en test ; squelette Expo + Supabase + CI. | Avis initial de l'avocat ; calendrier de la déclaration à la CAI. |
| **J1 — MVP Canada** | Inscription/connexion (PKCE), profil, Stripe Identity, annonces de trajet et demandes d'envoi, réservation, paiement retenu (separate charges and transfers), preuves de remise, livraison, libération des fonds, versements standard, messagerie simple, avis, signalements, litige de base, suppression du compte et export, fr/en, notifications push. | ÉFVP terminée ; politiques publiées ; Stripe en production ; pentest fait ; comptes stores ; déclaration à la CAI faite dans les délais. |
| **J2 — Version 1.1** | Versement instantané avec frais affichés ; assurance optionnelle (selon l'option A ou B validée) ; modération automatique ; amélioration du hors-ligne. | Contrat avec l'assureur ; avis juridique sur la distribution. |
| **J3 — Version 1.2** | Arabe (RTL) ; devises locales ; mises en avant ou abonnement (Stripe Billing) si retenus. | Volet légal sur les contrats à exécution successive. |
| **J4 — International** | Ouverture pays par pays selon la disponibilité de Stripe Connect et Stripe Identity ; exigences locales (RGPD, DSA, DAC7 en Europe) ; pays sous sanctions exclus. | Avocat local par pays. |
| **Plus tard** | Interac (VoPay / Zum Rails) seulement après avis d'avocat (CANAFE, AMF, Banque du Canada). | Avis juridique. |

### 6.3 Estimation qualitative des risques techniques

| Risque | Probabilité | Impact | Atténuation |
|---|---|---|---|
| Erreur dans la logique de libération des fonds (double transfert, transfert sans livraison) | Moyenne | Élevé | Machine d'états côté serveur, idempotence, tests automatisés, rapprochement avec Stripe, revue de code obligatoire. |
| Faille d'autorisation (RLS absente ou trop permissive) | Moyenne | Élevé | Tests RLS en CI, aucune table sans politique, pentest. |
| Fraude (faux comptes, cartes volées, colis interdits) | Moyenne | Élevé | Stripe Identity avant la première transaction, Radar, signalements, suspension des transferts, attestation du contenu. |
| Rétrofacturations après le transfert au voyageur | Moyenne | Moyen à élevé | Délai avant libération (à décider), preuves de remise, reversal selon les conditions. |
| Limites de Stripe (durée de détention des fonds, pays pris en charge, versements transfrontaliers) | Moyenne | Moyen | Validation avec Stripe avant J1 et avant chaque nouveau pays (**à confirmer**). |
| Changements d'exigences des stores (API cible, SDK, confidentialité) | Élevée (annuelle) | Moyen | Veille, mise à jour régulière du SDK Expo, vérification à chaque release. |
| Dépendance à Supabase (fournisseur unique) | Faible à moyenne | Moyen | PostgreSQL standard, logique métier en TypeScript, migrations versionnées, sauvegardes exportables. |
| Fuite de données personnelles (journaux, photos, messages) | Faible à moyenne | Élevé | SEC-13, SEC-17, chiffrement, registre et plan d'incident. |
| Complexité de l'interface RTL et du multilingue | Moyenne | Faible à moyen | RTL prévu dès le design system ; tests visuels. |
| Différences de comportement entre mobile et web (Expo Router, Stripe, cartes) | Moyenne | Moyen | Composants spécifiques par plateforme isolés dans la couche data/UI ; tests E2E web et mobile. |
| Retard dû aux préalables légaux (ÉFVP, CAI 60 jours, avis juridiques) | Moyenne | Moyen | Démarrage des démarches à J0, en parallèle du développement. |

## Annexe — Références officielles

- Expo Router : https://docs.expo.dev/router/introduction/
- Expo Notifications : https://docs.expo.dev/versions/latest/sdk/notifications/
- Expo SecureStore : https://docs.expo.dev/versions/latest/sdk/securestore/
- EAS Build : https://docs.expo.dev/build/introduction/ · EAS Submit : https://docs.expo.dev/submit/introduction/
- Stripe Connect, types de paiements : https://docs.stripe.com/connect/charges
- Separate charges and transfers : https://docs.stripe.com/connect/separate-charges-and-transfers
- Frais de plateforme (application fees) : https://docs.stripe.com/connect/marketplace/tasks/app-fees
- Durée des autorisations de carte : https://docs.stripe.com/payments/place-a-hold-on-a-payment-method
- Versements instantanés Connect : https://docs.stripe.com/connect/instant-payouts
- Platform Pricing Tool : https://docs.stripe.com/connect/platform-pricing-tools
- Stripe Identity, résultats de vérification : https://docs.stripe.com/identity/handle-verification-outcomes
- Stripe Identity, sessions et effacement : https://docs.stripe.com/identity/verification-sessions
- Webhooks Stripe : https://docs.stripe.com/webhooks
- Types d'événements Stripe : https://docs.stripe.com/api/events/types
- Stripe Billing : https://docs.stripe.com/billing
- Supabase, régions disponibles : https://supabase.com/docs/guides/platform/regions · Invocations régionales : https://supabase.com/docs/guides/functions/regional-invocation
- Supabase Auth : https://supabase.com/docs/guides/auth · RLS : https://supabase.com/docs/guides/database/postgres/row-level-security
- OWASP MASVS : https://mas.owasp.org/MASVS/ · MASTG : https://mas.owasp.org/MASTG/
- OWASP API Security Top 10 (2023) : https://owasp.org/API-Security/
- WCAG 2.2 : https://www.w3.org/TR/WCAG22/
- Google Play, niveau d'API cible : https://support.google.com/googleplay/android-developer/answer/11926878
- Apple, exigences à venir : https://developer.apple.com/news/upcoming-requirements/


# Partie C — Volet légal de la monétisation

*Préparé par Legal Team — 11 octobre 2026*

> **Avertissement.** Ce texte est une synthèse informative. Il ne constitue ni un avis juridique, ni un avis fiscal, ni un avis financier. Tout doit être validé par un avocat membre du Barreau du Québec, et par un comptable pour la fiscalité, avant le lancement.

## 1. Sources de revenus prévues

| Source | Qui paie | Comment Stripe l'encaisse (voir section technique) |
|---|---|---|
| Commission sur chaque livraison | L'expéditeur, ou une part du montant versé au voyageur | Frais de plateforme prélevés par Stripe Connect |
| Assurance optionnelle du colis | L'expéditeur, s'il choisit l'option | Prime versée à l'assureur partenaire. Volis touche au plus une rémunération que l'assureur lui verse et qui doit être divulguée |
| Frais de versement instantané | Le voyageur, s'il choisit le versement instantané | Frais de Stripe, avec une éventuelle marge pour Volis |
| Option future : abonnement ou mise en avant | Selon l'offre | À encadrer avant de lancer (voir 6) |

## 2. Prix et transparence (Loi sur la protection du consommateur et Loi sur la concurrence)

- **Prix total annoncé.** Le prix montré doit inclure tous les frais obligatoires : commission, frais de service et frais de traitement. Seules la TPS et la TVQ peuvent s'ajouter (LPC, art. 224 c). La Loi sur la concurrence interdit aussi d'annoncer un prix partiel en ajoutant des frais obligatoires plus tard.
- **Détail avant paiement.** Avant de payer, l'utilisateur doit voir le prix du transport, la commission de Volis, l'assurance si elle est choisie, les taxes et le total. Ce détail correspond à l'écran de paiement de la partie A (écran 11).
- **Contrat conclu à distance** (LPC, art. 54.1 et suivants). Avant la conclusion, l'utilisateur doit recevoir certaines informations : l'identité et l'adresse de Volis, une description du service, le prix détaillé, les modalités de paiement et la politique d'annulation et de remboursement. Il faut ensuite lui transmettre une copie du contrat dans les 15 jours. Si ces informations manquent, le consommateur peut annuler le contrat et demander une rétrofacturation à l'émetteur de sa carte.
- **Pas de publicité trompeuse** (LPC, art. 219 et suivants). Les messages comme « livraison garantie » ou « assuré » sont interdits si l'assurance n'est pas choisie.
- **Langue.** Les prix, les reçus, les factures et les conditions doivent être en français (Charte de la langue française).

## 3. Commission de la plateforme

- **Rôle d'intermédiaire.** Les conditions d'utilisation doivent dire clairement que la commission paie un service de mise en relation et de paiement, pas un service de transport.
- **Statut des voyageurs.** Les voyageurs sont des utilisateurs autonomes. Volis ne doit pas leur imposer d'horaires, de quotas ni de prix fixes, sinon un tribunal pourrait les considérer comme des salariés (Loi sur les normes du travail, cotisations sociales). Les règles de sécurité et la liste d'objets interdits restent permises.
- **Taxes sur la commission.** La commission et les frais de service sont des fournitures taxables. Volis doit s'inscrire à la TPS/TVQ dès que ses revenus dépassent 30 000 $ sur quatre trimestres civils consécutifs, ou plus tôt de façon volontaire. Les reçus doivent indiquer les numéros de TPS et de TVQ. **À confirmer avec un comptable :** les règles qui obligent les exploitants de plateformes numériques à percevoir les taxes à la place de certains fournisseurs pourraient s'appliquer à Volis.
- **Revenus des voyageurs.** Ils sont imposables pour les voyageurs. Le régime de déclaration de l'ARC pour les plateformes (en vigueur depuis 2024) pourrait obliger Volis à déclarer chaque année ce que touchent les voyageurs. **À confirmer avec un comptable.** Il faut donc prévoir dès maintenant de recueillir les renseignements requis (nom, adresse, NAS ou numéro d'entreprise), avec le consentement prévu par la Loi 25.

## 4. Assurance optionnelle

- **Ce que Volis ne doit pas faire.** Vendre de l'assurance en son propre nom ou conseiller les utilisateurs sur une assurance, à moins d'être inscrit auprès de l'AMF.
- **Option A, la plus simple : la recommandation.** Volis renvoie l'utilisateur vers l'assureur partenaire, qui vend lui-même l'assurance. Si l'assureur verse une rémunération de recommandation à Volis, il faut l'encadrer par contrat et la divulguer à l'utilisateur.
- **Option B : la distribution sans représentant** (Loi sur la distribution de produits et services financiers, titre VIII). Ce régime permet de proposer une assurance liée au service. L'assureur doit l'avoir déclaré à l'AMF, Volis doit remettre le guide de distribution de l'assureur et l'utilisateur garde un droit de résolution prévu par la loi. **À valider avec l'avocat et l'assureur.**
- **Interface.** Il faut une case d'acceptation qui n'est pas cochée d'avance, un prix montré à part, et les limites, exclusions et plafonds écrits clairement. L'assurance ne doit jamais être obligatoire pour utiliser le service.
- **Lien avec la politique de litiges.** Le plafond d'indemnisation de Volis s'applique quand l'assurance n'est pas choisie. Il ne peut jamais servir à exclure la responsabilité de Volis pour une faute lourde ou intentionnelle, ni pour un préjudice corporel ou moral (C.c.Q., art. 1474).

## 5. Frais de versement instantané

- Le montant ou le pourcentage doit être montré avant que le voyageur choisisse. Le virement standard gratuit reste toujours offert.
- Si Volis ajoute une marge aux frais de Stripe, elle doit être divulguée. Le terme « frais de Stripe » ne peut pas désigner un montant qui contient une marge pour Volis.
- Les données bancaires sont saisies seulement dans l'inscription hébergée par Stripe, et jamais sur les serveurs de Volis (Loi 25, minimisation des données).

## 6. Paiement retenu, remboursements et litiges

- **Encaissement des fonds.** Avec les « separate charges and transfers » de Stripe Connect, l'argent transite par le solde Stripe de Volis. Il faut faire confirmer par l'avocat que Volis peut compter sur l'inscription de Stripe comme fournisseur de services de paiement, ou qu'une exemption s'applique. Sinon, Volis devrait peut-être s'inscrire elle-même à la Banque du Canada (Loi sur les activités associées aux paiements de détail).
- **Politique de remboursement.** Elle doit préciser quand un remboursement s'applique (annulation, colis non remis), son délai, et quels frais sont remboursés ou non. Une clause qui empêcherait le consommateur d'exercer ses recours prévus par la LPC est sans effet.
- **Rétrofacturations.** Il faut prévoir comment Volis répond aux contestations de carte, en joignant les preuves de remise (photos et confirmation). Il faut aussi prévoir qui assume la perte, sans la transférer au voyageur sans son accord prévu dans les conditions.
- **Abonnement ou mise en avant payante (plus tard).** Ce sont des contrats à exécution successive selon la LPC. Il faudra des règles sur la résiliation, un avis avant chaque renouvellement automatique et un prix clair.

## 7. Marketing et données

- **Courriels et notifications promotionnels.** Ils demandent un consentement exprès, un lien de désabonnement et l'identification de l'expéditeur (LCAP, la loi anti-pourriel).
- **Publicité ciblée ou traçage.** La Loi 25 exige que ce soit désactivé par défaut avec un consentement distinct. Il faut aussi les fiches vie privée des stores.
- **Pas de vente de données personnelles** sans consentement exprès.
- **Sous-traitants qui reçoivent des données** : Stripe (paiements et vérification d'identité), Sentry (suivi des erreurs), le service de notifications d'Expo, l'outil d'analytics s'il y en a un, et l'assureur partenaire. Chacun doit figurer dans l'évaluation des facteurs relatifs à la vie privée (ÉFVP) et dans la politique de confidentialité, avec un contrat de traitement des données. Ceux qui traitent les données hors du Québec doivent faire l'objet d'une évaluation du transfert (Loi 25, art. 17). Supabase est hébergé au Canada (Central).

## 8. Clauses à prévoir dans les conditions d'utilisation

1. L'objet du service : une mise en relation et un paiement sécurisé, pas un service de transport.
2. Le prix, la commission, les taxes et le moment du prélèvement.
3. Le paiement retenu, sa libération à la remise et ses délais.
4. L'annulation, le remboursement et les frais non remboursables, dans les limites de la LPC.
5. La valeur déclarée, le plafond d'indemnisation et le renvoi à l'assurance optionnelle.
6. Les objets interdits, l'attestation du contenu et la responsabilité douanière du voyageur, présentée comme une information.
7. Les frais de versement et les conditions de Stripe Connect, que l'utilisateur accepte.
8. La suspension et la fermeture du compte, avec la suppression de compte dans l'application.
9. Le droit applicable (Québec) et la juridiction. Une clause d'arbitrage obligatoire est interdite pour les consommateurs québécois (LPC, art. 11.1).
10. La modification des conditions, avec un préavis aux utilisateurs.

## 9. À faire valider par l'avocat et le comptable

- [ ] Le mode de distribution de l'assurance (option A ou B) et la rémunération reçue de l'assureur.
- [ ] La perception de la TPS/TVQ par Volis comme plateforme, et la déclaration à l'ARC des revenus des voyageurs.
- [ ] Le statut de Volis selon la loi sur les paiements de détail, avec le modèle Stripe Connect.
- [ ] Le statut de travailleur autonome des voyageurs.
- [ ] L'ÉFVP et l'évaluation des transferts pour chaque sous-traitant (Stripe, Sentry, Expo, analytics, assureur).
- [ ] La version finale des conditions d'utilisation, de la politique de remboursement et de litiges, et de la politique de confidentialité.
