import os


class File1:
    def __init__(self, nom_chemin):
        self.nom_chemin = nom_chemin

    def read_file(self):
        nom_chemin2 = open(self.nom_chemin, "r")
        content = nom_chemin2.read()
        list1 = content.splitlines()
        nom_chemin2.close()
        return list
