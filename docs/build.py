from reportlab.lib.pagesizes import letter
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
D='/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV',D+'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB',D+'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DVI',D+'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVBI',D+'DejaVuSans-Bold.ttf'))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('DV',normal='DV',bold='DVB',italic='DVI',boldItalic='DVBI')
NAVY=colors.HexColor('#1F3A5F'); TEAL=colors.HexColor('#2A7F8E'); LIGHT=colors.HexColor('#EAF2F5'); WARN=colors.HexColor('#FFF4E0'); WARNB=colors.HexColor('#E0A030')
body=ParagraphStyle('b',fontName='DV',fontSize=9,leading=12.1,spaceAfter=3)
small=ParagraphStyle('s',parent=body,fontSize=8,leading=10.5)
cell=ParagraphStyle('c',parent=body,fontSize=8.3,leading=10.6,spaceAfter=0)
cellh=ParagraphStyle('ch',parent=cell,fontName='DVB',textColor=colors.white)
h1=ParagraphStyle('h1',fontName='DVB',fontSize=13.5,leading=17,textColor=NAVY,spaceBefore=10,spaceAfter=5,keepWithNext=1)
h2=ParagraphStyle('h2',fontName='DVB',fontSize=10.5,leading=14,textColor=TEAL,spaceBefore=6,spaceAfter=3,keepWithNext=1)
bul=ParagraphStyle('bul',parent=body,bulletFontName='DV',leftIndent=13,bulletIndent=3,spaceAfter=1.5)
chk=ParagraphStyle('chk',parent=body,bulletFontName='DV',bulletFontSize=10,leftIndent=16,bulletIndent=2,spaceAfter=2)
title=ParagraphStyle('t',fontName='DVB',fontSize=19,leading=24,textColor=NAVY,spaceAfter=4)
sub=ParagraphStyle('st',fontName='DV',fontSize=11,leading=15,textColor=TEAL,spaceAfter=8)
def L(url,txt=None): return f'<link href="{url}" color="#2A7F8E"><u>{txt or url}</u></link>'
def P(t,s=body): return Paragraph(t,s)
def B(items): return [Paragraph(i,bul,bulletText='•') for i in items]
def C(items): return [Paragraph(i,chk,bulletText='☐') for i in items]
def T(rows,widths,head=True,cs=None):
    cs=cs or cell
    data=[[Paragraph(c,cellh if (head and r==0) else cs) for c in row] for r,row in enumerate(rows)]
    t=Table(data,colWidths=widths,repeatRows=1 if head else 0)
    st=[('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#B8C7D0')),('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]
    if head: st+=[('BACKGROUND',(0,0),(-1,0),NAVY)]
    for r in range(1 if head else 0,len(rows)):
        if r%2==0: st.append(('BACKGROUND',(0,r),(-1,r),LIGHT))
    t.setStyle(TableStyle(st)); return t
def box(text,bg=WARN,border=WARNB):
    t=Table([[Paragraph(text,body)]],colWidths=[17.6*cm])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),bg),('BOX',(0,0),(-1,-1),1,border),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    return t
W=17.6*cm
def deco(c,doc):
    c.saveState(); c.setFillColor(NAVY); c.rect(0,letter[1]-0.55*cm,letter[0],0.55*cm,fill=1,stroke=0)
    c.setFont('DV',7.5); c.setFillColor(colors.grey)
    c.drawString(2*cm,1.1*cm,'Projet Volis — Fiche de recherche · 11 octobre 2026 · Faycal Chefai (Trois-Rivières, QC)')
    c.drawRightString(letter[0]-2*cm,1.1*cm,f'Page {doc.page}')
    c.drawString(2*cm,0.75*cm,'Document d’information — ne constitue pas un avis juridique.')
    c.restoreState()
doc=BaseDocTemplate('/workspace/projet-volis-fiche-recherche.pdf',pagesize=letter,leftMargin=2*cm,rightMargin=2*cm,topMargin=1.6*cm,bottomMargin=1.8*cm,
    title='Projet Volis — Fiche de recherche (technique, paiements, légal, design, lancement)',author='Faycal Chefai',subject='Projet Volis',lang='fr-CA')
doc.addPageTemplates([PageTemplate(id='p',frames=[Frame(doc.leftMargin,doc.bottomMargin,doc.width,doc.height,id='f')],onPage=deco)])
s=[]
s+=[P('Projet Volis — Fiche de recherche',title),P('Technique · Paiements · Légal · Design · Lancement',sub)]
s+=[T([['Préparé pour','Faycal Chefai — Trois-Rivières (Québec)'],['Date','11 octobre 2026'],
      ['Projet','Volis : application de mise en relation entre expéditeurs de colis et voyageurs qui les transportent'],
      ['Plateformes','iOS, Android et web']],[3.5*cm,W-3.5*cm],head=False)]
s+=[Spacer(1,8),box('<b>⚠ Avertissement.</b> Le présent document est une synthèse de recherche à titre informatif seulement. '
   '<b>Il ne constitue pas un avis juridique, fiscal ni financier.</b> Tous les éléments légaux, réglementaires et fiscaux '
   '(responsabilité, protection du consommateur, Loi 25, CANAFE/AMF, TPS/TVQ, international) doivent être <b>validés par un avocat '
   'membre du Barreau du Québec</b> (et, au besoin, par un comptable) avant le lancement.')]
s+=[Spacer(1,4),P('<b>En bref :</b> un seul code Expo pour les trois plateformes; un serveur qui décide seul de la libération des paiements; '
   'Stripe Connect (« separate charges and transfers ») et Stripe Identity au lancement; Interac reporté; lancement au Canada d’abord, '
   'puis pays par pays.')]

s+=[P('1. Architecture technique',h1)]
s+=B(['<b>Un seul code</b> avec <b>Expo (React Native) + Expo Router</b> pour iOS, Android et web — les maquettes sont prêtes pour cette approche. '+L('https://docs.expo.dev/router/introduction/','Documentation Expo Router'),
 '<b>Backend Node ou Supabase</b> qui reçoit les <b>webhooks Stripe</b>.',
 '<b>Règle d’or : c’est le serveur qui décide de libérer un paiement, jamais l’application.</b> L’app ne fait qu’afficher un statut fourni par le serveur.'])
s+=[Spacer(1,3),T([['Couche','Rôle'],
  ['UI (MVVM)','Écrans + ViewModels : état d’affichage, actions de l’utilisateur.'],
  ['Domaine (optionnel)','Cas d’usage / règles métier réutilisables.'],
  ['Data (repositories)','Accès aux données (API backend, Supabase, cache) derrière des repositories.'],
  ['Serveur','Webhooks Stripe, logique de libération des fonds, statuts officiels.']],[4.2*cm,W-4.2*cm])]
s+=[Spacer(1,3),P('Pour le détail, se référer au guide déjà fourni : <b>« Guide sécurité et architecture mobile »</b>.')]

s+=[P('2. Paiements et identité',h1),P('2.1 Vérification d’identité',h2)]
s+=B(['<b>Stripe Identity</b> : pièce d’identité + égoportrait. '+L('https://docs.stripe.com/identity','docs.stripe.com/identity'),
 '<b>Biométrie :</b> ne stocker <b>aucune image</b> de notre côté — seulement le <b>statut de vérification</b> et l’<b>ID de session Stripe</b>. Configurer la <b>durée de conservation minimale</b> chez Stripe.'])
s+=[P('2.2 Place de marché et retenue des fonds',h2)]
s+=B(['<b>Stripe Connect</b> pour la place de marché; Connect gère le <b>KYC des bénéficiaires</b> (voyageurs). '+L('https://docs.stripe.com/connect/charges','Types de paiements Connect'),
 'Pour retenir l’argent jusqu’à la remise du colis : <b>« separate charges and transfers »</b> — le paiement est encaissé sur le compte de la plateforme, puis un transfert est fait au voyageur quand le serveur confirme la remise. '+L('https://docs.stripe.com/connect/separate-charges-and-transfers','Documentation'),
 'Pourquoi pas une simple pré-autorisation : une autorisation de carte en ligne <b>expire généralement après ~7 jours</b> (vérifié : Stripe indique 7 jours pour la plupart des réseaux; 5 jours pour certaines transactions Visa initiées par le marchand). '+L('https://docs.stripe.com/payments/place-a-hold-on-a-payment-method','Retenir un paiement')])
s+=[P('2.3 Versements aux voyageurs',h2)]
s+=[T([['Option','Détails'],
 ['Compte bancaire canadien','Ajouté via l’<b>onboarding hébergé Stripe</b> ou ses <b>composants intégrés</b> — <b>jamais saisi dans nos écrans</b>.'],
 ['Virement standard','Versement bancaire habituel. '+L('https://docs.stripe.com/connect/payouts-connected-accounts','Versements Connect')],
 ['Versement instantané','Vers une carte de débit admissible, <b>avec frais</b>. '+L('https://docs.stripe.com/payouts/instant-payouts','Instant Payouts')],
 ['Interac','<b>Stripe ne fait pas de versements Interac.</b> Voir 2.4.']],[4.2*cm,W-4.2*cm])]
s+=[P('2.4 Interac : à reporter',h2)]
s+=[T([['Option','Avantage','Risque'],
 ['Stripe Connect (lancement)','Stripe détient et achemine les fonds; KYC inclus.','Pas d’Interac.'],
 ['VoPay ou Zum Rails (plus tard)','Versements Interac possibles.','Faycal <b>détiendrait les fonds</b> : risque d’inscription comme <b>entreprise de services monétaires (ESM) au CANAFE</b> et de <b>permis AMF</b> au Québec, ainsi que d’<b>enregistrement à la Banque du Canada</b> (<i>Loi sur les activités associées aux paiements de détail</i>, qui vise aussi ceux qui détiennent les fonds des utilisateurs).']],[4.6*cm,5.2*cm,W-9.8*cm])]
s+=[Spacer(1,4),box('<b>Recommandation :</b> lancer avec Stripe Connect; envisager Interac plus tard, <b>seulement avec l’avis d’un avocat</b>. '
  +L('https://fintrac-canafe.canada.ca','CANAFE')+' · '+L('https://lautorite.qc.ca','AMF')+' · '+L('https://www.banqueducanada.ca/surveillance-reglementaire/paiements-detail/','Banque du Canada'),bg=LIGHT,border=TEAL)]

s+=[P('3. Responsabilité (pertes, vols, litiges)',h1)]
s+=[P('Au Québec, <b>on ne peut pas exclure entièrement sa responsabilité</b> : selon l’article <b>1474 C.c.Q.</b>, on ne peut <b>jamais</b> exclure ni limiter sa responsabilité pour le <b>préjudice corporel ou moral</b> causé à autrui; pour le <b>préjudice matériel</b>, on ne peut pas l’exclure ni la limiter en cas de <b>faute lourde ou intentionnelle</b>. De plus, la <b>Loi sur la protection du consommateur</b> limite les clauses d’exclusion. L’objectif est donc de <b>réduire</b> le risque. '
  +L('https://www.legisquebec.gouv.qc.ca/fr/document/lc/CCQ-1991','C.c.Q.')+' · '+L('https://www.legisquebec.gouv.qc.ca/fr/document/lc/P-40.1','LPC'))]
s+=[T([['Mesure','Mise en œuvre'],
 ['Rôle d’intermédiaire clair','Volis met en relation; <b>Volis ne transporte pas</b> les colis.'],
 ['Politique de litiges','Avec <b>plafond d’indemnisation</b>.'],
 ['Valeur déclarée','Valeur déclarée du colis, avec le plafond d’indemnisation affiché à côté.'],
 ['Assurance optionnelle','Via un <b>assureur partenaire</b> (vendre soi-même de l’assurance est encadré par l’AMF).'],
 ['Preuves','Photos et <b>confirmation de remise</b>.'],
 ['Contenu','Case d’<b>attestation du contenu</b> + <b>liste d’objets interdits</b>.'],
 ['Consentement','<b>Confirmation explicite avant paiement</b>.'],
 ['Douane','<b>Information à donner aux voyageurs</b> : le voyageur est légalement responsable du colis qu’il transporte. <b>Attention : cette information ne protège pas Volis</b> et ne remplace pas les autres mesures ci-dessus.']],[4.6*cm,W-4.6*cm])]

s+=[P('4. Obligations légales — Québec et Canada',h1)]
s+=[T([['Obligation','À faire','Référence'],
 ['Immatriculation','Registraire des entreprises — obtenir un <b>NEQ</b>.',L('https://www.registreentreprises.gouv.qc.ca','Registraire')],
 ['TPS/TVQ','Inscription <b>au-delà de 30 000 $</b> de revenus.',L('https://www.revenuquebec.ca','Revenu Québec')],
 ['Loi 96','Conditions d’utilisation et politique de confidentialité <b>en français</b>.','—'],
 ['LPC','Contrats conclus à distance conformes à la LPC.',L('https://www.legisquebec.gouv.qc.ca/fr/document/lc/P-40.1','LPC')],
 ['Loi 25','Désigner un <b>responsable de la protection des renseignements personnels</b>; réaliser une <b>évaluation des facteurs relatifs à la vie privée (EFVP)</b> avant le lancement, couvrant aussi le <b>transfert hors Québec vers Stripe</b> (contrat de traitement des données de Stripe).',L('https://www.cai.gouv.qc.ca','CAI')+'<br/>'+L('https://stripe.com/legal/dpa','Stripe DPA')],
 ['Biométrie','L’égoportrait est biométrique : <b>consentement exprès</b> + <b>déclaration à la Commission d’accès à l’information faite d’avance, au moins 60 jours avant la mise en service</b> si une banque de données biométriques est créée — <b>à prévoir dans le calendrier</b>.',L('https://www.cai.gouv.qc.ca','CAI')],
 ['LPRPDE (fédéral)','La <b>loi fédérale sur la vie privée</b> s’applique aux renseignements personnels qui passent d’une province ou d’un pays à l’autre.',L('https://www.priv.gc.ca/fr/sujets-lies-a-la-protection-de-la-vie-privee/lois-sur-la-protection-des-renseignements-personnels-au-canada/la-loi-sur-la-protection-des-renseignements-personnels-et-les-documents-electroniques-lprpde/','Commissariat (CPVP)')],
 ['LCAP (anti-pourriel)','<b>Consentement requis</b> avant d’envoyer des courriels promotionnels (avec identification et désabonnement).',L('https://crtc.gc.ca/fra/internet/anti.htm','CRTC')+'<br/>'+L('https://fightspam-combattrelepourriel.ised-isde.canada.ca/site/loi-canadienne-anti-pourriel/fr','Combattre le pourriel')],
 ['Plateformes numériques','<b>Déclaration annuelle</b> des revenus des utilisateurs à l’<b>ARC</b> (règles des plateformes depuis 2024) — <b>à confirmer avec un comptable</b> : il n’est pas certain que les voyageurs payés soient visés.',L('https://www.canada.ca/fr/agence-revenu.html','ARC')]],[3.4*cm,10.4*cm,W-13.8*cm])]

s+=[P('5. Lancement (App Store, Google Play, web)',h1)]
s+=[T([['Élément','Apple (iOS)','Google Play (Android)'],
 ['Compte développeur','Apple Developer : <b>99 $ US/an</b>. '+L('https://developer.apple.com/programs/','Programme'),'Play Console : <b>25 $ US</b> (une fois). '+L('https://play.google.com/console','Console')],
 ['Type de compte','Idéalement un <b>compte d’organisation</b> avec <b>numéro D-U-N-S</b>.','Idem. Compte personnel : <b>test fermé de 12 testeurs pendant 14 jours</b> avant la production. '+L('https://support.google.com/googleplay/android-developer/answer/14151465','Exigences de test')],
 ['Exigence technique','<b>Xcode 26 / SDK iOS 26</b> obligatoires depuis le <b>28 avril 2026</b> (vérifié). '+L('https://developer.apple.com/news/upcoming-requirements/','Source Apple'),'Cibler l’<b>API 36</b> (Android 16) depuis le <b>31 août 2026</b> (vérifié). '+L('https://support.google.com/googleplay/android-developer/answer/11926878','Source Google')],
 ['Fiches vie privée','<b>Étiquettes de confidentialité</b> Apple. '+L('https://developer.apple.com/app-store/app-privacy-details/','Détails'),'Section <b>Sécurité des données</b>. '+L('https://support.google.com/googleplay/android-developer/answer/10787469','Aide')],
 ['Suppression du compte','Obligatoire dans l’app. '+L('https://developer.apple.com/support/offering-account-deletion-in-your-app/','Apple'),'Obligatoire dans l’app.']],[3.3*cm,7.15*cm,7.15*cm])]
s+=[Spacer(1,3)]+B(['<b>Politique de confidentialité en ligne</b> (URL publique, en français).','<b>Stripe en mode production</b> (activation du compte, clés de production, webhooks de production).'])

s+=[P('6. International',h1)]
s+=B(['<b>Pas partout d’un coup.</b> L’expansion est limitée par les <b>pays pris en charge par Stripe Connect et Stripe Identity</b>. '+L('https://stripe.com/global','Pays Stripe'),
 '<b>Europe :</b> RGPD (avec <b>représentant</b> dans l’UE), <b>DSA</b> (règlement sur les services numériques), <b>DAC7</b> (déclaration des plateformes).',
 '<b>Pays sous sanctions : exclus.</b>',
 'Stratégie : <b>lancer au Canada</b>, puis <b>pays par pays avec un avocat local</b>.',
 'Interface prévue <b>multilingue</b> : français, anglais, arabe (<b>droite à gauche</b>), avec <b>devises locales</b>.'])

s+=[P('7. Design (équipe UI)',h1)]
s+=[KeepTogether(T([['Élément','Statut / décision'],
 ['Logo principal','Kit logo <b>« Colis caché »</b>'],
 ['Icône d’app','<b>« Signature »</b>'],
 ['Écrans existants','<b>16 écrans</b> issus des concepts <b>« Carnet de voyage »</b> et <b>« Scrapbook »</b>'],
 ['Visuels des stores','<b>À préparer</b>']],[4.2*cm,W-4.2*cm]))]
s+=[KeepTogether([P('Écrans à ajouter',h2)]+C(['Consentement à la biométrie (consentement exprès, Loi 25)','Suppression du compte','Attestation du contenu pour la douane',
 'Statuts des versements (<b>en cours → déposé</b>)','Assurance optionnelle, avec le <b>plafond affiché près de la valeur déclarée</b>','Écran de litige avec photos']))]

s+=[P('8. Prochaines étapes — checklist ordonnée',h1)]
steps=[('A. Fondations légales et administratives',['Consulter un avocat québécois (responsabilité, LPC, Loi 25, Interac/CANAFE/AMF, assurance)',
  'Immatriculer l’entreprise au Registraire des entreprises (NEQ)','Suivre les revenus; s’inscrire à la TPS/TVQ au-delà de 30 000 $',
  'Désigner le responsable de la protection des renseignements personnels','Réaliser l’EFVP (incluant le transfert hors Québec vers Stripe et le DPA Stripe)',
  'Déclarer la banque de données biométriques à la Commission d’accès à l’information <b>au moins 60 jours avant la mise en service</b> (l’inscrire au calendrier dès maintenant)','Vérifier la conformité LPRPDE (données hors province/pays) et LCAP (consentement aux courriels promotionnels)',
  'Rédiger en français : conditions d’utilisation, politique de confidentialité, politique de litiges (plafond), liste d’objets interdits',
  'Choisir un assureur partenaire pour l’assurance optionnelle','Prévoir la déclaration annuelle à l’ARC (règles des plateformes) — <b>à confirmer avec un comptable</b> (voyageurs payés visés ou non?)']),
 ('B. Technique et paiements',['Mettre en place Expo + Expo Router (iOS/Android/web) en couches MVVM / domaine / data',
  'Mettre en place le backend Node ou Supabase recevant les webhooks Stripe','Intégrer Stripe Identity (stocker seulement statut + ID de session; conservation minimale)',
  'Intégrer Stripe Connect en « separate charges and transfers »; libération décidée par le serveur seulement','Onboarding Stripe hébergé ou intégré pour le compte bancaire; versements standard et instantanés',
  'Appliquer le « Guide sécurité et architecture mobile »']),
 ('C. Design',['Finaliser logo « Colis caché » et icône « Signature »','Ajouter les 6 écrans manquants (section 7)','Préparer les visuels des stores']),
 ('D. Lancement',['Créer les comptes Apple Developer et Google Play Console (organisation + D-U-N-S idéalement)',
  'Si compte Google personnel : test fermé de 12 testeurs pendant 14 jours','Compiler avec Xcode 26 / SDK iOS 26 et cibler l’API 36',
  'Publier la politique de confidentialité; remplir les étiquettes Apple et la section Sécurité des données','Vérifier la suppression du compte dans l’app',
  'Passer Stripe en mode production','Lancer au Canada']),
 ('E. Après le lancement',['Évaluer Interac (VoPay/Zum Rails) avec avis d’avocat, y compris l’enregistrement à la Banque du Canada (Loi sur les activités associées aux paiements de détail), le CANAFE et l’AMF','Expansion pays par pays avec un avocat local (RGPD, DSA, DAC7; sanctions)'])]
for t,items in steps:
    s+=[KeepTogether([P(t,h2)]+C(items))]
s+=[P('Annexe — Liens officiels de référence',h1),P('Faits Stripe et stores, et URL de l’annexe, vérifiés le 11 octobre 2026. Revérifier avant chaque soumission.',small)]
links=[['Sujet','Lien officiel'],
 ['Expo Router',L('https://docs.expo.dev/router/introduction/')],
 ['Stripe Identity',L('https://docs.stripe.com/identity')],
 ['Stripe Connect — types de paiements',L('https://docs.stripe.com/connect/charges')],
 ['Separate charges and transfers',L('https://docs.stripe.com/connect/separate-charges-and-transfers')],
 ['Durée d’une autorisation de carte',L('https://docs.stripe.com/payments/place-a-hold-on-a-payment-method')],
 ['Versements aux comptes connectés',L('https://docs.stripe.com/connect/payouts-connected-accounts')],
 ['Versements instantanés',L('https://docs.stripe.com/payouts/instant-payouts')],
 ['Stripe — contrat de traitement (DPA)',L('https://stripe.com/legal/dpa')],
 ['Disponibilité de Stripe par pays',L('https://stripe.com/global')],
 ['Apple Developer Program (99 $ US/an)',L('https://developer.apple.com/programs/')],
 ['Exigences Apple à venir / SDK minimum',L('https://developer.apple.com/news/upcoming-requirements/')],
 ['Étiquettes de confidentialité Apple',L('https://developer.apple.com/app-store/app-privacy-details/')],
 ['Suppression du compte (Apple)',L('https://developer.apple.com/support/offering-account-deletion-in-your-app/')],
 ['Google Play — niveau d’API cible',L('https://support.google.com/googleplay/android-developer/answer/11926878')],
 ['Google Play — tests (compte personnel)',L('https://support.google.com/googleplay/android-developer/answer/14151465')],
 ['Google Play — Sécurité des données',L('https://support.google.com/googleplay/android-developer/answer/10787469')],
 ['Registraire des entreprises du Québec',L('https://www.registreentreprises.gouv.qc.ca')],
 ['Revenu Québec (TPS/TVQ)',L('https://www.revenuquebec.ca')],
 ['CAI (Loi 25, biométrie)',L('https://www.cai.gouv.qc.ca')],
 ['Code civil du Québec (art. 1474)',L('https://www.legisquebec.gouv.qc.ca/fr/document/lc/CCQ-1991')],
 ['Loi sur la protection du consommateur',L('https://www.legisquebec.gouv.qc.ca/fr/document/lc/P-40.1')],
 ['CANAFE (services monétaires)',L('https://fintrac-canafe.canada.ca')],
 ['Autorité des marchés financiers (AMF)',L('https://lautorite.qc.ca')],
 ['LPRPDE — Commissariat à la vie privée',L('https://www.priv.gc.ca/fr/sujets-lies-a-la-protection-de-la-vie-privee/lois-sur-la-protection-des-renseignements-personnels-au-canada/la-loi-sur-la-protection-des-renseignements-personnels-et-les-documents-electroniques-lprpde/','https://www.priv.gc.ca/fr/sujets-lies-a-la-protection-de-la-vie-privee/…/lprpde/')],
 ['LCAP — CRTC',L('https://crtc.gc.ca/fra/internet/anti.htm')],
 ['LCAP — Combattre le pourriel',L('https://fightspam-combattrelepourriel.ised-isde.canada.ca/site/loi-canadienne-anti-pourriel/fr')],
 ['Banque du Canada — LAAPD',L('https://www.banqueducanada.ca/surveillance-reglementaire/paiements-detail/')],
 ['Agence du revenu du Canada',L('https://www.canada.ca/fr/agence-revenu.html')]]
annex=ParagraphStyle('ax',parent=cell,fontSize=7,leading=8.8)
at=T(links,[5.6*cm,W-5.6*cm],cs=annex); at.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),1.6),('BOTTOMPADDING',(0,0),(-1,-1),1.6)])); s+=[at]
s+=[Spacer(1,6),box('<b>Rappel :</b> ce document n’est pas un avis juridique. Faire valider l’ensemble par un avocat québécois avant le lancement. '
  'Les exigences des stores et de Stripe changent régulièrement : revérifier les liens officiels au moment de soumettre.')]
doc.build(s)
