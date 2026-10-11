# supabase/

Dossier réservé au backend Supabase de Volis. **Aucun projet Supabase réel n'a encore été créé.**

## Règles non négociables

- **Région : `ca-central-1` (Canada, Montréal).** Le projet devra être créé dans cette région pour garder les données personnelles au Canada (Loi 25 au Québec, LPRPDE), comme prévu au cahier technique (`docs/cdc-technique-securite.md`).
- **RLS (Row Level Security) obligatoire sur toutes les tables** du schéma `public`, activée dans la même migration que la création de la table, avec des politiques explicites (lecture/écriture limitées à `auth.uid()`). Une table sans RLS ne doit jamais être fusionnée.
- Les tables sensibles (`payments`, `transfers`, statuts de réservation, etc.) ne sont **écrites que par le serveur** (Edge Functions avec la clé `service_role`), jamais par l'application.
- La clé `service_role` et les clés secrètes Stripe (`sk_...`, secrets de webhook) restent dans les secrets Supabase / la CI. **Jamais dans ce dépôt, jamais dans une variable `EXPO_PUBLIC_*`.**

## Structure prévue (cahier technique, partie B §2.3)

```text
supabase/
  migrations/   # schéma SQL versionné + politiques RLS
  functions/    # Edge Functions (stripe-webhook, release-funds, …)
  tests/        # tests RLS et tests de fonctions
```

## Démarrage (le moment venu)

```bash
npx supabase init          # génère config.toml dans ce dossier
npx supabase start         # environnement local (Docker)
npx supabase migration new init_schema
```
