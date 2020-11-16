


class apprenant:
    def __init__(self, nom, prenom, id_apprenant):
        self.nom = nom
        self.prenom = prenom
        self.id_apprenant = id_apprenant

    def trait2(self):
        lst1 = []
        lst2 = []
        lst3 = []
        for id1 in self.cur:
            lst1.append(id1)

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
        return dict1

