import sqlite3


connection = sqlite3.connect("/home/nolhan/Documents/Perso/projet_perso/python/presentation/gestionnaire_mdp/BDD/main.db")
cursor = connection.cursor()


def test():
    cursor.execute("SELECT 1;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def se_connecter(les_infos) -> bool:
    id_co = les_infos[0]
    mdp_co = les_infos[1]
    
    try:
        req = "SELECT master_password FROM users WHERE username = ?"
        cursor.execute(req, (id_co,))
        rows = cursor.fetchall()
        
        if len(rows) == 0:
            print("Utilisateur non trouvé")
            return False
        
        master_password_bdd = rows[0][0]  
        
        if master_password_bdd == mdp_co:
            print("Connexion réussie !")
            return True
        else:
            print("Mot de passe incorrect")
            return False
            
    except :
        print(f"Erreur lors de la connexion")
        return False

def s_inscrire(les_infos):
    id_co = les_infos[0]
    mdp_co = les_infos[1]
    # En cours de création ...
    return False



def fermer():
    connection.close()