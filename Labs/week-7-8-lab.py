import replit
import time

# Constants in are named in all caps (PEP8 Standard)
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '
TIE_GAME = 'tie'
BOARD_SIZE = 3

current_player = PLAYER_X # Player X goes first

# Builds an EMPTY board
board = [[EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY],
        [EMPTY,EMPTY,EMPTY]]


def print_board():
    # Clear the screen
    replit.clear()

    """Prints the board to the console"""
    print('    0   1   2')
    print('  -------------')
    for i, row in enumerate(board):
        print(i, end="")
        for square in row:
            print(' | ' + square, end="")
        print(' |')
        print('  -------------')



def is_empty(row, col):
    """Returns True/False if a square is EMPTY

    params row, col: (int) The row and Column to Check
    return: (boolean) If the row is EMPTY
    """
    # TODO Part #1 complete is_empty()
    square = board[row][col]
    if square == EMPTY:
        return True
    else:
        return False

def move(player, row, col):
    """Makes a game move

    If a move is legal, moves the player to the row and col
    and returns True. If a move is illegal, no move is made
    and returns False. Hint: Should make use of is_empty()

    param player: Either PLAYER_X or PLAYER_O
    param row, col: (int) The row and Column to move to
    return: (boolean) Success of the move
    """
    #TODO Part #2 complete move()
    if is_empty(row,col):
        board[row][col] = player
        return True
    else:
        return False

def determine_winner():
    """Determine if there is a winner

    return: Returns None if there is no winner.
            Returns PLAYER_O or PLAYER_X if one of them won.
            Returns 'tie' if noone wins
    """
    #TODO Part #3 complete determine_winner()

    # Step 1: Check the horizontals looking for a winner.
    #         If so return winner.
    # Step 2: Check the verticals looking for a winner
    #         If so return winner.
    # Step 3: Check the diagonals looking for a winner
    #         If so return winner.
    # Step 4: Check to see if there are empty squares.
    #         If there are empty squares, return None because
    #         noone has won the game yet
    #         If there are no empty squares return TIE_GAME
    #         because we didn't find a winner and all moves are made
    for i, row in enumerate(board):
        #Checks horizontal wins
        if row[0] != EMPTY and row[1] == row[0] and row[2] == row[1]:
            return row[0]
        # Checks vertical wins
        elif board[0][i] != EMPTY and board[1][i] == board[0][i] and board[2][i] == board[1][i]:
            return board[0][i]

    # Checking diagonals
    if board[0][0] != EMPTY and board[1][1] == board[0][0] and board[2][2] == board[1][1]:
        return board[0][0]
    elif board[0][2] != EMPTY and board[1][1] == board[0][2] and board[2][0] == board[1][1]:
        return board[0][2]

    # EMPTY check to comfirm game over
    for row in board:
        if EMPTY in row:
            return None

    return TIE_GAME


while True:
    print()
    print_board()
    print()
    print('It is', current_player, 'turn')
    row = int(input('What is the row (0-3)? '))
    col = int(input('What is the col (0-3)? '))

    # Make sure the move is legal, if so make the move
    if is_empty(row, col):
        move(current_player, row, col)
    else:
        print('That is not a legal move!')
        time.sleep(2)
        continue

    # Check if there is a winner
    winner = determine_winner()
    if winner in (PLAYER_O, PLAYER_X):
        print_board()
        print('Congratulations', winner,'!!! You won!')
        print('But you are all winners')
        break

    if winner == TIE_GAME:
        print_board()
        print("It's a tie!!!")
        break

    # Let the other player have a turn
    if current_player == PLAYER_O:
        current_player = PLAYER_X
    else:
        current_player = PLAYER_O
