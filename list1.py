li=[3, 4, 8, 11,18, 22, 23]
for i in li:
    for j in li:
        if i+j==26:
            for k,x in enumerate(li):
                if x == i:
                    print("at location ",k)
            for l,x in enumerate(li):
                if x == j:
                    print("and ",l)
            print("****")
        else:
            pass
