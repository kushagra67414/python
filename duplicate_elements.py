def removeDuplicate( li ):
    newli=[]

    for item in li:
        if item not in newli:
            newli.append(item)

    return newli

li=[]
li= list(map(int, input ().split ()))
x = removeDuplicate(li)

for i in x:
    print(i,end=" ")