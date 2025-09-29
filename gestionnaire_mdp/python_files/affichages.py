""" 
Ici, on gère tous les affichages de l'application
On gère aussi les interactions avec l'utilisateur
C'est la partie "front-end"
"""

SEPARATEUR   = "\n----------------------------------"

def start()-> int:
    """
    Ceci est la fonction qui sert à lancer l'application"""
    print("\n-----Bonjour et bienvenue ! ----- ")
    print(SEPARATEUR)
    print('Que voulez vous faire ? ')
    print("1/ Je souhaite me connecter à l'application")
    print("2/ Je souhaite m'inscrire sur l'application")
    print("3/ Quitter\n")
    correct = False;
    while not correct :
        reponse = input("Choisissez 1/ ou 2/ ou 3/ .\nVotre réponse : ")
        try:
            reponse_int = int(reponse)
            return reponse_int        
        except:
            print("Veuillez entrer une réponse valide")


def connexion()-> list:
    print("Vous êtes sur la page de connexion")
    id_co = input("Veuillez entrer votre identifiant (q pour quitter): ")
    if id_co == 'q':
        quitter()
        return None

    mdp_co = input("Veuillez entrer votre mot de passe : ")
    informations = [id_co, mdp_co]
    return informations
    
def inscription()-> list:
    print("Vous êtes sur la page d'inscription (q pour quitter): ")
    fini = False
    informations = []
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
            informations = [id_ins, mdp_ins]
            fini = True
        elif rep == 'n' or rep == 'N':
            # on reprend les infos
            print("D'accord")
    
    return informations


def menu()-> int:
    fini = False
    rep = 0
    while not fini:
        print("Que voulez vous faire ?")
        print("1/ Afficher mes comptes")
        print("2/ Créer un nouveau mot de passe")
        print("3/ Quitter (q)")
        res = input("Votre choix : ")
        try:
            rep = int(res)
            if rep < 3:
                fini = True
            else:
                print("\n")
                print(SEPARATEUR)
                print("Veuillez entrer un choix valide")
        except:
            if res == 'q':
                fini = True            
            else:
                print("\n")
                print(SEPARATEUR)
                print("Veuillez entrer un choix valide")
    return rep
    

def liste_comptes(lst:list)-> None:
    indice = 1
    for cpt in lst:
        #print(cpt[-1], '|',cpt[1],'|',cpt[2], '|')
        site, id, mdp = cpt 
        espace = 25 - len(site)
        print(SEPARATEUR )
        indice_str = str(indice)
        print(indice_str,'/ |',site,espace*' ', '|')
        print("\n")
        indice +=1
    return None

def choix_compte(lst:list)-> None:
    err = "veuillez entrer une réponse valide"
    try:
        print("Choisissez un compte : ")
        res = int(input("Réponse :"))
        res -=1
        if res > len(lst):
            print(err)
        else: 
            compte = lst[res]
            site, id, mdp = compte
            print("Le mot de passe pour votre compte ", site, " est : ", mdp)

    except:
        print(err)

def quitter()-> bool:
    print("Au revoir !")
    return True
    # res = "Au revoir !"
    # return res


