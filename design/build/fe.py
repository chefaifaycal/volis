import screens as S
def mk(fn):
    return lambda: fn(False).replace('31,01', '32,06')
FE = [('07-accueil', mk(S.accueil)), ('08-resultats-recherche', mk(S.resultats)), ('09-profil-voyageur', mk(S.profil_voyageur)), ('12-suivi-colis', mk(S.suivi)),
      ('13-remise', mk(S.remise)), ('14-messages', mk(S.messages)), ('15-publier-voyage', mk(S.publier)), ('16-profil-portefeuille', mk(S.profil))]
