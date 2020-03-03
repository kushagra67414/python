def rpc(num1,num2,bit1,bit2):
    p1 = int(num1[bit1]) % 3
    p2 = int(num2[bit2]) % 3
    if ( player1[p1] == player2[p2] ):
        print("draw")
    elif (player1[p1]=='rock' and player2[p2]=='scissor'):
        print("player 1 wins")
    elif (player1[p1] == 'rock' and player2[p2] == 'paper'):
        print("player 2 wins")
    elif (player1[p1] == 'paper' and player2[p2] == 'scissor'):
        print("player 2 wins")
    elif (player1[p1] == 'scissor' and player2[p2] == 'rock'):
        print("player 2 wins")
    elif (player1[p1] == 'paper' and player2[p2] == 'rock'):
        print("player 1 wins")
    elif (player1[p1] == 'scissor' and player2[p2] == 'paper'):
        print("player 1 wins")




player1 = {0:'rock' , 1: 'paper' , 2: 'scissor'}
player2 = {0:'rock' , 1: 'scissor' , 2: 'paper'}

while(1):
    num1 = input("enter your choice p1 :")
    num2 = input("enter choice p2 : ")
    bit1 = int(input("enter bit 1 position"))
    bit2 = int(input("enter bit 2 position"))

    rpc(num1,num2,bit1,bit2)

    ch = input("do yo wanna continue? y/n")
    if(ch=='n'):
        break


