import os


class Filio():
    def __init__(self,nom_chemin):
        self.nom_chemin = nom_chemin

    def read_file(self):
        nom_chemin1 = open("nom_chemin", "r")
        content = nom_chemin1.read()
        list1 = content.splitlines()
        return list


    def __exit__(self, read_file):
    nom_chemin1.close()


class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()