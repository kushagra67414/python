T = int(input())

for i in range(T):
    line = input()
    ones = zeros = 0
    for c in line:
        if int(c) == 1:
            ones += 1
        elif int(c) == 0:
            zeros += 1
        else:
            raise ValueError
        if ones > 1 and zeros > 1:
            print("NO")
            break

    if ones == 1:
        print("YES")
    elif zeros == 1:
        print("YES")