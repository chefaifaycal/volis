FLOWS = [
 ('A', 'Accueil, connexion et compte', ['01','02','03','04','05','06','23','24','25']),
 ('B', 'Vérification d’identité (Stripe Identity)', ['17','18','19','20','21','22']),
 ('C', 'Recherche et réservation', ['07','08','38','39','36','09','10','11','40']),
 ('D', 'Envoi, remise et suivi', ['30','27','28','29','43','14','13','37','12','50','33']),
 ('E', 'Côté voyageur', ['15','31','26','49']),
 ('F', 'Imprévus, litiges et aide', ['34','35','44','45']),
 ('G', 'Profil, portefeuille et réglages', ['16','41','42','32','46','47','48']),
]
LABEL = {
 '01':'Splash','02':'Onboarding 1 · Envoyez','03':'Onboarding 2 · Voyagez','04':'Onboarding 3 · Confiance','05':'Connexion','06':'Inscription',
 '07':'Accueil','08':'Résultats de recherche','09':'Profil voyageur','10':'Créer un envoi · 2/4','11':'Paiement protégé + assurance','12':'Suivi du colis',
 '13':'Remise (QR + code)','14':'Messages','15':'Publier un voyage','16':'Profil / Portefeuille','17':'Vérif. identité · intro','18':'Consentement biométrique',
 '19':'Stripe Identity (hébergé)','20':'Résultat · vérifiée','21':'Résultat · en attente','22':'Résultat · échec','23':'Mot de passe oublié','24':'Lien envoyé',
 '25':'Vérification téléphone (SMS)','26':'Demande · côté voyageur','27':'Envoi · en attente','28':'Envoi · accepté','29':'Envoi · refusé','30':'Mes envois',
 '31':'Mes voyages','32':'Notifications','33':'Livraison + avis double aveugle','34':'Vol annulé · réattribuer','35':'Signaler / litige','36':'État vide + alerte',
 '37':'Remise hors ligne','38':'Filtres (bottom sheet)','39':'Vue carte','40':'Assurance optionnelle','41':'Versements','42':'Configurer versements Stripe',
 '43':'Ajouter un destinataire','44':'Centre d’aide','45':'Objets interdits','46':'Réglages','47':'Supprimer mon compte','48':'Suppression · confirmation',
 '49':'Attestation douane (voyageur)','50':'Live Activity iOS'}
