def vow(l):
    return ((l == 'a') or (l == 'e') or (l == 'i') or (l == 'o') or (l == 'u'))


def final(ip):

    for i in range(0, len(ip)):
        if ((vow(ip[i - 1]) != True) or
                (vow(ip[i]) != True)):
            print(ip[i], end="")


ip = input()
final(ip)