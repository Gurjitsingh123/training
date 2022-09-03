from students import student

def main():
    while True:
        print("\n******welcome******\n")
        print("please enter number equivalent to function\n1:all students\n2:add new student\n3:edit student data\n4:search student\n5:delete a student\n6:exit")
        try:
            x=int(input())
            if x==1:
                student.all_students()
            elif x==2:
                student.add_student()
            elif x==3:
                student.update_student()
            elif x==4:
                student.search_student()
            elif x==5:
                student.del_student()
            elif x==6:
                break
            else:
                print("you have enterd a wrong choice--try again--")
        except:
            print("enterd a  wrong details--try again--")

        


main()    