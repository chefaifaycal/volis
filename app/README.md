# Volis — application (Expo / React Native, TypeScript strict)

Cible : iOS, Android et web, avec Expo Router (routes dans `src/app/`).

## Démarrer

```bash
cd app
npm install
cp .env.example .env      # puis renseigner les valeurs PUBLIQUES (voir le fichier)
npx expo start            # i = iOS, a = Android, w = web
npx tsc --noEmit          # vérification de types
npx expo lint             # lint
```

Node.js ≥ 20.19.4 (ou 22.13+) recommandé pour React Native 0.86.

## Architecture (cahier technique, partie B §2.2–2.3)

```text
src/
  app/                 # routes Expo Router uniquement (fines : elles délèguent aux écrans)
    _layout.tsx        # fournisseurs globaux : polices, thème, safe area
    (tabs)/            # Accueil, Envois, Voyages, Messages, Profil
  ui/
    screens/           # écrans (affichage seulement)
    viewmodels/        # hooks ViewModel : état d'écran immuable, flux unidirectionnel
    components/        # design system (Icon, Card, Screen…)
  domain/              # TypeScript pur, sans React Native : modèles, Money, machine d'états
  data/
    repositories/      # contrats des repositories (seul accès au réseau / stockage)
    fakes/             # implémentations en mémoire (données fictives) en attendant Supabase
    config/env.ts      # lecture des variables EXPO_PUBLIC_*
  theme/
    theme.ts           # généré depuis design/dev-assets/tokens/tokens.json — ne pas éditer
    fonts.ts           # polices locales (assets/fonts, licence OFL)
```

Règle : l'UI n'appelle jamais le réseau ni le stockage directement ; elle passe par un ViewModel qui utilise un repository.

## Design

- Thème : `useTheme()` de `@/theme` (couleurs clair/sombre, typographie, espacements, rayons, ombres).
- Icônes : `<Icon name="package" />` (`src/ui/components/Icon.tsx`, react-native-svg).
- Polices : Plus Jakarta Sans, Inter, JetBrains Mono, Caveat (SIL OFL 1.1, licences dans `assets/fonts/`).
- Icônes d'app et splash : `assets/expo/` (issus de `design/dev-assets/expo/`).

## Secrets

Seules les variables `EXPO_PUBLIC_*` de `.env.example` sont lues, et elles sont publiques (embarquées dans l'app). Aucun secret ici.
