#program to create an divide exception and store output in file
def div(divident,qoutient):
    
    try:
        remainder=qoutient/divident
        print (remainder)
    except ZeroDivisionError:
        file1=open('errorreport.txt','a')
        file1.write("exception case 1 :divident must not be zero "+'\n')
        file1.close()
    except TypeError:
        file1=open('errorreport.txt','a')
        file1.write("exception case 2 :enterd credientials are wrong"+'\n')
        file1.close()   
    else:
        print("")
    
div(0,6)
div('t',7)