# A simple 2 player tic-tac-toe game

from random import *


def display_board(board):
    """Displays the board"""
    first_line = board[1] + ' | ' + board[2] + ' | ' + board[3]
    second_line = '--+---+--'
    third_line = board[4] + ' | ' + board[5] + ' | ' + board[6]
    fourth_line = '--+---+--'
    fifth_line = board[7] + ' | ' + board[8] + ' | ' + board[9]

    print(first_line)
    print(second_line)
    print(third_line)
    print(fourth_line)
    print(fifth_line)


def who_goes_first():
    """Chooses a random value denoting X or O.
    Returns the random value chosen"""
    value = randint(0, 1)
    if value == 1:
        print('Player X goes first')
        return 'X'
    else:
        print('Player O goes first')
        return 'O'



def check_position(bo, pos, mov):
    """Checks if the position(pos) is free and hasn't been occupied
    If it has, return false"""
    if bo[pos] != ' ':
        return False

    else:
        return True


def check_board(bo, le):
    """bo = board, le = letter
    Checks the """
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))


while True:
    print("\t\tWELCOME TO TIC-TAC-TOE")
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    is_on = True
    turn = who_goes_first()
    while is_on:
        if turn == 'X':
            print("\nIt's Player X's Turn")
            move = 'X'
            position = int(input('Select an empty position (1 - 9): '))
            if check_position(board, position, move):
                board[position] = move
            else:
                print('Position is already occupied, select another')
                continue
            if check_board(board, move):
                display_board(board)
                print(f'{move.upper()} won!')
                is_on = False
            elif " " not in board[1:]:
                print('A tie!')
                is_on = False
                break
            else:
                turn = 'O'
        else:
            print("\nIt's Player O's Turn")
            move = 'O'
            position = int(input('Select an empty position (1 - 9): '))
            if check_position(board, position, move):
                board[position] = move
            else:
                print('Position is already occupied, select another')
                continue
            if check_board(board, move):
                display_board(board)
                print(f'{move.upper()} won!\n')
                is_on = False
            elif " " not in board[1:]:
                print('A tie!\n')
                is_on = False
                break
            else:
                turn = 'X'
        display_board(board)
    print('Do you want to play again? (y or n)')
    if not input().lower() == 'y':
        break
