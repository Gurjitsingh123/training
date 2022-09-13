import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="training")
mycursor=mydb.cursor() 
def all_students():
        
    try:
        mycursor.execute("select * from student")
        print("all students present in table\n")
        for i in mycursor:
            print(i,"\n")  
    except:
        print("error in program kindley report")
def add_student():
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
        print("data inserted sucessfully")
    except:
        mydb.rollback()
        print("\ndata cant be inserted")
def del_student():
    try:
        s1=input("enter student name  that you want to delete there data:")
        stmt1=("DELETE FROM student WHERE name='{}'").format(s1)
        mycursor.execute(stmt1)
        mydb.commit()
        print("data deleted sucessfully")
        print(mycursor.rowcount,"record's delete")      
    except:
        mydb.rollback()
        print("rollback query is exceuted")
        print("no student exist with that name")
def update_student():
    try:
        name=str(input("enter a name you want to update data:"))
        new_class=str(input("enter a new class:"))
        new_age=int(input("enter new age:"))
        new_height=str(input("enter new height: "))
        stmt=("UPDATE  student SET class='{}',age={},height='{}' WHERE name='{}'").format(new_class,new_age,new_height,name)
        mycursor.execute(stmt)
        mydb.commit()
        print("data updated sucessfully")
        print(mycursor.rowcount,"rows affected")
    except:
        mydb.rollback()
        print("data did not updated")
def search_student():
    try:
        search_by=input("enter a column you want to search by table:")
        search_for=input("enter a value of that column you want to search for:")
        stmt=("select * from student where {}='{}'").format(search_by,search_for)
        mycursor.execute(stmt)
        result=mycursor.fetchall()
        print(result)
    except:
        print("there is not having any column of that name ") 
def main():
    while True:
        print("\n******welcome******\n")
        print("please enter number equivalent to function\n1:all students\n2:add new student\n3:edit student data\n4:search student\n5:delete a student\n6:exit")
        try:
            x=int(input())
            if x==1:
                all_students()
            elif x==2:
                add_student()
            elif x==3:
                update_student()
            elif x==4:
                search_student()
            elif x==5:
                del_student()
            elif x==6:
                break
            else:
                print("you have enterd a wrong choice--try again--")
        except:
            print("enterd a  wrong details--try again--")
main()    
mydb.close()