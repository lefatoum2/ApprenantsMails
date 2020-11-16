import mysql.connector as mysqlpyth
import random
from datetime import datetime

db = mysqlpyth.connect(
    host="localhost",
    user="root",
    passwd="root",
    port=3306,
    db="binomotron"
)

print("Connexion réussie !")
sql = "insert into employee2(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) values(%s,%s,%s,%s,%s)"
cursor = db.cursor()
age = 23
nom = 'Marc'
prenom = 'Jean'
income = 56000.0
sex = 'M'
ds = (nom, prenom, age, sex, income)
yh = cursor.execute(sql, ds)
print("Réussie 2")
db.commit()
cursor.close()
db.close()
