from re import L
from sqlite3 import connect
import mysql.connector
import pandas as pd
li=[]
li1=[]
li2=[]
li3=[]
li4=[]
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="training")
mycursor=mydb.cursor()
mycursor.execute("select uXS,uS,uM,uL,uXL,uXXL from products")
for i in mycursor:
    li.append(i)  
mycursor1=mydb.cursor()
mycursor1.execute("select XS,S,M,L,XL,XXL from products")
for j in mycursor1:
    li1.append(j)
li3=(list(map(lambda x:str(x),str(li).replace('[','').replace(']','').replace(')','').replace('(','').replace('}','').replace('{','').split(','))))
li4=(list(map(lambda x:str(x),str(li1).replace('[','').replace(']','').replace(')','').replace('(','').replace('}','').replace('{','').split(','))))
for k in range(len(li3)):
    dict={li3[k]:[li4[k]]}
    print(dict)
data=pd.DataFrame(dict)
print(data)