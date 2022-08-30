from sqlite3 import connect
import mysql.connector
import pandas as pd
li=[]
li1=[]
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="training")
mycursor=mydb.cursor()
mycursor.execute("select uXS,uS,uM,uL,uXL,uXXL from products")
for i in mycursor:
   li.append(i)
mycursor1=mydb.cursor()
mycursor1.execute("select XS,S,M,L,XL,XXL from products")
for j in mycursor1:
    li1.append(j)
dict={
    'size':li,
    'qty':li1
}
data=pd.DataFrame(dict)
print(data)