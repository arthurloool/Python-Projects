# Tic-Tac-Toe

# Board
board={'7':' ','8':' ','9':' ',
       '4':' ','5':' ','6':' ',
       '1':' ','2':' ','3':' '}

def display_board():
    global board
    print(board['7']+'|'+board['8']+'|'+board['9']+'\n'+
          '-+-+-'+'\n'+
          board['4']+'|'+board['5']+'|'+board['6']+'\n'+
          '-+-+-'+'\n'+
          board['1']+'|'+board['2']+'|'+board['3'])

# Game Rule
def winp1():
    print('Player 1 Win')
    exit()

def winp2():
    print('Player 2 Win')
    exit()

player1_state = None
def player1_win():
    global board
    global player1_state
    if board['1']=='O' and board['2']=='O' and board['3']=='O':
        winp1()
    elif board['4']=='O' and board['5']=='O' and board['6']=='O':
        winp1()
    elif board['7']=='O' and board['8']=='O' and board['9']=='O':
        winp1()
    elif board['7']=='O' and board['4']=='O' and board['1']=='O':
        winp1()
    elif board['8']=='O' and board['5']=='O' and board['2']=='O':
        winp1()
    elif board['9']=='O' and board['6']=='O' and board['3']=='O':
        winp1()
    elif board['7']=='O' and board['5']=='O' and board['3']=='O':
        winp1()
    elif board['9']=='O' and board['5']=='O' and board['1']=='O':
        winp1()
    else:
        player1_state = None

player2_state = None
def player2_win():
    global board
    global player2_state
    if board['1']=='X' and board['2']=='X' and board['3']=='X':
        winp2()
    elif board['4']=='X' and board['5']=='X' and board['6']=='X':
        winp2()
    elif board['7']=='X' and board['8']=='X' and board['9']=='X':
        winp2()
    elif board['7']=='X' and board['4']=='X' and board['1']=='X':
        winp2()
    elif board['8']=='X' and board['5']=='X' and board['2']=='X':
        winp2()
    elif board['9']=='X' and board['6']=='X' and board['3']=='X':
        winp2()
    elif board['7']=='X' and board['5']=='X' and board['3']=='X':
        winp2()
    elif board['9']=='X' and board['5']=='X' and board['1']=='X':
        winp2()
    else:
        player2_state = None

def tie():
    if ' ' not in board.values() and player1_state == None and player2_state == None:
        print('Tie')
        exit()

# Play
def play1():
    player1_O ='O'

    while True:

        print('Choose your grid. 1-9'+'\n'+
              '7|8|9'+'\n'+ 
              '-+-+-'+'\n'+
              '4|5|6'+'\n'+
              '-+-+-'+'\n'+
              '1|2|3')
    
        while True:
            player1_input = input('Player 1: ')

            if board[str(player1_input)] != ' ':
                print('Already picked, choose another.')
                break
            else:
                board[str(player1_input)] = player1_O
                display_board()
                player1_win()
                tie()
                play2()

def play2():
    player2_X ='X'

    while True:

        print('Choose your grid. 1-9'+'\n'+
              '7|8|9'+'\n'+ 
              '-+-+-'+'\n'+
              '4|5|6'+'\n'+
              '-+-+-'+'\n'+
              '1|2|3')
    
        while True:
            player2_input = input('Player 2: ')

            if board[str(player2_input)] != ' ':
                print('Already picked, choose another.')
                break
            else:
                board[str(player2_input)] = player2_X
                display_board()
                player2_win()
                tie()
                play1()

def game():
    play1()

game()
