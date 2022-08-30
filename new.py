from sqlite3 import connect
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="",database="training")
mycursor=mydb.cursor()
mycursor.execute("select * from products")
for i in mycursor:
    print(i)
