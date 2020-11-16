import pymysql
import mysql.connector as mysqlpyth


class DB:

    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.password = "root"
        self.db = "binomotron"
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
        donnee1 = []
        recu = self.cur.execute(sql)
        #for jk, kl in enumerate(self.cur):
        #    donnee1.append(kl)
        #return donnee1
        return recu
