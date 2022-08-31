#program to create an divide exception and store output in file
def div(divident,qoutient):
    file1=open('errorreport.txt','a')
    try:
        remainder=qoutient/divident
        print (remainder)
    except ZeroDivisionError:
        file1.write("exception case 1 :divident must not be zero "+'\n')
    except TypeError:
        file1.write("exception case 2 :enterd credientials are wrong"+'\n')
    else:
        print("")
    file1.close()
div(0,6)
div('t',7)