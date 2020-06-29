n= int(input())
i=0
lines = []
while i<n:
    l = input()
    if l:
        lines.append(l.upper())
        i = i+1
    else:
        break;

for z in lines:
    print(z)