import random

def display(board):
    print(f'''
         {board[7]}|{board[8]}|{board[9]}                  7 | 8 | 9
         ---+---+---                 ---+---+---
         {board[4]}|{board[5]}|{board[6]}      Position->  4 | 5 | 6
         ---+---+---                 ---+---+---
         {board[1]}|{board[2]}|{board[3]}                  1 | 2 | 3
         ''')
def valid_input():
    while True:
        pos = input("Enter Position : ")
        if pos != ' ':
            if int(pos) in range(1, 10):
                pos = int(pos)
                break
            print('Not valid position\n')
        else:
            print('Thank You (^u^) for playing Tic-Tac-Toe!')
            exit()
    return int(pos)

def valid_pos(turn, board):
    print(f'{turn} chance')
    pos = valid_input()
    while True:
        if board[pos] == '   ':
            board[pos] = turn
            break
        else:
            print('Cannot overwrite , Please Select new Location .')
            pos = valid_input()
def check(board):
    check = 0
    #rows
    if board[1] == board[2] == board[3] != '   ' or board[4] == board[5] == board[6] != '  ' or board[7] == board[8] == board[9] != '  ':
        check =1
    #columns
    elif board[1] == board[4] == board[7] != '   ' or board[2] == board[5] == board[8] != '   ' or board[3] == board[6] == board[90] != '  ':
        check =1
    #diagonals
    elif board[1] == board[5] == board[9] != '   ' or board[3] == board[5] == board[7] != '   ' or board[2] == board[5] == board[8] != '  ':
        check =1
def userInput(board,symbol) :
    sym1 , sym2 = symbol[random.randint(0,1)]
    print(f'{sym1} is going first\n\n')
    display(board)
    for i in range(9):
        if i%2==0 :
            turn= ' '+sym1+' '
            valid_pos(turn,board)
        else :
            turn = ' '+sym2+' '
            valid_pos(turn,board)
        display(board)
        if i>4 :
            if check(board):
                display(board)
                print(f"'{turn}' won!!!!!! HURRAY!!!!!!!")
                break
        if i==8 :
            print("No one won, (*_*) it's a TIE")

def game():
    board =["Just to adjust loc : ",'   ','   ','   ','   ','   ','   ','   ','   ','   ']
    symbol = [('x','o'),('o','x')]
    name = input('\nEnter your name : ').capitalize()
    marker = input('\nEnter your marker : ').upper()
    print('Hello',name,'! Your marker is "',marker,'".')
    while True:
        if marker == 'X' or marker == 'O':
            userInput(board,symbol)
            break
        else :
            print('Wrong Marker (x,o) Enter your maker again.\n')
    display(board)

def main():
    again ='Y'
    while again == 'Y' :
        print('Press <space> for input whenever you want to stop the game')
        game()
        again = input("Press (Y/y), To play again : ").upper()
main()

