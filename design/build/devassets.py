import json, os, shutil, sys, re, glob, csv
sys.path.insert(0, '/workspace/maquettes-v4/build')
from tokens import *
from PIL import Image
D = '/workspace/volis-design/dev-assets'
LOGO = '/workspace/logos/final'
for sub in ['tokens', 'icons/svg', 'icons/react-native', 'illustrations', 'logos', 'app-icons', 'expo', 'fonts', 'screens']:
    os.makedirs(f'{D}/{sub}', exist_ok=True)
# ---------------- TOKENS (W3C DTCG) ----------------
def col(v, d=''): return {'$type': 'color', '$value': v, **({'$description': d} if d else {})}
def dim(v): return {'$type': 'dimension', '$value': f'{v}px'}
tok = {'$description': 'Volis design tokens — concept 1 « Carnet de voyage » — format W3C Design Tokens (DTCG)',
       'palette': {k: col(v) for k, v in PALETTE.items()},
       'color': {'light': {k: col(v) for k, v in LIGHT.items()}, 'dark': {k: col(v) for k, v in DARK.items()}},
       'font': {'family': {k: {'$type': 'fontFamily', '$value': [v, 'system-ui', 'sans-serif'] if k != 'mono' else [v, 'ui-monospace', 'monospace']} for k, v in FONTS.items()}},
       'typography': {n: {'$type': 'typography', '$value': {'fontFamily': '{font.family.%s}' % f, 'fontSize': f'{s}px', 'lineHeight': f'{lh}px', 'fontWeight': w, 'letterSpacing': f'{ls}px'}, '$description': u} for n, f, s, lh, w, ls, u in TYPE},
       'space': {k: dim(v) for k, v in SPACE.items()},
       'radius': {k: dim(v) for k, v in RADII.items()},
       'shadow': {k: {'$type': 'shadow', '$value': {'color': SHADOW_COLOR + format(int(v['opacity']*255), '02X'), 'offsetX': '0px', 'offsetY': f'{v["y"]}px', 'blur': f'{v["blur"]}px', 'spread': f'{v["spread"]}px'}, '$description': v['use']} for k, v in SHADOWS.items()},
       'duration': {k: {'$type': 'duration', '$value': f'{MOTION[k]}ms'} for k in ('instant', 'fast', 'base', 'slow')},
       'easing': {'standard': {'$type': 'cubicBezier', '$value': [0.2, 0, 0, 1]}, 'exit': {'$type': 'cubicBezier', '$value': [0.3, 0, 1, 1]}},
       'layout': {k: dim(v) if k != 'columns' else {'$type': 'number', '$value': v} for k, v in LAYOUT.items()}}
json.dump(tok, open(f'{D}/tokens/tokens.json', 'w'), ensure_ascii=False, indent=2)
# ---------------- theme.ts ----------------
fam = {'display': {800: 'PlusJakartaSans_800ExtraBold', 700: 'PlusJakartaSans_700Bold'}, 'body': {400: 'Inter_400Regular', 500: 'Inter_500Medium', 600: 'Inter_600SemiBold', 700: 'Inter_700Bold'},
       'mono': {600: 'JetBrainsMono_600SemiBold', 700: 'JetBrainsMono_700Bold'}, 'hand': {600: 'Caveat_600SemiBold'}}
def ts_obj(d, ind=4): return '{\n' + ''.join(f'{" "*ind}{k}: {json.dumps(v)},\n' for k, v in d.items()) + ' '*(ind-2) + '}'
typo = ''.join(f"  {n}: {{ fontFamily: '{fam[f][w]}', fontSize: {s}, lineHeight: {lh}, letterSpacing: {ls} }}, // {u}\n" for n, f, s, lh, w, ls, u in TYPE)
shad = ''.join(f"  {k}: {{ shadowColor: '{SHADOW_COLOR}', shadowOffset: {{ width: 0, height: {v['y']} }}, shadowOpacity: {v['opacity']}, shadowRadius: {v['blur']/2}, elevation: {[0,2,6,12,16][int(k[1])]} }}, // {v['use']}\n" for k, v in SHADOWS.items())
theme = f"""// Volis — thème React Native / Expo (généré depuis tokens.json). Ne pas éditer à la main.
import {{ useColorScheme }} from 'react-native';

export const palette = {ts_obj(PALETTE, 2)} as const;

export const lightColors = {ts_obj(LIGHT, 2)} as const;

export const darkColors: Record<keyof typeof lightColors, string> = {ts_obj(DARK, 2)};

export const fonts = {{
  display: 'PlusJakartaSans_800ExtraBold', displayBold: 'PlusJakartaSans_700Bold',
  body: 'Inter_400Regular', bodyMedium: 'Inter_500Medium', bodySemiBold: 'Inter_600SemiBold', bodyBold: 'Inter_700Bold',
  mono: 'JetBrainsMono_700Bold', monoSemiBold: 'JetBrainsMono_600SemiBold',
  hand: 'Caveat_600SemiBold', // décoratif uniquement — jamais pour une étiquette, un bouton ou un champ
}} as const;

export const typography = {{
{typo}}} as const;

export const space = {{ {', '.join(f"'{k}': {v}" for k, v in SPACE.items())} }} as const; // grille de 8 pt (demi-pas 4)
export const radii = {ts_obj(RADII, 2)} as const;
export const shadows = {{
{shad}}} as const;
export const motion = {json.dumps(MOTION)} as const;
export const layout = {ts_obj(LAYOUT, 2)} as const;

export type ThemeColors = typeof lightColors;
export const makeTheme = (scheme: 'light' | 'dark') => ({{
  scheme, colors: scheme === 'dark' ? darkColors : lightColors, fonts, typography, space, radii, shadows, motion, layout,
}});
export type Theme = ReturnType<typeof makeTheme>;
export function useTheme(): Theme {{
  const scheme = useColorScheme() === 'dark' ? 'dark' : 'light';
  return makeTheme(scheme);
}}
"""
open(f'{D}/tokens/theme.ts', 'w').write(theme)
# ---------------- CSS variables ----------------
kebab = lambda s: re.sub(r'([A-Z])', lambda m: '-' + m.group(1).lower(), s)
css = '/* Volis — variables CSS (générées depuis tokens.json) */\n:root {\n'
css += ''.join(f'  --vl-palette-{kebab(k)}: {v};\n' for k, v in PALETTE.items())
css += ''.join(f'  --vl-{kebab(k)}: {v};\n' for k, v in LIGHT.items())
css += f"  --vl-font-display: '{FONTS['display']}', system-ui, sans-serif;\n  --vl-font-body: '{FONTS['body']}', system-ui, sans-serif;\n  --vl-font-mono: '{FONTS['mono']}', ui-monospace, monospace;\n  --vl-font-hand: '{FONTS['hand']}', cursive;\n"
css += ''.join(f'  --vl-text-{kebab(n)}: {w} {s}px/{lh}px var(--vl-font-{f});\n' for n, f, s, lh, w, ls, u in TYPE)
css += ''.join(f'  --vl-space-{k.replace(".", "_")}: {v}px;\n' for k, v in SPACE.items())
css += ''.join(f'  --vl-radius-{k}: {v}px;\n' for k, v in RADII.items())
css += ''.join(f'  --vl-shadow-{k}: 0 {v["y"]}px {v["blur"]}px {v["spread"]}px rgba(20,28,40,{v["opacity"]});\n' for k, v in SHADOWS.items())
css += f"  --vl-duration-fast: {MOTION['fast']}ms;\n  --vl-duration-base: {MOTION['base']}ms;\n  --vl-duration-slow: {MOTION['slow']}ms;\n  --vl-easing: {MOTION['easing']};\n}}\n"
css += '@media (prefers-color-scheme: dark) {\n  :root {\n' + ''.join(f'    --vl-{kebab(k)}: {v};\n' for k, v in DARK.items()) + '  }\n}\n'
css += '[data-theme="dark"] {\n' + ''.join(f'  --vl-{kebab(k)}: {v};\n' for k, v in DARK.items()) + '}\n'
css += '@media (prefers-reduced-motion: reduce) { :root { --vl-duration-fast: 0ms; --vl-duration-base: 0ms; --vl-duration-slow: 0ms; } }\n'
open(f'{D}/tokens/tokens.css', 'w').write(css)
# ---------------- tailwind / nativewind ----------------
tw = f"""// Volis — tailwind.config.js (web) et NativeWind v4 (Expo). Couleurs pilotées par variables CSS -> mode sombre automatique.
// Web : importez tokens.css. NativeWind : importez tokens.css dans global.css (NativeWind v4 supporte les variables CSS).
/** @type {{import('tailwindcss').Config}} */
module.exports = {{
  content: ['./app/**/*.{{js,jsx,ts,tsx}}', './src/**/*.{{js,jsx,ts,tsx}}'],
  presets: [/* NativeWind : require('nativewind/preset') */],
  darkMode: 'media',
  theme: {{
    extend: {{
      colors: {{
{''.join(f"        '{kebab(k)}': 'var(--vl-{kebab(k)})',\n" for k in LIGHT if k != 'scrim')}        brand: {{ {', '.join(f"'{kebab(k)}': '{v}'" for k, v in PALETTE.items())} }},
      }},
      fontFamily: {{ display: ['{FONTS['display']}'], body: ['{FONTS['body']}'], mono: ['{FONTS['mono']}'], hand: ['{FONTS['hand']}'] }},
      fontSize: {{
{''.join(f"        '{kebab(n)}': ['{s}px', {{ lineHeight: '{lh}px', fontWeight: '{w}', letterSpacing: '{ls}px' }}],\n" for n, f, s, lh, w, ls, u in TYPE)}      }},
      spacing: {{ {', '.join(f"'{k}': '{v}px'" for k, v in SPACE.items())} }},
      borderRadius: {{ {', '.join(f"{k}: '{v}px'" for k, v in RADII.items())} }},
      boxShadow: {{ {', '.join(f"{k}: '0 {v['y']}px {v['blur']}px {v['spread']}px rgba(20,28,40,{v['opacity']})'" for k, v in SHADOWS.items())} }},
      minHeight: {{ touch: '44px' }}, minWidth: {{ touch: '44px' }},
      transitionDuration: {{ fast: '{MOTION['fast']}ms', base: '{MOTION['base']}ms', slow: '{MOTION['slow']}ms' }},
      transitionTimingFunction: {{ volis: '{MOTION['easing']}' }},
    }},
  }},
}};
"""
open(f'{D}/tokens/tailwind.config.js', 'w').write(tw)
print('tokens ok')
# ---------------- ICONS ----------------
from common import P
import icons as IC0
EXTRA = {
 'close': 'M18 6 6 18M6 6l12 12',
 'external': 'M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5',
 'wifi-off': 'M2 8.8a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0M12 20h.01M3 3l18 18',
 'eye': 'M2.06 12.35a1 1 0 0 1 0-.7 10.75 10.75 0 0 1 19.88 0 1 1 0 0 1 0 .7 10.75 10.75 0 0 1-19.88 0M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6',
 'key': 'M2.59 17.41A2 2 0 0 0 2 18.83V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.17a2 2 0 0 0 1.42-.59l.81-.81a6.5 6.5 0 1 0-4-4zM16.5 7.5h.01',
 'star': 'M12 2.5l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.3 6.1 20.5l1.2-6.5L2.5 9.4l6.6-.9z',
 'trash': 'M3 6h18M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2M6 6l1 14a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1l1-14M10 11v6M14 11v6',
 'copy': 'M9 9h11v11H9zM5 15H4V4h11v1',
}
NAMES = {'chev': 'chevron-right', 'back': 'chevron-left', 'down': 'chevron-down', 'cal': 'calendar', 'chat': 'message', 'dollar': 'currency-dollar', 'id': 'id-card', 'qr': 'qr-code', 'doc': 'document', 'pin': 'map-pin', 'bank': 'bank', 'help': 'help-circle', 'info': 'info-circle', 'alert': 'alert-triangle', 'swap': 'arrows-swap', 'sort': 'sort'}
ALLI = {NAMES.get(k, k): v for k, v in {**P, **EXTRA}.items()}
idx_paths = {}
for n, d in sorted(ALLI.items()):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
           f'<path d="{d}"/></svg>\n')
    open(f'{D}/icons/svg/{n}.svg', 'w').write(svg); idx_paths[n] = d
rn = """// Volis — icônes React Native (react-native-svg). Grille 24 px, trait 2 px, extrémités arrondies.
// Usage : <Icon name="package" size={22} color={theme.colors.text} />
import * as React from 'react';
import Svg, { Path } from 'react-native-svg';

export const iconPaths = {
""" + ''.join(f"  '{n}': '{d}',\n" for n, d in sorted(idx_paths.items())) + """} as const;

export type IconName = keyof typeof iconPaths;
type Props = { name: IconName; size?: number; color?: string; strokeWidth?: number; accessibilityLabel?: string };

export function Icon({ name, size = 24, color = '#1E2A3A', strokeWidth = 2, accessibilityLabel }: Props) {
  const fill = name === 'star' ? color : 'none';
  return (
    <Svg width={size} height={size} viewBox="0 0 24 24" fill={fill} accessible={!!accessibilityLabel}
      accessibilityLabel={accessibilityLabel} accessibilityElementsHidden={!accessibilityLabel}>
      <Path d={iconPaths[name]} stroke={color} strokeWidth={strokeWidth} strokeLinecap="round" strokeLinejoin="round" />
    </Svg>
  );
}
export default Icon;
"""
open(f'{D}/icons/react-native/Icon.tsx', 'w').write(rn)
print('icons', len(ALLI))
# ---------------- ILLUSTRATIONS ----------------
ILL = {'a-voyageur': 'voyageur-valise-colis', 'b-remise': 'remise-colis-expediteur-voyageur', 'c-reception': 'reception-destinataire-coeur', 'd-connexion': 'salut-telephone', 'e-inscription': 'passeport-colis'}
for k, n in ILL.items():
    im = Image.open(f'/workspace/maquettes-v2/build/c1-{k}.png').convert('RGBA')
    bb = im.getbbox(); im = im.crop(bb)
    for sc in (3, 2, 1):
        w = round(im.width*sc/3); h = round(im.height*sc/3)
        r = im if sc == 3 else im.resize((w, h), Image.LANCZOS)
        sfx = '' if sc == 1 else f'@{sc}x'
        r.save(f'{D}/illustrations/{n}{sfx}.png', optimize=True)
        r.save(f'{D}/illustrations/{n}{sfx}.webp', 'WEBP', quality=90, method=6)
print('illustrations ok')
# ---------------- LOGOS + APP ICONS ----------------
shutil.copytree(f'{LOGO}/01-logo-principal', f'{D}/logos/logo-principal', dirs_exist_ok=True)
shutil.copytree(f'{LOGO}/02-symbole', f'{D}/logos/symbole', dirs_exist_ok=True)
shutil.copytree(f'{LOGO}/03-icone-app', f'{D}/app-icons', dirs_exist_ok=True)
shutil.copy(f'{LOGO}/LISEZMOI.txt', f'{D}/logos/LISEZMOI-kit-logo.txt')
for d_ in ('logos/logo-principal/pdf', 'logos/symbole/pdf'): pass
# ---------------- EXPO ----------------
from svgpng import svg2png
E = f'{D}/expo'
shutil.copy(f'{LOGO}/03-icone-app/ios/volis-icone-ios-1024.png', f'{E}/icon.png')
shutil.copy(f'{LOGO}/03-icone-app/ios/volis-icone-ios-sombre-1024-transparent.png', f'{E}/icon-ios-dark.png')
shutil.copy(f'{LOGO}/03-icone-app/ios/volis-icone-ios-teinte-1024-niveaux-de-gris.png', f'{E}/icon-ios-tinted.png')
A = f'{LOGO}/03-icone-app/android/svg-calques-108dp'
for lay in ('foreground', 'background', 'monochrome'):
    svg2png(f'{A}/ic_launcher_{lay}.svg', f'{E}/adaptive-icon-{lay}.png', 1024)
shutil.copy(f'{LOGO}/03-icone-app/favicon/favicon-48.png', f'{E}/favicon.png')
def splash(src, out, W=1200):
    im = Image.open(src).convert('RGBA'); im = im.crop(im.getbbox())
    im = im.resize((W, round(im.height*W/im.width)), Image.LANCZOS); im.save(out, optimize=True)
splash(f'{LOGO}/01-logo-principal/png-4000px-transparent/volis-logo-couleur-fond-creme.png', f'{E}/splash-icon.png')
splash(f'{LOGO}/01-logo-principal/png-4000px-transparent/volis-logo-fond-encre.png', f'{E}/splash-icon-dark.png')
app = {'expo': {
  'name': 'Volis', 'slug': 'volis', 'scheme': 'volis', 'version': '1.0.0', 'orientation': 'portrait', 'userInterfaceStyle': 'automatic',
  'icon': './assets/expo/icon.png',
  'ios': {'bundleIdentifier': 'app.volis.ios', 'supportsTablet': False,
          'icon': {'light': './assets/expo/icon.png', 'dark': './assets/expo/icon-ios-dark.png', 'tinted': './assets/expo/icon-ios-tinted.png'},
          'infoPlist': {'NSCameraUsageDescription': 'Volis utilise la caméra pour photographier votre colis et scanner le code de remise.', 'NSSupportsLiveActivities': True}},
  'android': {'package': 'app.volis.android',
              'adaptiveIcon': {'foregroundImage': './assets/expo/adaptive-icon-foreground.png', 'backgroundImage': './assets/expo/adaptive-icon-background.png', 'monochromeImage': './assets/expo/adaptive-icon-monochrome.png', 'backgroundColor': '#0F766E'}},
  'web': {'favicon': './assets/expo/favicon.png', 'bundler': 'metro'},
  'plugins': [['expo-splash-screen', {'image': './assets/expo/splash-icon.png', 'imageWidth': 200, 'resizeMode': 'contain', 'backgroundColor': '#F5F1E8',
                                       'dark': {'image': './assets/expo/splash-icon-dark.png', 'backgroundColor': '#121A24'}}],
              ['expo-font', {'fonts': ['./assets/fonts/PlusJakartaSans-ExtraBold.ttf', './assets/fonts/Inter-Regular.ttf']}],
              'expo-localization']}}
json.dump(app, open(f'{E}/app.json.snippet.json', 'w'), ensure_ascii=False, indent=2)
print('expo ok')
# ---------------- SCREENS + CSV ----------------
from flows import FLOWS
from inventory import INV
flow_of = {i: f'{c} · {t}' for c, t, ids in FLOWS for i in ids}
S = f'{D}/screens'
for f in sorted(glob.glob('/workspace/volis-design/ecrans/*.png')): shutil.copy(f, S)
with open(f'{D}/screens/inventaire-ecrans.csv', 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.writer(fh); w.writerow(['id', 'fichier', 'nom', 'parcours', 'objectif', 'composants_cles', 'barre_onglets'])
    TAB = {'07': 'Accueil', '08': 'Accueil', '36': 'Accueil', '39': 'Accueil', '12': 'Envois', '30': 'Envois', '15': 'Voyages', '31': 'Voyages', '14': 'Messages', '16': 'Profil', '44': 'Profil'}
    for f in sorted(os.listdir(S)):
        if not f.endswith('.png'): continue
        i = f[:2]; n, p, k = INV[i]
        w.writerow([i, f, n, flow_of[i], p, k, TAB.get(i, '—')])
shutil.copy('/workspace/volis-design/volis-ecrans-concept1.pdf', f'{D}/screens/')
# fix fonts in app.json
app = json.load(open(f'{D}/expo/app.json.snippet.json'))
app['expo']['plugins'][1] = ['expo-font', {'fonts': [f'./assets/fonts/{x}' for x in sorted(os.listdir(f'{D}/fonts')) if x.endswith('.ttf')]}]
json.dump(app, open(f'{D}/expo/app.json.snippet.json', 'w'), ensure_ascii=False, indent=2)
print('screens', len([x for x in os.listdir(S) if x.endswith('.png')]))
