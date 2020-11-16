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

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.__disconnect__()


class Db2:
    def __init__(self, user, password, host1, data1):
        self.user = user
        self.password = password
        self.host1 = host1
        self.data1 = data1

    def curs12(self, query1):
        bdd = mysqlpyth.connect(user='user',
                                password='root',
                                host='localhost',
                                port="3306",
                                database='binomotron2')
