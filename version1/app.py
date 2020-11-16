import os


def open1(file2):
    f1 = open(file2, "r")
    content1 = f1.read()
    list1 = content1.splitlines()
    f1.close()


list5 = []


def repl2(list1):
    for list3 in list1:
        list6 = list3.replace(".", '')
        list6 = list6.replace("-", '')
        list6 = list6.split("@")[0]
        list5.append(list6)
    return (list5)


list29 = {}
# def comp1(list15,list47):
#    for list in list15:
#        if list in list47:


f = open("../version/apprenantmail.txt", "r")
content = f.read()
list1 = content.splitlines()
f.close()

f2 = open("../apprenant.txt", "r")
content2 = f2.read()
list2 = content2.splitlines()
f2.close()

print(list1)
print(list2)

list5 = []
for list3 in list1:
    list6 = list3.replace(".", '')
    list6 = list6.replace("-", '')
    list6 = list6.split("@")[0]
    list5.append(list6)
print(list5)

# -un fichier python avec une classe pour connecter à MySQL
# -un pour extraire et traiter les emails du document texte
# -un pour les envoyer dans la base MySQL
# -et un fichier python sans sa propre classe, mais qui utilise les trois autres pour coordonner la tâche


list10 = []
for list3 in list2:
    list6 = list3.lower()
    list6 = list6.replace(" ", '')
    list6 = list6.replace("-", '')
    list10.append(list6)
print(list10)

s = 'xjhgjg876-896@domain.com'
s = s.split("@")[0]
s = s.replace("-", '')
s = s.replace(".", '')
print(s)

dict23 = {}
for i in list5:
    for j in list10:
        if i == j:
            dict23[i] = j
print(dict23)
