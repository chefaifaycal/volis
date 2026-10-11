# Source unique des design tokens Volis (concept 1 « Carnet de voyage »)
LIGHT = {
 'bg': '#F5F1E8', 'surface': '#FFFDF8', 'surfaceSunken': '#EFE8DA', 'surfaceInverse': '#1E2A3A',
 'text': '#1E2A3A', 'textSecondary': '#4E5A69', 'textMuted': '#6F6A60', 'textInverse': '#FFFFFF', 'textOnAccent': '#1E2A3A',
 'primary': '#0F766E', 'primaryPressed': '#0B5B55', 'primarySubtle': '#D6ECE8', 'onPrimary': '#FFFFFF',
 'secondary': '#1E2A3A', 'onSecondary': '#FFFFFF',
 'accent': '#FF7A59', 'accentSubtle': '#FFE1D6', 'mint': '#DCEFEA', 'sand': '#FFE9C7',
 'border': '#7E7A70', 'borderSubtle': '#E4DACA', 'divider': '#DCD3C2', 'disabledBg': '#E2DACB', 'disabledText': '#6F6A60',
 'success': '#15803D', 'successText': '#14532D', 'successBg': '#D8F0DF',
 'warning': '#B45309', 'warningText': '#6B3A06', 'warningBg': '#FFF0E0', 'warningBorder': '#E0A458',
 'error': '#B42318', 'errorText': '#8F1D14', 'errorBg': '#FDE7E4',
 'info': '#1F4E8C', 'infoText': '#1F4E8C', 'infoBg': '#E3ECF8',
 'focusRing': '#0F766E', 'scrim': 'rgba(20,28,40,0.45)',
}
DARK = {
 'bg': '#121A24', 'surface': '#1B2533', 'surfaceSunken': '#0D141C', 'surfaceInverse': '#F5F1E8',
 'text': '#F3EEE4', 'textSecondary': '#B6BFCB', 'textMuted': '#8E98A6', 'textInverse': '#1E2A3A', 'textOnAccent': '#1E2A3A',
 'primary': '#3FB8AC', 'primaryPressed': '#5FCFC3', 'primarySubtle': '#16403D', 'onPrimary': '#0B1F1D',
 'secondary': '#F3EEE4', 'onSecondary': '#1E2A3A',
 'accent': '#FF8D6F', 'accentSubtle': '#4A2A22', 'mint': '#173A36', 'sand': '#3D3222',
 'border': '#6B7788', 'borderSubtle': '#2E3A4B', 'divider': '#2A3545', 'disabledBg': '#2A3442', 'disabledText': '#8E98A6',
 'success': '#4ADE80', 'successText': '#86EFAC', 'successBg': '#143323',
 'warning': '#FBBF6A', 'warningText': '#FCD38D', 'warningBg': '#3A2A12', 'warningBorder': '#8A5A16',
 'error': '#FF8A80', 'errorText': '#FFB4AB', 'errorBg': '#3D1A17',
 'info': '#8AB4F8', 'infoText': '#AECBFA', 'infoBg': '#16263D',
 'focusRing': '#3FB8AC', 'scrim': 'rgba(0,0,0,0.6)',
}
PALETTE = {  # couleurs de marque brutes
 'creme': '#F5F1E8', 'papier': '#FFFDF8', 'encre': '#1E2A3A', 'ardoise': '#4E5A69', 'sarcelle': '#0F766E', 'sarcelleFoncee': '#0B5B55',
 'sarcelleClaire': '#D6ECE8', 'menthe': '#DCEFEA', 'corail': '#FF7A59', 'peche': '#FFE1D6', 'sable': '#FFE9C7', 'lin': '#E4DACA', 'taupe': '#7E7A70',
}
FONTS = {'display': 'Plus Jakarta Sans', 'body': 'Inter', 'mono': 'JetBrains Mono', 'hand': 'Caveat'}
TYPE = [  # nom, famille, taille, interligne, graisse, tracking, usage
 ('display', 'display', 34, 40, 800, -0.8, 'Écran de bienvenue, gros montants'),
 ('h1', 'display', 26, 32, 800, -0.5, 'Titre d’écran'),
 ('h2', 'display', 22, 28, 800, -0.3, 'Titre de section importante'),
 ('h3', 'display', 19, 24, 800, 0, 'En-tête de navigation'),
 ('title', 'display', 17, 22, 800, 0, 'Titre de carte'),
 ('bodyLg', 'body', 16, 22, 500, 0, 'Champs de saisie, texte principal'),
 ('body', 'body', 15, 21, 400, 0, 'Texte courant'),
 ('bodySm', 'body', 14, 20, 400, 0, 'Texte secondaire'),
 ('label', 'body', 14, 18, 600, 0, 'Étiquettes de champs'),
 ('caption', 'body', 13, 18, 500, 0, 'Aide, métadonnées'),
 ('micro', 'body', 12, 16, 600, 0, 'Badges, horodatage (minimum absolu)'),
 ('tab', 'body', 11, 14, 600, 0, 'Libellés barre d’onglets (exception iOS)'),
 ('button', 'body', 17, 22, 700, 0, 'Bouton principal'),
 ('buttonSm', 'body', 15, 20, 700, 0, 'Bouton secondaire / compact'),
 ('code', 'mono', 32, 32, 700, 0, 'Code de remise 4821'),
 ('monoMd', 'mono', 15, 20, 700, 0, 'Codes aéroport, n° de vol'),
 ('monoSm', 'mono', 12, 16, 600, 0, 'Références (VL-4821)'),
 ('hand', 'hand', 21, 22, 600, 0, 'Annotations décoratives uniquement'),
]
SPACE = {'0': 0, '0.5': 4, '1': 8, '1.5': 12, '2': 16, '2.5': 20, '3': 24, '4': 32, '5': 40, '6': 48, '8': 64}
RADII = {'xs': 6, 'sm': 10, 'md': 14, 'lg': 20, 'xl': 28, 'pill': 999}
SHADOWS = {
 'e0': {'y': 0, 'blur': 0, 'spread': 0, 'opacity': 0, 'use': 'Cartes à plat (bordure 1,5 px lin)'},
 'e1': {'y': 2, 'blur': 6, 'spread': 0, 'opacity': 0.12, 'use': 'Segment actif, puces'},
 'e2': {'y': 8, 'blur': 20, 'spread': -8, 'opacity': 0.30, 'use': 'Cartes flottantes sur carte, épingles'},
 'e3': {'y': -10, 'blur': 30, 'spread': 0, 'opacity': 0.25, 'use': 'Bottom sheet'},
 'e4': {'y': 20, 'blur': 50, 'spread': 0, 'opacity': 0.35, 'use': 'Modales, toasts'},
}
SHADOW_COLOR = '#141C28'
MOTION = {'instant': 100, 'fast': 150, 'base': 250, 'slow': 400, 'easing': 'cubic-bezier(0.2, 0, 0, 1)', 'easingExit': 'cubic-bezier(0.3, 0, 1, 1)', 'spring': {'damping': 18, 'stiffness': 220}}
LAYOUT = {'screenMargin': 16, 'gutter': 12, 'columns': 4, 'minTouch': 44, 'tabBarHeight': 60, 'headerHeight': 48, 'ctaHeight': 56, 'inputHeight': 50}
def _lin(c):
    c = c / 255
    return c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
def lum(h):
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return 0.2126*_lin(r)+0.7152*_lin(g)+0.0722*_lin(b)
def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la+0.05)/(lb+0.05)
PAIRS = [('text', 'bg'), ('text', 'surface'), ('textSecondary', 'bg'), ('textSecondary', 'surface'), ('textMuted', 'surface'), ('onPrimary', 'primary'), ('primary', 'bg'), ('primary', 'surface'),
         ('textOnAccent', 'accent'), ('successText', 'successBg'), ('warningText', 'warningBg'), ('errorText', 'errorBg'), ('error', 'surface'), ('infoText', 'infoBg'), ('border', 'surface'), ('disabledText', 'disabledBg')]
if __name__ == '__main__':
    for nm, T in (('clair', LIGHT), ('sombre', DARK)):
        for a, b in PAIRS: print(nm, a, b, round(contrast(T[a], T[b]), 2))
