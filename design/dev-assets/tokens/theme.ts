// Volis — thème React Native / Expo (généré depuis tokens.json). Ne pas éditer à la main.
import { useColorScheme } from 'react-native';

export const palette = {
  creme: "#F5F1E8",
  papier: "#FFFDF8",
  encre: "#1E2A3A",
  ardoise: "#4E5A69",
  sarcelle: "#0F766E",
  sarcelleFoncee: "#0B5B55",
  sarcelleClaire: "#D6ECE8",
  menthe: "#DCEFEA",
  corail: "#FF7A59",
  peche: "#FFE1D6",
  sable: "#FFE9C7",
  lin: "#E4DACA",
  taupe: "#7E7A70",
} as const;

export const lightColors = {
  bg: "#F5F1E8",
  surface: "#FFFDF8",
  surfaceSunken: "#EFE8DA",
  surfaceInverse: "#1E2A3A",
  text: "#1E2A3A",
  textSecondary: "#4E5A69",
  textMuted: "#6F6A60",
  textInverse: "#FFFFFF",
  textOnAccent: "#1E2A3A",
  primary: "#0F766E",
  primaryPressed: "#0B5B55",
  primarySubtle: "#D6ECE8",
  onPrimary: "#FFFFFF",
  secondary: "#1E2A3A",
  onSecondary: "#FFFFFF",
  accent: "#FF7A59",
  accentSubtle: "#FFE1D6",
  mint: "#DCEFEA",
  sand: "#FFE9C7",
  border: "#7E7A70",
  borderSubtle: "#E4DACA",
  divider: "#DCD3C2",
  disabledBg: "#E2DACB",
  disabledText: "#6F6A60",
  success: "#15803D",
  successText: "#14532D",
  successBg: "#D8F0DF",
  warning: "#B45309",
  warningText: "#6B3A06",
  warningBg: "#FFF0E0",
  warningBorder: "#E0A458",
  error: "#B42318",
  errorText: "#8F1D14",
  errorBg: "#FDE7E4",
  info: "#1F4E8C",
  infoText: "#1F4E8C",
  infoBg: "#E3ECF8",
  focusRing: "#0F766E",
  scrim: "rgba(20,28,40,0.45)",
} as const;

export const darkColors: Record<keyof typeof lightColors, string> = {
  bg: "#121A24",
  surface: "#1B2533",
  surfaceSunken: "#0D141C",
  surfaceInverse: "#F5F1E8",
  text: "#F3EEE4",
  textSecondary: "#B6BFCB",
  textMuted: "#8E98A6",
  textInverse: "#1E2A3A",
  textOnAccent: "#1E2A3A",
  primary: "#3FB8AC",
  primaryPressed: "#5FCFC3",
  primarySubtle: "#16403D",
  onPrimary: "#0B1F1D",
  secondary: "#F3EEE4",
  onSecondary: "#1E2A3A",
  accent: "#FF8D6F",
  accentSubtle: "#4A2A22",
  mint: "#173A36",
  sand: "#3D3222",
  border: "#6B7788",
  borderSubtle: "#2E3A4B",
  divider: "#2A3545",
  disabledBg: "#2A3442",
  disabledText: "#8E98A6",
  success: "#4ADE80",
  successText: "#86EFAC",
  successBg: "#143323",
  warning: "#FBBF6A",
  warningText: "#FCD38D",
  warningBg: "#3A2A12",
  warningBorder: "#8A5A16",
  error: "#FF8A80",
  errorText: "#FFB4AB",
  errorBg: "#3D1A17",
  info: "#8AB4F8",
  infoText: "#AECBFA",
  infoBg: "#16263D",
  focusRing: "#3FB8AC",
  scrim: "rgba(0,0,0,0.6)",
};

export const fonts = {
  display: 'PlusJakartaSans_800ExtraBold', displayBold: 'PlusJakartaSans_700Bold',
  body: 'Inter_400Regular', bodyMedium: 'Inter_500Medium', bodySemiBold: 'Inter_600SemiBold', bodyBold: 'Inter_700Bold',
  mono: 'JetBrainsMono_700Bold', monoSemiBold: 'JetBrainsMono_600SemiBold',
  hand: 'Caveat_600SemiBold', // décoratif uniquement — jamais pour une étiquette, un bouton ou un champ
} as const;

export const typography = {
  display: { fontFamily: 'PlusJakartaSans_800ExtraBold', fontSize: 34, lineHeight: 40, letterSpacing: -0.8 }, // Écran de bienvenue, gros montants
  h1: { fontFamily: 'PlusJakartaSans_800ExtraBold', fontSize: 26, lineHeight: 32, letterSpacing: -0.5 }, // Titre d’écran
  h2: { fontFamily: 'PlusJakartaSans_800ExtraBold', fontSize: 22, lineHeight: 28, letterSpacing: -0.3 }, // Titre de section importante
  h3: { fontFamily: 'PlusJakartaSans_800ExtraBold', fontSize: 19, lineHeight: 24, letterSpacing: 0 }, // En-tête de navigation
  title: { fontFamily: 'PlusJakartaSans_800ExtraBold', fontSize: 17, lineHeight: 22, letterSpacing: 0 }, // Titre de carte
  bodyLg: { fontFamily: 'Inter_500Medium', fontSize: 16, lineHeight: 22, letterSpacing: 0 }, // Champs de saisie, texte principal
  body: { fontFamily: 'Inter_400Regular', fontSize: 15, lineHeight: 21, letterSpacing: 0 }, // Texte courant
  bodySm: { fontFamily: 'Inter_400Regular', fontSize: 14, lineHeight: 20, letterSpacing: 0 }, // Texte secondaire
  label: { fontFamily: 'Inter_600SemiBold', fontSize: 14, lineHeight: 18, letterSpacing: 0 }, // Étiquettes de champs
  caption: { fontFamily: 'Inter_500Medium', fontSize: 13, lineHeight: 18, letterSpacing: 0 }, // Aide, métadonnées
  micro: { fontFamily: 'Inter_600SemiBold', fontSize: 12, lineHeight: 16, letterSpacing: 0 }, // Badges, horodatage (minimum absolu)
  tab: { fontFamily: 'Inter_600SemiBold', fontSize: 11, lineHeight: 14, letterSpacing: 0 }, // Libellés barre d’onglets (exception iOS)
  button: { fontFamily: 'Inter_700Bold', fontSize: 17, lineHeight: 22, letterSpacing: 0 }, // Bouton principal
  buttonSm: { fontFamily: 'Inter_700Bold', fontSize: 15, lineHeight: 20, letterSpacing: 0 }, // Bouton secondaire / compact
  code: { fontFamily: 'JetBrainsMono_700Bold', fontSize: 32, lineHeight: 32, letterSpacing: 0 }, // Code de remise 4821
  monoMd: { fontFamily: 'JetBrainsMono_700Bold', fontSize: 15, lineHeight: 20, letterSpacing: 0 }, // Codes aéroport, n° de vol
  monoSm: { fontFamily: 'JetBrainsMono_600SemiBold', fontSize: 12, lineHeight: 16, letterSpacing: 0 }, // Références (VL-4821)
  hand: { fontFamily: 'Caveat_600SemiBold', fontSize: 21, lineHeight: 22, letterSpacing: 0 }, // Annotations décoratives uniquement
} as const;

export const space = { '0': 0, '0.5': 4, '1': 8, '1.5': 12, '2': 16, '2.5': 20, '3': 24, '4': 32, '5': 40, '6': 48, '8': 64 } as const; // grille de 8 pt (demi-pas 4)
export const radii = {
  xs: 6,
  sm: 10,
  md: 14,
  lg: 20,
  xl: 28,
  pill: 999,
} as const;
export const shadows = {
  e0: { shadowColor: '#141C28', shadowOffset: { width: 0, height: 0 }, shadowOpacity: 0, shadowRadius: 0.0, elevation: 0 }, // Cartes à plat (bordure 1,5 px lin)
  e1: { shadowColor: '#141C28', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.12, shadowRadius: 3.0, elevation: 2 }, // Segment actif, puces
  e2: { shadowColor: '#141C28', shadowOffset: { width: 0, height: 8 }, shadowOpacity: 0.3, shadowRadius: 10.0, elevation: 6 }, // Cartes flottantes sur carte, épingles
  e3: { shadowColor: '#141C28', shadowOffset: { width: 0, height: -10 }, shadowOpacity: 0.25, shadowRadius: 15.0, elevation: 12 }, // Bottom sheet
  e4: { shadowColor: '#141C28', shadowOffset: { width: 0, height: 20 }, shadowOpacity: 0.35, shadowRadius: 25.0, elevation: 16 }, // Modales, toasts
} as const;
export const motion = {"instant": 100, "fast": 150, "base": 250, "slow": 400, "easing": "cubic-bezier(0.2, 0, 0, 1)", "easingExit": "cubic-bezier(0.3, 0, 1, 1)", "spring": {"damping": 18, "stiffness": 220}} as const;
export const layout = {
  screenMargin: 16,
  gutter: 12,
  columns: 4,
  minTouch: 44,
  tabBarHeight: 60,
  headerHeight: 48,
  ctaHeight: 56,
  inputHeight: 50,
} as const;

export type ThemeColors = typeof lightColors;
export const makeTheme = (scheme: 'light' | 'dark') => ({
  scheme, colors: scheme === 'dark' ? darkColors : lightColors, fonts, typography, space, radii, shadows, motion, layout,
});
export type Theme = ReturnType<typeof makeTheme>;
export function useTheme(): Theme {
  const scheme = useColorScheme() === 'dark' ? 'dark' : 'light';
  return makeTheme(scheme);
}
