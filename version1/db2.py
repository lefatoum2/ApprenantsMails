import pymysql
import mysql.connector as mysqlpyth

groupe = []


class Monty:
    def __init__(self, nom, prenom, id):
        self.id = id
        self.nom = nom
        self.prenom = prenom


class DB:

    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.password = "root"
        self.db = "breizhibus"
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
                                   cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def disconnect(self):
        self.con.close()
        self.cur.close()

    def send1(self, sql):
        self.cur.execute(sql)

    def get1(self, sql):
        tu2 = ()
        # cursor = self.cursor()
        # cursor.execute(sql)
        cura = self.cur
        cur1 = cura.execute(sql)
        print(cura)
        for i, a, n in cura:
            nouveau = Monty(i, a, n)
            groupe.append(nouveau)
        return cur1
