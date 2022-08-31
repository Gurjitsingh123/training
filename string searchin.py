#Find if the characters of the sample string is in the same order in the text string
text2='HKLjKKoNO'
text_string = 'abcJjhAghOjhfhIljHNkhgDbhjNEvfhR'
sample = 'JOHN'
def searching(list1,list2):
    list3=[]
    list1=list1.upper()
    list2=list2.upper()
    for j in list2:
        for i in list1:
            if j==i :
                list3.append(j)
    print(list3)
searching(text_string,sample)
searching(text2,sample)