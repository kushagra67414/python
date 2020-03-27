import numpy
board =numpy.array( [ ['-','-','-'] , ['-','-','-'] , ['-','-','-'] ] )
p1 = 'x'
p2 = 'o'


def check_Row(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count = count+1
        if count == 3 :
            print(symbol,'won')
            return True
    return False
def check_col(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbol:
                count = count+1
        if count == 3 :
            print(symbol,'won')
            return True
    return False

def check_dia(symbol):
    if board[0][2]==board[1][1] and board[1][1] == board[2][0] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    if board[0][0]==board[1][1] and board[1][1] == board[2][2] and board[1][1]==symbol:
        print(symbol,'won')
        return True
    return False

def won(symbol):
    return check_Row(symbol) or check_col(symbol) or check_dia(symbol)

def place(symbol):
    print (numpy.matrix(board))
    while(1):
        row = int (input('enter row 1 n 2 n 3'))
        col = int(input('enter column 1n 2n 3'))
        if row>0 and row<4 and col>0 and col<4 and board[row -1][col -1 ] =='-' :
            break
        else :
            print('invalid data')
    board[row-1][col-1] = symbol

def play():
    for turn in range(9):
        if turn%2==0:
            print('x turn')
            place(p1)
            if won(p1):
                break

        else :
            print('y turn')
            place(p2)
            if won(p2):
                break
        if not(won(p1) and won(p2)):
            print("its a draw")

play()

