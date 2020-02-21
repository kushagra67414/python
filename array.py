from array import *
arr = array('i', [])
n = int(input("enter range"))
for i in range(n):
    x = int(input("enter next value"))
    arr.append(x)

print(arr)

val = int(input("enter search value"))

print(arr.index(val))