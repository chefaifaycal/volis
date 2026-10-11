p='/workspace/volis/cdc-technique-securite.md';s=open(p).read()
def R(a,b):
    global s
    assert a in s,a[:70]; s=s.replace(a,b,1)
REG="https://supabase.com/docs/guides/platform/regions"
R("| Hébergement au Canada | Région canadienne : **à confirmer** | Selon l'hébergeur choisi : **à confirmer** |",
  "| Hébergement au Canada | Région **Canada (Central)**, code `ca-central-1` (vérifié dans la doc Supabase « Available regions ») | Selon l'hébergeur choisi : **à confirmer** |")
R("- Pour garder une porte de sortie,",
  "- **Région : Canada (Central), `ca-central-1`** (existence vérifiée dans la doc Supabase, "+REG+"). Il faut choisir cette **région précise** à la création du projet, et non la région générale « Americas », qui déploie dans une région AWS de la zone (par ex. Virginie du Nord). Ce choix est **recommandé, pas exigé par la loi** : il allège l'évaluation des transferts hors Québec dans l'ÉFVP, puisque la base, le stockage et l'authentification restent au Canada. Selon l'équipe juridique, il ne reste alors que Stripe à justifier. **À faire valider par l'avocat.** Point technique à signaler à l'équipe juridique : d'autres fournisseurs reçoivent aussi des données (Sentry, service push d'Expo, éventuel outil d'analytics, assureur partenaire) et doivent figurer dans l'ÉFVP. Les Edge Functions peuvent être invoquées dans `ca-central-1` (doc Supabase « Regional Invocations ») : à configurer.\n- Pour garder une porte de sortie,")
R("effacement (redact) des sessions selon la politique de conservation (la doc Stripe indique que l'effacement peut prendre jusqu'à 4 jours).",
  "**effacement (redact) de la session Stripe Identity dès que la vérification est faite** (voir 3.1 ; la doc Stripe indique que l'effacement peut prendre jusqu'à 4 jours et émet `identity.verification_session.redacted`).")
R("Données à conserver pour obligations légales (paiements, litiges) : liste et durées **à confirmer avec l'équipe juridique**.",
  "Les données soumises à une obligation de conservation (paiements, preuves de litige, consentements, registre des incidents) sont conservées selon le tableau 3.1, puis détruites ou anonymisées.")
i24=s.index("| SEC-24 |"); e24=s.index("\n",i24)+1
row25="| SEC-25 | **Purge et conservation automatisées** : tâches planifiées (par ex. `pg_cron` ou fonction planifiée, **à confirmer**) qui appliquent les durées du tableau 3.1, puis détruisent ou anonymisent les données ; **gel légal** (`legal_hold`) qui suspend la purge des éléments liés à un litige ou à une rétrofacturation en cours ; journal des purges sans données personnelles. | MASVS-PRIVACY-4 ; Loi 25 (art. 23) | Test automatisé en CI : données fictives datées → purgées ou anonymisées à l'échéance ; données sous gel légal → conservées ; session Identity vérifiée → redact demandé. |\n"
s=s[:e24]+row25+s[e24:]
tbl='''
## 3.1 Durées de conservation et purge (SEC-19, SEC-25)

> **À faire valider par l'avocat.** Durées fournies par l'équipe juridique. Le point de départ de chaque délai doit être stocké explicitement (date de fin d'année fiscale, date de livraison, date de prise de connaissance de l'incident, date de fermeture du compte).

| Données | Durée de conservation | Fondement (selon l'équipe juridique) | Mise en œuvre technique |
|---|---|---|---|
| Paiements, factures, commissions | 6 ans après la fin de l'année fiscale concernée | Lois fiscales fédérale et québécoise | Tables `payments`, `transfers`, reçus ; purge annuelle après l'échéance. Les objets chez Stripe suivent les règles de Stripe. |
| Preuves de litige (photos de remise, confirmations, messages liés) | 3 ans après la livraison ; **prolongé si un litige est en cours** | Prescription, C.c.Q. art. 2925 | `delivery_proofs`, `dispute_evidence`, messages rattachés ; gel légal actif tant que le litige ou la rétrofacturation n'est pas clos. |
| Registre des incidents de confidentialité | 5 ans à partir de la prise de connaissance de l'incident | Règlement de la Loi 25 | `security_incidents.discovered_at` comme point de départ. |
| Preuves de consentement | Toute la durée du compte, puis 3 ans | Équipe juridique | Table `consents` (finalité, version du texte, date, retrait) ; purge 3 ans après la fermeture du compte. |
| Géolocalisation et messages **sans litige** | Supprimés dès la fin de la livraison et du délai de contestation | Minimisation (Loi 25) | Purge déclenchée par la transition vers « Fonds libérés » (délai de contestation écoulé), sauf gel légal. |
| Session Stripe Identity | Effacée dès que la vérification est faite | Minimisation (Loi 25) ; biométrie | Appel `redact` à la réception de `identity.verification_session.verified` ; Volis ne garde que `identity_status` et l'ID de session. Traitement après un échec définitif : **à faire valider par l'avocat**. |

**Après ces délais : destruction ou anonymisation** (Loi 25, art. 23). L'anonymisation doit être irréversible ; sinon, on détruit.

Exigences techniques (SEC-25) :

- **Tâches de purge planifiées**, idempotentes, exécutées côté serveur, avec un journal (catégorie, nombre d'éléments, date) sans données personnelles. Les fichiers du stockage sont supprimés en même temps que leurs lignes.
- **Gel légal** : table `legal_holds` (ressource, motif, ouvert le, levé le), posé automatiquement à `charge.dispute.created` et à l'ouverture d'un litige interne, levé à la clôture. Toute purge vérifie l'absence de gel.
- **Sauvegardes** : leur durée de rétention doit rester compatible avec ces délais (une donnée purgée disparaît des sauvegardes à leur expiration) : **à confirmer** selon l'offre Supabase.
- **Test automatisé** en CI (critère de SEC-25).
'''
R("\n# 4. Monétisation", tbl+"\n# 4. Monétisation")
R("| `stripe_events` |","| `legal_holds` | ressource visée, motif (litige, rétrofacturation), ouvert le, levé le | Suspend la purge (voir 3.1). |\n| `consents` | utilisateur, finalité, version du texte, accordé le, retiré le | Preuves de consentement (voir 3.1). |\n| `stripe_events` |")
R("| **prod** | Projet Supabase de production, accès restreint |","| **prod** | Projet Supabase de production, région **Canada (Central)** `ca-central-1`, accès restreint |")
R("| **staging** | Projet Supabase séparé, mêmes migrations |","| **staging** | Projet Supabase séparé (même région que la prod), mêmes migrations |")
R("- Supabase Auth : https://supabase.com/docs/guides/auth","- Supabase, régions disponibles : "+REG+" · Invocations régionales : https://supabase.com/docs/guides/functions/regional-invocation\n- Supabase Auth : https://supabase.com/docs/guides/auth")
open(p,'w').write(s)
