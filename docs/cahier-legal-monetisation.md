---
title: "Volis — Cahier des charges, section : Volet légal de la monétisation"
subtitle: "Préparé par Legal Team — 11 octobre 2026"
---

> **Avertissement.** Ce texte est une synthèse informative. Il ne constitue ni un avis juridique, ni un avis fiscal, ni un avis financier. Tout doit être validé par un avocat membre du Barreau du Québec, et par un comptable pour la fiscalité, avant le lancement.

# 1. Sources de revenus prévues

| Source | Qui paie | Comment Stripe l'encaisse (voir section technique) |
|---|---|---|
| Commission sur chaque livraison | L'expéditeur, ou une part du montant versé au voyageur | Frais de plateforme prélevés par Stripe Connect |
| Assurance optionnelle du colis | L'expéditeur, s'il choisit l'option | Prime versée à l'assureur partenaire. Volis touche au plus une rémunération que l'assureur lui verse et qui doit être divulguée |
| Frais de versement instantané | Le voyageur, s'il choisit le versement instantané | Frais de Stripe, avec une éventuelle marge pour Volis |
| Option future : abonnement ou mise en avant | Selon l'offre | À encadrer avant de lancer (voir 6) |

# 2. Prix et transparence (Loi sur la protection du consommateur et Loi sur la concurrence)

- **Prix total annoncé.** Le prix montré doit inclure tous les frais obligatoires : commission, frais de service et frais de traitement. Seules la TPS et la TVQ peuvent s'ajouter (LPC, art. 224 c). La Loi sur la concurrence interdit aussi d'annoncer un prix partiel en ajoutant des frais obligatoires plus tard.
- **Détail avant paiement.** Avant de payer, l'utilisateur doit voir le prix du transport, la commission de Volis, l'assurance si elle est choisie, les taxes et le total. Ce détail correspond à l'écran de confirmation prévu par Ui Designer.
- **Contrat conclu à distance** (LPC, art. 54.1 et suivants). Avant la conclusion, l'utilisateur doit recevoir certaines informations : l'identité et l'adresse de Volis, une description du service, le prix détaillé, les modalités de paiement et la politique d'annulation et de remboursement. Il faut ensuite lui transmettre une copie du contrat dans les 15 jours. Si ces informations manquent, le consommateur peut annuler le contrat et demander une rétrofacturation à l'émetteur de sa carte.
- **Pas de publicité trompeuse** (LPC, art. 219 et suivants). Les messages comme « livraison garantie » ou « assuré » sont interdits si l'assurance n'est pas choisie.
- **Langue.** Les prix, les reçus, les factures et les conditions doivent être en français (Charte de la langue française).

# 3. Commission de la plateforme

- **Rôle d'intermédiaire.** Les conditions d'utilisation doivent dire clairement que la commission paie un service de mise en relation et de paiement, pas un service de transport.
- **Statut des voyageurs.** Les voyageurs sont des utilisateurs autonomes. Volis ne doit pas leur imposer d'horaires, de quotas ni de prix fixes, sinon un tribunal pourrait les considérer comme des salariés (Loi sur les normes du travail, cotisations sociales). Les règles de sécurité et la liste d'objets interdits restent permises.
- **Taxes sur la commission.** La commission et les frais de service sont des fournitures taxables. Volis doit s'inscrire à la TPS/TVQ dès que ses revenus dépassent 30 000 $ sur quatre trimestres civils consécutifs, ou plus tôt de façon volontaire. Les reçus doivent indiquer les numéros de TPS et de TVQ. **À confirmer avec un comptable :** les règles qui obligent les exploitants de plateformes numériques à percevoir les taxes à la place de certains fournisseurs pourraient s'appliquer à Volis.
- **Revenus des voyageurs.** Ils sont imposables pour les voyageurs. Le régime de déclaration de l'ARC pour les plateformes (en vigueur depuis 2024) pourrait obliger Volis à déclarer chaque année ce que touchent les voyageurs. **À confirmer avec un comptable.** Il faut donc prévoir dès maintenant de recueillir les renseignements requis (nom, adresse, NAS ou numéro d'entreprise), avec le consentement prévu par la Loi 25.

# 4. Assurance optionnelle

- **Ce que Volis ne doit pas faire.** Vendre de l'assurance en son propre nom ou conseiller les utilisateurs sur une assurance, à moins d'être inscrit auprès de l'AMF.
- **Option A, la plus simple : la recommandation.** Volis renvoie l'utilisateur vers l'assureur partenaire, qui vend lui-même l'assurance. Si l'assureur verse une rémunération de recommandation à Volis, il faut l'encadrer par contrat et la divulguer à l'utilisateur.
- **Option B : la distribution sans représentant** (Loi sur la distribution de produits et services financiers, titre VIII). Ce régime permet de proposer une assurance liée au service. L'assureur doit l'avoir déclaré à l'AMF, Volis doit remettre le guide de distribution de l'assureur et l'utilisateur garde un droit de résolution prévu par la loi. **À valider avec l'avocat et l'assureur.**
- **Interface.** Il faut une case d'acceptation qui n'est pas cochée d'avance, un prix montré à part, et les limites, exclusions et plafonds écrits clairement. L'assurance ne doit jamais être obligatoire pour utiliser le service.
- **Lien avec la politique de litiges.** Le plafond d'indemnisation de Volis s'applique quand l'assurance n'est pas choisie. Il ne peut jamais servir à exclure la responsabilité de Volis pour une faute lourde ou intentionnelle, ni pour un préjudice corporel ou moral (C.c.Q., art. 1474).

# 5. Frais de versement instantané

- Le montant ou le pourcentage doit être montré avant que le voyageur choisisse. Le virement standard gratuit reste toujours offert.
- Si Volis ajoute une marge aux frais de Stripe, elle doit être divulguée. Le terme « frais de Stripe » ne peut pas désigner un montant qui contient une marge pour Volis.
- Les données bancaires sont saisies seulement dans l'inscription hébergée par Stripe, et jamais sur les serveurs de Volis (Loi 25, minimisation des données).

# 6. Paiement retenu, remboursements et litiges

- **Encaissement des fonds.** Avec les « separate charges and transfers » de Stripe Connect, l'argent transite par le solde Stripe de Volis. Il faut faire confirmer par l'avocat que Volis peut compter sur l'inscription de Stripe comme fournisseur de services de paiement, ou qu'une exemption s'applique. Sinon, Volis devrait peut-être s'inscrire elle-même à la Banque du Canada (Loi sur les activités associées aux paiements de détail).
- **Politique de remboursement.** Elle doit préciser quand un remboursement s'applique (annulation, colis non remis), son délai, et quels frais sont remboursés ou non. Une clause qui empêcherait le consommateur d'exercer ses recours prévus par la LPC est sans effet.
- **Rétrofacturations.** Il faut prévoir comment Volis répond aux contestations de carte, en joignant les preuves de remise (photos et confirmation). Il faut aussi prévoir qui assume la perte, sans la transférer au voyageur sans son accord prévu dans les conditions.
- **Abonnement ou mise en avant payante (plus tard).** Ce sont des contrats à exécution successive selon la LPC. Il faudra des règles sur la résiliation, un avis avant chaque renouvellement automatique et un prix clair.

# 7. Marketing et données

- **Courriels et notifications promotionnels.** Ils demandent un consentement exprès, un lien de désabonnement et l'identification de l'expéditeur (LCAP, la loi anti-pourriel).
- **Publicité ciblée ou traçage.** La Loi 25 exige que ce soit désactivé par défaut avec un consentement distinct. Il faut aussi les fiches vie privée des stores.
- **Pas de vente de données personnelles** sans consentement exprès.
- **Sous-traitants qui reçoivent des données** : Stripe (paiements et vérification d'identité), Sentry (suivi des erreurs), le service de notifications d'Expo, l'outil d'analytics s'il y en a un, et l'assureur partenaire. Chacun doit figurer dans l'évaluation des facteurs relatifs à la vie privée (ÉFVP) et dans la politique de confidentialité, avec un contrat de traitement des données. Ceux qui traitent les données hors du Québec doivent faire l'objet d'une évaluation du transfert (Loi 25, art. 17). Supabase est hébergé au Canada (Central).

# 8. Clauses à prévoir dans les conditions d'utilisation

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

# 9. À faire valider par l'avocat et le comptable

- [ ] Le mode de distribution de l'assurance (option A ou B) et la rémunération reçue de l'assureur.
- [ ] La perception de la TPS/TVQ par Volis comme plateforme, et la déclaration à l'ARC des revenus des voyageurs.
- [ ] Le statut de Volis selon la loi sur les paiements de détail, avec le modèle Stripe Connect.
- [ ] Le statut de travailleur autonome des voyageurs.
- [ ] L'ÉFVP et l'évaluation des transferts pour chaque sous-traitant (Stripe, Sentry, Expo, analytics, assureur).
- [ ] La version finale des conditions d'utilisation, de la politique de remboursement et de litiges, et de la politique de confidentialité.
