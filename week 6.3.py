def printDict():
    n = int(input())
    dicta= {}
    for i in range (1, n+1):
        dicta[i] = i * i
    print(dicta)
printDict()