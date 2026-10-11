"""Vérifie que les dépendances du guide existent et ne forment aucun cycle."""
import sys; sys.path.insert(0, '.')
from content import PHASES
S = {s['id']: s for p in PHASES for s in p['steps']}
unknown = [(i, d) for i, s in S.items() for d in s['deps'] if d not in S]
color, cycles = {}, []
def dfs(u, path):
    color[u] = 1
    for v in S[u]['deps']:
        if color.get(v) == 1: cycles.append(path + [v])
        elif not color.get(v): dfs(v, path + [v])
    color[u] = 2
for u in S:
    if not color.get(u): dfs(u, [u])
print(f'{len(S)} étapes · dépendances inconnues : {unknown or "aucune"} · cycles : {cycles or "aucun"}')
sys.exit(1 if unknown or cycles else 0)
