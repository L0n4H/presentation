import sqlite3


connection = sqlite3.connect("/home/nolhan/Documents/Perso/projet_perso/python/presentation/gestionnaire_mdp/BDD/main.db")
cursor = connection.cursor()


def test():
    cursor.execute("SELECT 1;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)