n = int(input())
l = []
for i in range(n):
    for j in range(1):
        temp = [int(g) for g in input().split()]
        l.append(temp)
# uploaded by ultimate gamer
for i in range(n):
    for j in range(n):
        if i < j:
                print(0, end=" ")
        else:

                print(l[i][j], end=" ")


    if i != n :
        print()