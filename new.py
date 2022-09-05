from re import L
from sqlite3 import connect
import mysql.connector
li=[]
li1=[]
li2=[]
li3=[]
li4=[]
li5=[]
li6=[]
li7=[]
li8=[]
dict={}
dict2={}
s=int()
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="training")
mycursor=mydb.cursor()
mycursor.execute("select uXS,uS,uM,uL,uXL,uXXL from products")
for i in mycursor:
    li.append(i)  
mycursor1=mydb.cursor()
mycursor1.execute("select XS,S,M,L,XL,XXL from products")
for j in mycursor1:
    li1.append(j)
li3=(list(map(lambda x:float(x),str(li).replace('[','').replace(']','').replace(')','').replace('(','').replace('}','').replace('{','').split(','))))
li4=(list(map(lambda x:float(x),str(li1).replace('[','').replace(']','').replace(')','').replace('(','').replace('}','').replace('{','').split(','))))
for i in li3:
  li5.append(int(i))
for j in li4:
  li6.append(int(j))
try:
   mycursor.execute("CREATE TABLE IF NOT EXISTS products_analysis (products_size INT, products_sold INT );")
   print("table created")
   print(li5,li6)
   mydb.commit()
   for k in range(len(li5)):
      mycursor.execute("INSERT INTO `products_analysis`(`products_size`, `products_sold`) VALUES ('{}','{}')".format(li5[k],li6[k]))
      mydb.commit()
   print("sucessfull")

except:
   print("nops")
mydb.close()