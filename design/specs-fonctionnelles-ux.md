---
title: "Volis — Cahier des charges, section : Spécifications fonctionnelles et UX"
subtitle: "Préparé par l’équipe UI/UX — 11 octobre 2026"
lang: fr-CA
---

> **Portée de cette section.** Elle décrit ce que l’application doit faire du point de vue de l’utilisateur : rôles, parcours, histoires utilisateur, critères d’acceptation, états et cas limites, accessibilité, localisation et événements analytiques. Elle s’appuie sur les 50 maquettes du concept 1 « Carnet de voyage » (`volis-design/ecrans/`, numérotées 01 à 50) et sur la charte graphique (`volis-charte-graphique.pdf`). La technique (machine d’états, Stripe, sécurité) relève du volet technique; le cadre légal, du volet légal. Les renvois sont indiqués entre parenthèses.
>
> **Convention.** Les montants, taux, délais et plafonds visibles dans les maquettes (commission de 15 %, 1,5 % pour le versement instantané, protection de base de 100 $, valeur déclarée maximale de 1 000 $, délai de signalement de 72 h, etc.) sont **illustratifs**. Ils restent **à décider par Faycal**, puis à faire valider par l’équipe juridique quand c’est nécessaire. Tous les noms et numéros sont fictifs.

# 1. Rôles et principes

## 1.1 Rôles

| Rôle | Description | Compte requis | Vérification |
|---|---|---|---|
| **Visiteur** | Parcourt les trajets et les prix sans compte (« Explorer sans compte », écran 05). | Non | — |
| **Expéditeur** | Crée un envoi, choisit un voyageur, paie en séquestre, remet le colis, suit la livraison, laisse un avis. | Oui | Courriel + téléphone; identité (Stripe Identity) avant le 1er paiement (SEC-15). |
| **Voyageur** | Publie un voyage, accepte ou refuse les demandes, inspecte et transporte le colis, reçoit ses gains via Stripe Connect. | Oui | Courriel + téléphone + identité; vol confirmé (billet vérifié) pour le badge « Vol confirmé »; compte Stripe Connect avant le 1er versement. |
| **Destinataire** | Reçoit le colis à l’arrivée. Suit l’envoi par un lien web et donne le code de réception. | Non (lien de suivi) | Téléphone (reçoit le texto) |
| **Agent soutien / modération** (interne) | Traite les litiges, signalements, vérifications manuelles. | Outil interne | MFA obligatoire |

Un même compte peut être expéditeur et voyageur. Le rôle n’est pas un réglage : il découle de l’action (« J’envoie un colis » / « Je voyage », écran 07). Le choix de rôle à l’inscription (écran 06) sert seulement à personnaliser l’accueil.

## 1.2 Principes UX (rappel de la charte)

1. **Confiance visible au bon moment** : identité vérifiée, séquestre et preuves de remise sont rappelés à chaque décision (paiement, remise, acceptation).
2. **Une action principale par écran**, en bas, pleine largeur, libellée par un verbe précis (« Payer 32,06 $ »).
3. **Prix tout inclus, détail avant paiement** (volet légal 2; volet technique 4.1) : le prix affiché dans les listes inclut tous les frais obligatoires; seules les taxes s’ajoutent.
4. **Jamais de données bancaires ni biométriques dans nos écrans** : Stripe Identity et Stripe Connect sont hébergés (SEC-10, SEC-11).
5. **Accessible par défaut** : WCAG 2.2 AA, cibles 44 pt, texte dynamique (section 6).

# 2. Navigation et architecture de l’information

- **Barre d’onglets** (5 onglets fixes) : Accueil · Envois · Voyages · Messages · Profil. L’onglet actif est indiqué par une pilule sarcelle claire, un libellé gras et `accessibilityState.selected`. Une pastille corail signale du non lu (Messages, Notifications).
- **Piles de navigation** par onglet; les flux transactionnels (créer un envoi, paiement, remise, vérification) s’ouvrent en plein écran sans barre d’onglets, avec retour et un indicateur d’étape.
- **Feuilles modales** (bottom sheets) pour les choix secondaires : filtres (38), assurance (40), tri. Fermeture par glissement, bouton « Fermer » et geste retour Android.
- **Liens profonds** (SEC-23) : `volis://envoi/{id}`, `volis://voyage/{id}`, `volis://remise/{id}`, retour Stripe Identity et Stripe Connect par Universal Links / App Links. Le lien de suivi destinataire est une page web (`volis.app/s/{code}`).

# 3. Parcours et histoires utilisateur

Format : **US-xx** « En tant que…, je veux…, afin de… » puis critères d’acceptation (CA) vérifiables. Les écrans sont cités par leur numéro.

## 3.1 Parcours A — Accueil, inscription et connexion (écrans 01–06, 23–25)

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

## 3.2 Parcours B — Vérification d’identité (écrans 17–22)

**US-10 — Vérifier mon identité.** En tant qu’utilisateur, je veux faire vérifier mon identité afin d’envoyer ou de transporter un colis.
- CA1 : l’intro (17) explique les 3 étapes et la durée (~2 min) avant tout traitement.
- CA2 : **consentement exprès et distinct** à la biométrie (18) : quoi, pourquoi, qui (Stripe), où (hors Québec, le cas échéant), durée (gabarit supprimé après la vérification), droits; case non cochée par défaut; bouton désactivé tant qu’elle ne l’est pas; alternative « vérification manuelle sans biométrie » toujours offerte (Loi 25; SEC-10). Le consentement est horodaté avec la version du texte (table `consents`).
- CA3 : la capture se fait sur la page hébergée Stripe Identity (19), présentée comme une page externe (barre d’adresse visible).
- CA4 : trois résultats : **Vérifiée** (20), **En cours d’examen** (21, notification à la fin), **Échec** (22, raison lisible issue de `last_error.reason`, conseils, nombre d’essais restants, voie manuelle).
- CA5 : Volis ne stocke que `identity_status` et l’ID de session; la session est effacée (redact) dès la vérification (SEC-10, tableau 3.1).

## 3.3 Parcours C — Recherche et réservation (écrans 07–11, 36, 38–40)

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

## 3.4 Parcours D — Demande, remise et suivi (écrans 12–14, 26–30, 33, 37, 43, 50)

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

## 3.5 Parcours E — Côté voyageur (écrans 15, 26, 31, 49)

**US-40 — Publier un voyage.** CA1 : trajet, date, vol (numéro facultatif, billet joint en privé pour le badge « Vol confirmé »), capacité en kg, catégories acceptées, prix par kg avec suggestion (15). CA2 : le billet n’est jamais visible par les expéditeurs. CA3 : publication modifiable tant qu’aucune demande n’est acceptée.

**US-41 — Gérer mes voyages.** CA1 : liste (31) : capacité acceptée / en attente / libre, demandes à traiter, gain prévu. CA2 : annuler un voyage avec demandes acceptées déclenche le parcours de réattribution pour chaque expéditeur (US-50).

## 3.6 Parcours F — Imprévus, litiges et aide (écrans 34, 35, 44, 45)

**US-50 — Vol retardé ou annulé.** En tant qu’expéditeur, je veux savoir quoi faire si le vol est annulé afin de ne pas perdre mon argent.
- CA1 : notification immédiate; écran (34) avec le vol annulé, rappel « Votre argent est protégé ».
- CA2 : trois choix : réattribuer à un autre voyageur (prix égal ou inférieur), garder le voyageur sur son nouveau vol, remboursement total.
- CA3 : un simple retard ne demande aucune action; on avertit à chaque changement.
- CA4 : sans choix de l’expéditeur dans un délai (à décider), remboursement automatique.

**US-51 — Ouvrir un litige.** CA1 : motif (endommagé, manquant, non livré, autre), description, photos de l’utilisateur + **preuves automatiques** (photos de remise horodatées) (35). CA2 : indemnisation possible affichée : protection de base (sans assurance) ou couverture de l’assurance, plafonnée à la valeur déclarée. CA3 : délai de signalement et délai de réponse affichés; transfert au voyageur gelé pendant l’examen (`legal_holds`, SEC-25). CA4 : la décision est notifiée avec explication et recours.

**US-52 — Trouver de l’aide.** CA1 : centre d’aide (44) avec recherche, catégories, FAQ, contact soutien (délai moyen affiché) et **urgence sécurité** distincte. CA2 : liste des objets interdits et sous conditions (45), aussi accessible depuis la création d’envoi et l’attestation douane.

## 3.7 Parcours G — Profil, argent et réglages (écrans 16, 32, 41, 42, 46–48)

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

# 4. Inventaire des écrans

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

# 5. États et cas limites

## 5.1 États transverses (tous les écrans de données)

| État | Traitement |
|---|---|
| Chargement | Squelettes aux dimensions du contenu (pas de spinner plein écran au-delà de 300 ms); boutons en état « chargement » pendant une action. |
| Vide | Illustration + explication + action utile (36). Jamais un écran blanc. |
| Erreur réseau | Toast « Hors ligne · on réessaie automatiquement »; données en cache affichées avec la date de dernière synchro; actions d’argent bloquées hors ligne (sauf code de remise, 37). |
| Erreur serveur | Message humain + « Réessayer »; identifiant de corrélation dans « Détails » pour le soutien. |
| Permission refusée | Expliquer l’utilité, proposer « Ouvrir les réglages »; ne pas redemander en boucle (SEC-24). |
| Session expirée | Ré-authentification en feuille, retour à l’écran en cours sans perte de saisie. |
| Version obsolète | Écran de mise à jour bloquant (SEC-21). |

## 5.2 Cas limites métier

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

# 6. Accessibilité

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

# 7. Localisation

- **Langue par défaut : français (Canada)**; anglais (Canada) au lancement; arabe (RTL) à évaluer selon les corridors (Algérie, Maroc). Toutes les chaînes dans des fichiers de traduction (i18next + `expo-localization`); aucune chaîne en dur.
- **Formats fr-CA** : `32,06 $`, `21 h 40`, `ven. 14 nov.`, séparateur de milliers espace insécable (`1 000 $`). Utiliser `Intl.NumberFormat('fr-CA', { style: 'currency', currency: 'CAD' })` et `Intl.DateTimeFormat`.
- **Termes** : courriel, texto, égoportrait, clé d’accès, séquestre (guide de ton, charte p. 16). Vouvoiement.
- **Pluriels et genres** gérés par ICU MessageFormat (« 1 voyageur », « 8 voyageurs »).
- **RTL** : utiliser `start`/`end`, icônes directionnelles miroir, codes et montants restent LTR.
- **Fuseaux** : stocker en UTC, afficher dans le fuseau pertinent avec la ville.
- **Expansion** : prévoir +30 % de longueur (anglais → français); boutons sur deux lignes interdits, préférer un libellé plus court.
- Les reçus et contrats sont en français (volet légal 2).

# 8. Événements analytiques suggérés

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

# 9. Monétisation : exigences UX

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
