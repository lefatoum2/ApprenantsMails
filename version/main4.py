# from app import *
from version.database import *
from version.openfilemail import *

if __name__ == "__main__":
    db1 = DB()
    sql1 = "select * from employee2"
    print(db1.get1(sql1))

    #doc = 'apprenantmail.txt'
    #open1 = Openone(doc)
    #print(open1.trait1())
