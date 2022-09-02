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
for k in li3:
    k=int(k)
    li5.append(k)
for l in li4:
    l=int(l)
    li6.append(l)  
for p in range(len(li5)):
    if p >= 0 : 
        if li5[p]==li5[p-1]:
            s=li6[p]+li6[p-1]   
        else:
            li7.append(li5[p])
            li8.append(s)                            
for m,n in zip(li7,li8):
    dict[m]=n
print(dict)
