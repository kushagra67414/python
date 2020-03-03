import random
door = [0] *3
shoedoor = [0] *2
swap = 0
dontswap = 0
x =random.randint(0,2)
door[x] = "bmw"
for i in range(0,3):
    if(i==x):
        continue
    else:
        door[i] = "shoe"
        shoedoor.append(i)
choice=int(input("enter chioice"))
door_open = random.choice(shoedoor)
while (door_open ==choice):
    door_open = random.choice(shoedoor)
ch = input("do you wanna swap? y/n")
if(ch=='y'):
    if(door[choice]=='shoe'):
        print("you win")
        swap = swap+1
    else:
        print("you lose")
else:
    if(door[choice]=='shoe'):
        print("player lost")
    else:
        print("playern win")
        dontswap = dontswap +1

print(swap)
print(dontswap)
