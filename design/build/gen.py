import sys, importlib
mods = ['fa', 'fb', 'fc', 'fd', 'fe']
ALL = []
for m in mods:
    try: ALL += importlib.import_module(m).__dict__[m.upper()]
    except ModuleNotFoundError: pass
only = sys.argv[1:]
for n, fn in ALL:
    if only and not any(n.startswith(o) for o in only): continue
    h = fn()
    if n[:2] in ('08', '09', '38', '39'):
        h = h.replace(">31 $<", ">27,60 $<").replace("</span>31 $</div>", "</span>27,60 $</div>").replace("font:800 21px/24px 'Plus Jakarta Sans'\">27,60", "font:800 21px/24px 'Plus Jakarta Sans';white-space:nowrap\">27,60")
    if n[:2] == '39':
        h = h.replace("font:800 21px/24px 'Plus Jakarta Sans';white-space:nowrap", "font:800 18px/22px 'Plus Jakarta Sans';white-space:nowrap")
    open(f'html/{n}.html', 'w').write(h)
print(len(ALL))
