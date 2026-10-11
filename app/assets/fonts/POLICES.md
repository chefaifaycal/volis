# Polices Volis

Les quatre familles sont distribuées sous **SIL Open Font License 1.1 (OFL)** : utilisation, intégration dans une appli et redistribution autorisées (y compris commerciale), à condition de garder la licence avec les fichiers et de ne pas vendre les polices seules. Les licences sont dans ce dossier (`OFL-*.txt`).

| Rôle | Famille | Graisses fournies | Google Fonts | Paquet Expo | Licence |
|---|---|---|---|---|---|
| Titres, montants, logo | Plus Jakarta Sans | 700, 800 | https://fonts.google.com/specimen/Plus+Jakarta+Sans | `@expo-google-fonts/plus-jakarta-sans` | OFL 1.1 |
| Texte, interface | Inter (opsz 14) | 400, 500, 600, 700 | https://fonts.google.com/specimen/Inter | `@expo-google-fonts/inter` | OFL 1.1 |
| Codes, aéroports, vols, références | JetBrains Mono | 600, 700 | https://fonts.google.com/specimen/JetBrains+Mono | `@expo-google-fonts/jetbrains-mono` | OFL 1.1 |
| Annotations décoratives seulement | Caveat | 600 | https://fonts.google.com/specimen/Caveat | `@expo-google-fonts/caveat` | OFL 1.1 |

Les fichiers `.ttf` statiques ici ont été extraits des polices variables officielles (Google Fonts) avec fontTools, sans modification des contours. Nom de fichier = clé à utiliser dans `fontFamily`.

## Option A : paquets @expo-google-fonts (recommandé)

```bash
npx expo install expo-font expo-splash-screen @expo-google-fonts/plus-jakarta-sans @expo-google-fonts/inter @expo-google-fonts/jetbrains-mono @expo-google-fonts/caveat
```

```tsx
// app/_layout.tsx (expo-router)
import { useEffect } from 'react';
import { Stack } from 'expo-router';
import * as SplashScreen from 'expo-splash-screen';
import { useFonts } from 'expo-font';
import { PlusJakartaSans_700Bold, PlusJakartaSans_800ExtraBold } from '@expo-google-fonts/plus-jakarta-sans';
import { Inter_400Regular, Inter_500Medium, Inter_600SemiBold, Inter_700Bold } from '@expo-google-fonts/inter';
import { JetBrainsMono_600SemiBold, JetBrainsMono_700Bold } from '@expo-google-fonts/jetbrains-mono';
import { Caveat_600SemiBold } from '@expo-google-fonts/caveat';

SplashScreen.preventAutoHideAsync();

export default function RootLayout() {
  const [loaded, error] = useFonts({
    PlusJakartaSans_700Bold, PlusJakartaSans_800ExtraBold,
    Inter_400Regular, Inter_500Medium, Inter_600SemiBold, Inter_700Bold,
    JetBrainsMono_600SemiBold, JetBrainsMono_700Bold, Caveat_600SemiBold,
  });
  useEffect(() => { if (loaded || error) SplashScreen.hideAsync(); }, [loaded, error]);
  if (!loaded && !error) return null;
  return <Stack screenOptions={{ headerShown: false }} />;
}
```

Les noms (`Inter_600SemiBold`, etc.) correspondent à ceux de `tokens/theme.ts`.

## Option B : fichiers locaux (config plugin, chargés au build)

Copiez ce dossier vers `assets/fonts/`, puis dans `app.json` (déjà dans `expo/app.json.snippet.json`) :

```json
["expo-font", { "fonts": ["./assets/fonts/Inter-Regular.ttf", "./assets/fonts/PlusJakartaSans-ExtraBold.ttf", "..."] }]
```

Avec l’option B, le nom de famille vient du fichier. Sur iOS, utilisez le nom PostScript ; sur Android, le nom du fichier sans extension. Si vous choisissez cette option, ajustez `fonts` dans `theme.ts` en conséquence. L’option A évite ce piège.

## Web

```html
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@600;700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
```
