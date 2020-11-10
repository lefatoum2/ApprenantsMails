import mysql.connector as mysqlpyth


class Monty:

    def __init__(self, nom, prenom, id):
        self.id = id
        self.nom = nom
        self.prenom = prenom


# lire data
def lire_data():
    groupe = []

    # Python se connecte sur la bdd
    bdd = mysqlpyth.connect(user='root',
                            password='root',
                            host='localhost',
                            port="3306",
                            database='binomotron2')

    # récupère le curseur sur la base pour travailler avec
    cursor = bdd.cursor()

    # chaine de cractères de la requête à exécuter
    query = "SELECT * FROM apprenant;"
    # exécute la requête grâce au curseur
    cursor.execute(query)

    # récupère les données retournées par le select
    for id, nom, prenom in cursor:
        nouveau = Monty(nom, prenom, id)
        groupe.append(nouveau)

    # chaine de cractères de la requête à exécuter
    query = "ALTER TABLE apprenant ADD COLUMN mail VARCHAR(100);"
    # exécute la requête grâce au curseur
    cursor.execute(query)

    # tout fermer c'est plus propre
    cursor.close()
    bdd.close()
    return groupe


# fonction principale de mon code
def main():
    tous = lire_data()

    for monty in tous:
        print(monty.nom, monty.prenom)


main()
