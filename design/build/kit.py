import sys
sys.path.insert(0, '/workspace/maquettes-v4/build')
from common import *
import screens as S
from screens import hdr, sect, rowkv, checkrow, stepper
SC = False
SUCC_BG='#D8F0DF'; SUCC_FG='#14532D'; WARN_BG='#FFF0E0'; WARN_BD='#E0A458'; WARN_FG='#6B3A06'; WARN_IC='#8A4B08'
ERR='#B42318'; ERR_BG='#FDE7E4'; ERR_FG='#8F1D14'; INFO_BG='#E3ECF8'; INFO_FG='#1F4E8C'; DIS='#B9B09E'
def pg(body, tab=None, deco='', bg=CREAM, overlay=''):
    h = page(False, f'<div class="ct" style="padding-top:2px">{body}</div>', tab, deco, bg)
    if overlay: h = h.replace('</div></body>', overlay + '</div></body>', 1)
    return h
def illus(name, h, style=''):
    return f'<img src="{ill(name)}" style="height:{h}px;object-fit:contain;display:block;{style}"/>'
def status(label, kind='ok', dot=True):
    m = {'ok': (SUCC_BG, SUCC_FG), 'warn': (WARN_BG, WARN_FG), 'err': (ERR_BG, ERR_FG), 'info': (INFO_BG, INFO_FG), 'teal': (TSEL, '#0B5B55'),
         'ink': (INK, '#FFFFFF'), 'mute': ('#EAE2D2', T2), 'sand': (SAND, INK)}[kind]
    d = f'<i style="width:7px;height:7px;border-radius:4px;background:{m[1]};flex:none"></i>' if dot else ''
    return f'<span class="badge" style="background:{m[0]};color:{m[1]}">{d}{label}</span>'
def banner(kind, title, text, icn=None):
    bg, fg, bd, ic_ = {'warn': (WARN_BG, WARN_FG, WARN_BD, WARN_IC), 'err': (ERR_BG, ERR_FG, '#F2A79E', ERR), 'info': (INFO_BG, INFO_FG, '#A9C1E6', INFO_FG),
                       'ok': (SUCC_BG, SUCC_FG, '#9BD3AE', SUCC_FG), 'teal': (MINT, '#0B5B55', '#A8D5CC', '#0B5B55')}[kind]
    icn = icn or {'warn': 'alert', 'err': 'alert', 'info': 'info', 'ok': 'check', 'teal': 'shield'}[kind]
    t = f'<span style="font:700 14px/18px Inter;color:{fg}">{title}</span>' if title else ''
    x = f'<span style="font:400 13px/18px Inter;color:{INK}">{text}</span>' if text else ''
    return (f'<div class="row" style="flex:none;gap:10px;padding:11px 12px;border-radius:14px;background:{bg};border:1.5px solid {bd};align-items:flex-start">'
            f'<span style="margin-top:1px">{ic(icn, ic_, 18, 2.2)}</span><div class="col" style="flex:1;gap:2px">{t}{x}</div></div>')
def btn(label, kind='primary', icn=None, h=56, style=''):
    st = {'primary': f'background:{TEAL};color:#fff', 'ink': f'background:{INK};color:#fff', 'secondary': f'background:{CARD};color:{TEAL};border:2px solid {TEAL}',
          'ghost': f'background:transparent;color:{TEAL}', 'danger': f'background:{ERR};color:#fff', 'danger2': f'background:{CARD};color:{ERR};border:2px solid {ERR}',
          'disabled': f'background:#E2DACB;color:#6F6A60', 'coral': f'background:{CORAL};color:{INK}'}[kind]
    c = '#fff' if kind in ('primary', 'ink', 'danger') else (ERR if kind == 'danger2' else ('#6F6A60' if kind == 'disabled' else (INK if kind == 'coral' else TEAL)))
    i_ = ic(icn, c, 19, 2.3) if icn else ''
    return f'<div class="row" style="height:{h}px;border-radius:{h//2}px;justify-content:center;gap:8px;font:700 {17 if h>=52 else 15}px/22px Inter;flex:none;{st};{style}">{i_}{label}</div>'
def toggle(on=True):
    return (f'<span style="width:51px;height:31px;border-radius:16px;background:{TEAL if on else "#CFC6B4"};position:relative;flex:none;display:block">'
            f'<i style="position:absolute;top:2px;{"right" if on else "left"}:2px;width:27px;height:27px;border-radius:14px;background:#fff;box-shadow:0 2px 4px rgba(0,0,0,.2)"></i></span>')
def radio(on):
    return f'<span style="width:22px;height:22px;border-radius:11px;border:2px solid {TEAL if on else "#7E7A70"};display:flex;align-items:center;justify-content:center;flex:none">{"<i style=\'width:12px;height:12px;border-radius:6px;background:%s\'></i>" % TEAL if on else ""}</span>'
def box(on): return f'<div class="cb">{ic("check", "#fff", 16, 3)}</div>' if on else f'<div class="cb" style="background:{CARD};border:2px solid #7E7A70"></div>'
def card(inner, style=''): return f'<div class="cd" style="flex:none;{style}">{inner}</div>'
def chip(t, on=False, icn=None, style=''):
    return f'<span class="chip{" sel" if on else ""}" style="height:40px;font-size:14px;padding:0 13px;{style}">{ic(icn, TEAL if on else T2, 16) if icn else ""}{t}</span>'
def seg(items, active):
    s = ''.join(f'<div class="row" style="flex:1;height:38px;justify-content:center;border-radius:19px;font:{"700" if i==active else "600"} 14px/18px Inter;color:{INK if i==active else T2};{"background:#FFFDF8;box-shadow:0 1px 3px rgba(30,42,58,.18);" if i==active else ""}">{t}</div>' for i, t in enumerate(items))
    return f'<div class="row" style="flex:none;height:44px;padding:3px;border-radius:22px;background:#E9E1D1;gap:2px" role="tablist">{s}</div>'
def listrow(icn, label, val='', first=False, color=INK, chev=True, h=50, sub=''):
    sb = f'<span class="xs" style="font-weight:500">{sub}</span>' if sub else ''
    return (f'<div class="row" style="gap:12px;min-height:{h}px;{"" if first else "border-top:1.5px solid "+LINE}">{ic(icn, color, 20) if icn else ""}'
            f'<div class="col" style="flex:1;padding:6px 0"><span class="b15" style="font-weight:500;color:{color}">{label}</span>{sb}</div><span class="xs" style="font-weight:500">{val}</span>{ic("chev", T2, 18) if chev else ""}</div>')
def field(lab, val, icn=None, ph=False, state='', help_='', suf='', h=50):
    bd = {'focus': f'border:2px solid {TEAL};box-shadow:0 0 0 4px #D6ECE8', 'err': f'border:2px solid {ERR}', 'ok': f'border:1.5px solid {TEAL}', '': ''}[state]
    hc = ERR if state == 'err' else T2
    hp = f'<span class="row" style="gap:5px;font:500 13px/18px Inter;color:{hc}">{ic("alert", ERR, 14) if state=="err" else ""}{help_}</span>' if help_ else ''
    l_ = f'<span class="lab">{lab}</span>' if lab else ''
    return (f'<div class="fld" style="flex:none">{l_}<div class="inp" style="height:{h}px;{bd}">{ic(icn, T2, 18) if icn else ""}'
            f'<span style="flex:1;white-space:nowrap;{"color:#6F6A60;font-weight:400" if ph else ""}">{val}</span>{suf}</div>{hp}</div>')
def iconcircle(icn, bg=TSEL, c='#0B5B55', s=44, isz=22):
    return f'<div style="width:{s}px;height:{s}px;border-radius:{s//2}px;background:{bg};display:flex;align-items:center;justify-content:center;flex:none">{ic(icn, c, isz, 2.2)}</div>'
def sheet(inner, top=300, dim=True):
    d = f'<div class="abs" style="inset:0;background:rgba(20,28,40,.45);z-index:40"></div>' if dim else ''
    return (d + f'<div class="abs" style="left:0;right:0;top:{top}px;bottom:0;background:{CARD};border-radius:28px 28px 0 0;z-index:41;padding:8px 16px 0;display:flex;flex-direction:column;box-shadow:0 -10px 30px rgba(20,28,40,.25)">'
            f'<div style="width:40px;height:5px;border-radius:3px;background:#B9B09E;margin:0 auto 6px;flex:none"></div>{inner}'
            f'<div style="height:34px;flex:none;margin-top:auto;display:flex;justify-content:center;align-items:flex-end;padding-bottom:8px"><div style="width:134px;height:5px;border-radius:3px;background:{INK}"></div></div></div>')
def h1(t, sub='', mt=10, size=26):
    s = f'<div style="font:400 15px/22px Inter;color:{T2};margin-top:6px">{sub}</div>' if sub else ''
    return f'<div class="col" style="flex:none;margin-top:{mt}px"><div class="h1" style="font-size:{size}px;line-height:{size+6}px">{t}</div>{s}</div>'
def blob(seed, x, y, r, c, o=.55):
    return f'<div class="abs" style="left:0;top:0">{blobsvg(393,852,[(seed,x,y,r,c,o)])}</div>'
def sp(h): return f'<div style="height:{h}px;flex:none"></div>'
