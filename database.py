from django.shortcuts import render
import requests
import mysql.connector
name=requests.GET.get('fname')
last=requests.GET.get('lname')
print(name,last)
connection=mysql.connector.connect(host="localhost",user="root",password="",database="training")
mycursor=connection.cursor()
stmt="INSERT INTO `formdata`(`id`, `email`, `password`) VALUES ('','{}','{}')".format(name,last)
print(stmt)
try:
    mycursor.execute("CREATE TABLE IF NOT EXISTS formdata (id INT NOT NULL AUTO_INCREMENT , email VARCHAR(200) , password VARCHAR(200), PRIMARY KEY(id));")
    mycursor.execute(stmt)
    connection.commit()
    print("done")
except:
    print("none")    
connection.close()