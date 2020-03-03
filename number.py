for i in range(1001):
    f=0
    for j in range (2,i):
        if(j*j)==0:
            f=1
            break
        if(f==0):
            print(i)