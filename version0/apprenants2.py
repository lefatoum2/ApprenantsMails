import mysql.connector as mysqlpyth
import os

lst1 = []
lst2 = []
lst3 = []

bdd = mysqlpyth.connect(user='root',
                        password='root',
                        host='localhost',
                        port="3306",
                        database='binomotron2')

# récupère le curseur sur la base pour travailler avec
cursor = bdd.cursor()
# chaine de caractères de la requête à exécuter
query = "SELECT * FROM apprenant;"
# exécute la requête grâce au curseur
cursor.execute(query)

# (données de la réquête) Liste de tuple d'apprenants avec leur identifiant, nom et prénom
for ih in cursor:
    lst1.append(ih)

# Mettre le prénom+nom dans une liste
for a, (b, c, d) in enumerate(lst1):
    lst2.append(d + c)

# concaténation de la liste de prénom+nom
for a in lst2:
    a = a.lower()
    a = a.replace(" ", '')
    a = a.replace("-", '')
    a = a.replace("é", 'e')
    a = a.replace("è", 'e')
    lst3.append(a)

# Formation d'un dictionnaire(données/nom+prenom concaténés)(lst1,lst3)

zip1 = zip(lst1, lst3)
dict1 = dict(zip1)
print(dict1)
# chaine de caractères de la requête à exécuter ( création de la colomne mail dans apprenant)
# query = "ALTER TABLE apprenant ADD COLUMN mail VARCHAR(100);"
# exécute la requête grâce au curseur
# cursor.execute(query)
