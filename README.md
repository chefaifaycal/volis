# Volis

**Volis** met en relation des **expéditeurs de colis** et des **voyageurs** qui ont de la place dans leurs bagages. L'expéditeur trouve un voyageur vérifié sur son trajet ; le voyageur rentabilise ses kilos libres. Paiement protégé (séquestre via Stripe), vérification d'identité (Stripe Identity), messagerie et suivi de la remise.

Plateformes visées : **iOS, Android et web** (Expo / React Native), backend **Supabase** (région `ca-central-1`).

> ⚠️ **Avertissement** : les documents légaux et réglementaires de ce dépôt (cahier légal et monétisation, mentions relatives à la conformité, à la douane, à l'assurance, etc.) sont fournis à titre informatif et **ne constituent pas un avis juridique**. Faites-les valider par un professionnel qualifié avant toute mise en production.

## Arborescence

```text
.
├── README.md
├── docs/                         # Cahier des charges et documentation projet
│   ├── cahier-des-charges-volis.{pdf,docx}
│   ├── cdc-technique-securite.{md,docx}       # volet technique et sécurité (architecture, RLS, Stripe…)
│   ├── cahier-legal-monetisation.{md,docx}    # volet légal et monétisation
│   ├── projet-volis-fiche-recherche.pdf
│   ├── guide-securite-architecture-mobile.{pdf,docx}
│   ├── guide/                    # guide interactif HTML, ses sources (build/) et captures
│   ├── assemblage/               # sources d'assemblage du cahier des charges (md, html, diagrammes)
│   └── cdc/                      # première version et diagrammes Mermaid
├── design/                       # Identité visuelle et maquettes
│   ├── volis-charte-graphique.pdf, charte/    # charte graphique (PDF + pages PNG)
│   ├── volis-ecrans-concept1.pdf, ecrans/     # 50 maquettes d'écrans
│   ├── boards/                   # planches des parcours A à G
│   ├── specs-fonctionnelles-ux.md
│   ├── dev-assets/               # ressources développeurs : tokens, icônes, illustrations, logos, polices (OFL), icônes d'app
│   └── build/                    # scripts de génération des ressources
├── app/                          # Application Expo (React Native, TypeScript strict, Expo Router)
└── supabase/                     # Backend (vide pour l'instant : région ca-central-1, RLS obligatoire)
```

Liens rapides :

- Documentation : [`docs/`](docs/) — commencer par [`docs/cdc-technique-securite.md`](docs/cdc-technique-securite.md) et [`docs/cahier-legal-monetisation.md`](docs/cahier-legal-monetisation.md)
- Design : [`design/`](design/) — ressources développeurs : [`design/dev-assets/README_DEV.md`](design/dev-assets/README_DEV.md), specs UX : [`design/specs-fonctionnelles-ux.md`](design/specs-fonctionnelles-ux.md)
- Application : [`app/README.md`](app/README.md)
- Backend : [`supabase/README.md`](supabase/README.md)

## Démarrer l'application

Prérequis : Node.js ≥ 20.19.4 (ou 22 LTS), npm ; Expo Go ou un simulateur iOS/Android pour tester sur mobile.

```bash
cd app
npm install
cp .env.example .env     # renseigner les valeurs publiques (laisser vide = mode démo avec données fictives)
npx expo start           # puis i (iOS), a (Android) ou w (web)
```

Vérifications :

```bash
npx tsc --noEmit
npx expo lint
```

## Sécurité

- Aucun secret dans ce dépôt. Seules des variables **publiques** `EXPO_PUBLIC_*` sont prévues (`app/.env.example`).
- La clé `service_role` Supabase et les clés secrètes Stripe vivent uniquement dans les secrets du serveur / de la CI.
- Toute table Supabase doit avoir la RLS activée (voir `supabase/README.md`).

## Licence

Projet propriétaire, non open source. Aucune licence d'utilisation n'est accordée.
Les polices incluses restent sous leur propre licence (SIL Open Font License 1.1, fichiers `OFL-*.txt`).

Tous droits réservés © 2026 Faycal Chefai
