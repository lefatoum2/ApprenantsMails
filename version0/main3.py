from version0.apprenants2 import *
from version0.mails import *
# On importe les scripts entiers mails et apprenants2

# On replace les valeurs du dictionnaires qui étaient des noms concaténés par les mails correspondants
for g, b in dict1.items():
    for h, k in dict3.items():
        if k == b:
            dict1[g] = h
    else:
        None

# On envoie à la base de donnée les mails correspondants via dict1 en utilisant ID_APPRENANT
for (g, c, j), b in dict1.items():
    query1 = "update apprenant set mail = %s where ID_APPRENANT = %s"
    value1 = (b, g)
    cursor.execute(query1, value1)
    bdd.commit()

cursor.close()
bdd.close()
