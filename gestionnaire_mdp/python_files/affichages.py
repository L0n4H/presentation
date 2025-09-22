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
        try:
            reponse_int = int(reponse)
            print(reponse_int)
            if reponse_int == 1:
                print(" je suis arrivé ici")
                choix = "Vous avez choisi de vous connecter"
                print(choix)
                connexion()
                correct = True
            elif reponse_int == 2:
                choix = "Vous avez choisi de vous inscrire"
                print(choix)
                inscription()
                correct = True
            elif reponse_int == 3:
                choix = "Vous quittez l'application"
                quitter()
                return None
        
        except:
            print("Veuillez entrer une réponse valide")


def connexion():
    # print("En cours ...")
    print("Vous êtes sur la page de connexion")
    id_co = input("Veuillez entrer votre identifiant (q pour quitter): ")
    if id_co == 'q':
        quitter()
        return None

    mdp_co = input("Veuillez entrer votre mot de passe : ")
    print("identifiant : ", id_co, " | mot de passe : ", mdp_co)
    # maintenant faut aller dans la bd
    
def inscription():
    # print("En cours ...")
    print("Vous êtes sur la page d'inscription (q pour quitter): ")
    fini = False
    while not fini :
        id_ins = input("Veuillez entrer un identifiant : ")
        if id_ins == 'q':
            quitter()
            return None
        mdp_ins = input("Veuillez entrer votre mot de passe : ")
        
        print("D'accord ! Votre identifiant est ", id_ins, " | et votre mot de passe est : ", mdp_ins)
        rep = input("Confirmez vous ces informations ? (O oui, N non) :")
        print("la reponse : ", rep)
        if rep == 'o' or rep == 'O':
            # on rentre dans la bd les infos
            print("Enregistrement des informations ...")
            fini = True
        elif rep == 'n' or rep == 'N':
            # on reprend les infos
            print("D'accord")

    

def quitter():
    print("Au revoir !")
    # res = "Au revoir !"
    # return res


