import mysql.connector as mysqlpyth

groupe = []
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

for id1 in cursor:
    groupe.append(id1)

for i, (a, b, c) in enumerate(groupe):
    print(c, b)


dict1 = {}

