""" 
Ici, on gère tous les affichages de l'application
On gère aussi les interactions avec l'utilisateur
C'est la partie "front-end"
"""


def dem_app():
    """
    Ceci est la fonction qui sert à lancer l'application"""
    print("\n-----Bonjour et bienvenue ! ----- ")
    print('----------------------------------')
    print('Que voulez vous faire ? ')
    print("1/ Je souhaite me connecter à l'application")
    print("2/ Je souhaite m'inscrire sur l'application")
    print("3/ Quitter\n")
    correct = False;
    while not correct :
        reponse = input("Choisissez 1/ ou 2/ ou 3/ .\nVotre réponse : ")
        choix = ""
        if not (reponse != int):
            if int(reponse) == 1:
                choix = "Vous avez choisi de vous connecter"
                correct = True
                print(choix)
                connexion()
            elif int(reponse) == 2:
                choix = "Vous avez choisi de vous inscrire"
                correct = True
                print(choix)
                inscription()
            elif int(reponse) == 3:
                choix = "Vous quittez l'application"
                quitter()
                return None
            else:
                print("veuillez choisir une option valide")


def connexion():
    print("En cours ...")

def inscription():
    print("En cours ...")

def quitter():
    print("Au revoir !")


