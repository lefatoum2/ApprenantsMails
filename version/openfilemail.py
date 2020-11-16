import os


class Openone:
    def __init__(self, nom_chemin):
        self.nom_chemin = nom_chemin

    def trait1(self):
        # On ouvre le document texte avec open puis on met ligne par ligne les mails dans une liste
        nom_chemin2 = open(self.nom_chemin, "r")
        content = nom_chemin2.read()
        list1 = content.splitlines()
        nom_chemin2.close()

        # concaténation du nom + prenom dans une liste(list5)
        list5 = []
        for list3 in list1:
            list3 = list3.replace(".", '')
            list3 = list3.replace("-", '')
            list3 = list3.replace("é", 'e')
            list3 = list3.replace("è", 'e')
            list3 = list3.split("@")[0]
            list5.append(list3)

        # On prend les deux listes list1 et list5 pour les mettre dans un dictionnaire
        zip2 = zip(list1, list5)
        dict3 = dict(zip2)
        return dict3
