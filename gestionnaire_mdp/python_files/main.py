"""
Bienvenu sur ce projet python qui est en cours de construction.
Le but de ce projet est de développer un gestionnaire de mot de
passe sécurisé en ligne de commande
"""

# 1/ interface 
# 2/ BDD
# 3/ Systeme de chiffrage

import affichages as aff
import connexionBD as co

SEPARATEUR   = "\n----------------------------------"


def main():
    rep = aff.start()
    informations = list
    connexion = None
    co_en_cours = True
    while co_en_cours:
        correct = False;
        while not correct :
            choix = ""
            print(rep)
            if rep == 1:
                print(SEPARATEUR)
                choix = "Vous avez choisi de vous connecter"
                print(choix)
                informations = aff.connexion()
                connexion = True
                correct = True
            elif rep == 2:
                choix = "Vous avez choisi de vous inscrire"
                print(choix)
                informations = aff.inscription()
                connexion = False
                correct = True
            elif rep == 3:
                choix = "Vous quittez l'application"
                aff.quitter()
                return None
            
        # si l'utilisateur se connecte
        if connexion:
            res = co.se_connecter(informations)
            if res:
                print("La connexion a fonctionné")
                co_en_cours = False
            else:
                print("La connexion a échoué")

        # si l'utilisateur s'inscrit
        else:
            res = co.s_inscrire(informations)
            if res:
                print("L'inscription a fonctionné")
                co_en_cours = False
            else:
                print("L'inscription a échoué")

    # ici, l'application est sur sa page d'acceuil
    quitter = False
    while not quitter:

        print(SEPARATEUR)
        print("Bienvenu : " + informations[0])
        reponse = aff.menu()
        print(SEPARATEUR)
        print("la reponse est :", reponse)
        if reponse == 0 or reponse == 3:
            quitter = aff.quitter()
        elif reponse==1:
            print("Voici vos comptes enregistrés ")
            les_comptes = co.comptes(informations[0])
            aff.liste_comptes(les_comptes)
            aff.choix_compte(les_comptes)
        elif reponse==2:
            print("In progress ...")
    
    co.fermer()

main()
