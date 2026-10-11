# Volis : ressources de design pour les développeurs

Concept retenu : **1 « Carnet de voyage »**. Cible : **Expo / React Native** (iOS, Android) et **web**.
Tout est généré à partir d’une source unique (`tokens/tokens.json`). Si une valeur change, modifiez d’abord le token, puis les fichiers dérivés.

## Arborescence

```
dev-assets/
├── README_DEV.md                 ← ce fichier
├── tokens/
│   ├── tokens.json               ← design tokens au format W3C (DTCG) : palette, couleurs clair/sombre, typo, espacements, rayons, ombres, mouvement, mise en page
│   ├── theme.ts                  ← thème React Native typé : lightColors, darkColors, typography, space, radii, shadows, motion, layout, useTheme()
│   ├── tailwind.config.js        ← Tailwind (web) / NativeWind v4 : couleurs liées aux variables CSS, échelle typo, rayons, ombres
│   └── tokens.css                ← variables CSS (--vl-*) avec mode sombre (prefers-color-scheme et [data-theme="dark"]) et prefers-reduced-motion
├── icons/
│   ├── svg/                      ← 58 icônes SVG 24 px, trait 2 px, stroke="currentColor"
│   └── react-native/Icon.tsx     ← composant <Icon name="package" size={22} color=… /> (react-native-svg)
├── illustrations/                ← personnages dessinés à la main, PNG transparents @1x/@2x/@3x + WebP
├── logos/
│   ├── logo-principal/           ← « Colis caché » : SVG, PNG 4000 px transparents, PDF, aperçus (crème, encre, sarcelle, mono noir/blanc)
│   └── symbole/                  ← o-colis + pastille : SVG, PNG 2000 px, PDF
├── app-icons/                    ← icône « Signature » : iOS 1024 (clair, sombre, teinté), Android adaptatif (res/mipmap-*, calques SVG 108 dp, Play Store 512), favicon (ico, svg, png, apple-touch-icon)
├── expo/                         ← fichiers prêts pour app.json : icon.png, icon-ios-dark/tinted, adaptive-icon-foreground/background/monochrome (1024), splash-icon(.dark).png, favicon.png, app.json.snippet.json
├── fonts/                        ← TTF statiques (OFL) + POLICES.md (liens Google Fonts, licence, extrait expo-font)
└── screens/                      ← 50 maquettes PNG 786×1704 (393×852 pt @2x) numérotées, inventaire-ecrans.csv, volis-ecrans-concept1.pdf
```

## Démarrage rapide (Expo)

1. Copiez `expo/*` dans `assets/expo/`, `fonts/*.ttf` dans `assets/fonts/`, `illustrations/` dans `assets/illustrations/`.
2. Fusionnez `expo/app.json.snippet.json` dans votre `app.json` (icônes iOS clair/sombre/teinté, icône adaptative Android avec monochrome, splash clair/sombre via `expo-splash-screen`, polices via `expo-font`).
3. Chargez les polices : voir `fonts/POLICES.md` (option A recommandée : `@expo-google-fonts/*`).
4. Copiez `tokens/theme.ts` dans `src/theme/` et utilisez `useTheme()` :

```tsx
import { useTheme } from '@/theme/theme';
import { Icon } from '@/ui/Icon';

export function TrustBanner() {
  const t = useTheme();
  return (
    <View style={{ flexDirection: 'row', gap: t.space['1'], padding: t.space['1.5'], borderRadius: t.radii.md, backgroundColor: t.colors.mint }}>
      <Icon name="shield" size={20} color={t.colors.primaryPressed} />
      <Text style={[t.typography.caption, { color: t.colors.text, flex: 1 }]}>Votre argent est protégé : il reste en séquestre jusqu’à la remise.</Text>
    </View>
  );
}
```

5. Illustrations : `require('@/assets/illustrations/voyageur-valise-colis.png')`. React Native choisit seul @2x/@3x. Marquez-les décoratives (`accessible={false}`). Les WebP servent au web (`<img srcset>`).

## Web

- Importez `tokens/tokens.css`. Utilisez `var(--vl-primary)`, `font: var(--vl-text-body)`.
- Tailwind : `tokens/tailwind.config.js` → classes `bg-primary`, `text-text-secondary`, `rounded-lg`, `shadow-e2`, `text-h1`, `font-display`.
- Favicon : `app-icons/favicon/` (`favicon.ico` 16/32/48, `favicon.svg`, `apple-touch-icon.png`).

## Règles à respecter (extrait de la charte)

- **Couleurs** : utilisez toujours les tokens sémantiques (`primary`, `text`, `successBg`…), jamais la palette brute dans un composant. Le corail (`accent`) est décoratif : **jamais de texte blanc dessus**.
- **Typographie** : Plus Jakarta Sans pour les titres et montants, Inter pour l’interface, JetBrains Mono pour les codes et vols, **Caveat seulement pour des annotations décoratives**. Activez `allowFontScaling` et ne fixez pas de hauteur sur du texte.
- **Espacements** : grille de 8 pt (`space`), marges d’écran de 16 pt, cibles tactiles ≥ 44 pt (`layout.minTouch`).
- **Mode sombre** : `darkColors` est fourni et vérifié AA (charte, page 6). Les maquettes sont en mode clair.
- **Mouvement** : `motion.fast/base/slow`; respectez `AccessibilityInfo.isReduceMotionEnabled()`.
- **Stripe** : Identity, Connect (onboarding des versements) et PaymentSheet sont hébergés. Aucun champ bancaire ni biométrique dans l’appli (volet technique SEC-10, SEC-11).

## Écrans

`screens/inventaire-ecrans.csv` (UTF-8 avec BOM, s’ouvre dans Excel) : `id, fichier, nom, parcours, objectif, composants_cles, barre_onglets`. Les parcours A à G correspondent aux planches de `volis-design/boards/` et aux histoires utilisateur de `specs-fonctionnelles-ux.md`.

## Licences

- Polices : SIL Open Font License 1.1 (voir `fonts/OFL-*.txt`).
- Logos, icônes, illustrations : propriété de Volis (projet de Faycal Chefai). Icônes dessinées dans le style Lucide (ISC), redessinées à la main.
- Noms, numéros et montants des maquettes : fictifs et illustratifs.
