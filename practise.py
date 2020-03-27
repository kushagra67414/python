def g(num):
    a = int(input("guess a num"))
    if(a==num) :
        print("success")
    else:
        g(num)
g(10)