from sqlite3 import Cursor
from types import NoneType
import mysql.connector
#def student(x):

 #   switcher={
  #      1:print("all students"),
   #     2:print("add student"),
    #    3:print("edit students data"),
     #  4:print("search students"),
      #  5:print("del student "),
       # 6:print("exit"),   }
def all_students():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="training")
    mycursor=mydb.cursor()
    mycursor.execute("select name from student")
    print("all students present in table")
    for i in mycursor:
        print(i)  
    mydb.close()
def add_student():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="training")
    mycursor=mydb.cursor()
    try:
        n=input("enter name:")
        c=input("enter class:")
        a=input("enter age:")
        h=input("enter height:")
        stmt=("INSERT INTO student (name,class,age,height)values(%s,%s,%s,%s)")
        data=(n,c,a,h)
        mycursor.execute(stmt,data)
        mydb.commit()
        print(mycursor.rowcount,'rowsaffected')
    except:
        mydb.rollback()
    print("data inserted")
    mydb.close()
def del_student():
        mydb = mysql.connector.connect(host="localhost",user="root",password="",database="training")
        mycursor=mydb.cursor()
        try:
                s1=input("enter student name  that you want to delete there data:")
                data1=s1
                print(data1)
                stmt1=("DELETE FROM student WHERE name='{}'").format(data1)
                mycursor.execute(stmt1)
                mydb.commit()
                print("data deleted sucessfully")
                print(mycursor.rowcount,"record's delete")      
        except:
            mydb.rollback()
            print("rollback query is exceuted")
            print("no student exist with that name")
            mydb.close()
def update_student():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="training")
    mycursor=mydb.cursor()
    try:
        name=str(input("enter a name you want to update data"))
        new_class=str(input("enter a new class"))
        new_age=int(input("enter new class"))
        new_height=str(input("enter new height"))
        stmt=("UPDATE  student SET class='{}',age={},height='{}' WHERE name='{}'").format(new_class,new_age,new_height,name)
        print(stmt)
        mycursor.execute(stmt)
        mydb.commit()
        print("data updated sucessfully")
        print(mycursor.rowcount,"rows affected")
    except:
        mydb.rollback()
        print("data did not updated")
        mydb.close()
def search_student():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="training")
    mycursor=mydb.cursor()
    try:
        search_by=input("enter a column you want to search by table")
        search_for=input("enter a value of that column you want to search for")
        stmt=("select * from student where {}='{}'").format(search_by,search_for)
        mycursor.execute(stmt)
        result=mycursor.fetchall()
        print(result)
    except:
        print("data did not present here")
    
#all_students()
#add_student()
#del_student()
#all_students()
#update_student()
search_student()
#x=input("please enter number equivalent to function\n1:all students\n2:add new student\n3:edit student data\n4:search student\n5:delete a student\n6:exit")
