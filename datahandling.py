import mysql.connector
li,li1,li2,li3,li4,li5,li6,li7=[],[],[],[],[],[],[],[]
dict,dict1={},{}
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="training")
mycursor=mydb.cursor()
mycursor.execute("select uXS,uS,uM,uL,uXL,uXXL from products")
for i in mycursor:
    li.append(i)  
mycursor1=mydb.cursor()
mycursor1.execute("select XS,S,M,L,XL,XXL from products")
for j in mycursor1:
    li1.append(j)
for y in li:
   for z in y:
      li3.append(int(z))
for y1 in li1:
   for z1 in y1:
      li4.append(int(z1))
for key,value in zip(li3,li4):
    if key not in dict:
        dict[key]=[value]
    else:
        dict[key].append(value)
for q in list(dict.values()):
    li6.append(sum(q))
for ke,va in zip(list(dict.keys()),li6):
    dict1[ke]=[va]
print(sorted(dict1.items()))