# tic-tac-toe
import random

width = 3
height = 3


def new_board():
    # returns an empty w x h board
    board = [[None for i in range(0, width)] for j in range(0, height)]
    return board


def render(board):
    # print board on screen with coordinates
    print('  0 ' + '1 ' + '2 ')
    print('  ' + '-' * width * 2)
    for i in range(height):
        print(str(i) + '|', end='')
        for j in range(width):
            if board[i][j] is None:
                print(' ', end=' ')
            else:
                print(board[i][j], end=' ')
        print('|')
    print('  ' + '-' * width * 2)


def get_move():
    # asks user coordinates of their next move
    while True:
        x = int(input('What\'s your next move\'s row number? '))
        if x >= height:
            print('You entered invalid coordinate')
        else:
            break
    while True:
        y = int(input('What\'s your next move\'s column number? '))
        if y >= width:
            print('You entered invalid coordinate')
        else:
            break
    return ((int(x), int(y)))


def make_move(old_board, move_coords, player):
    # makes move and updates board by creating new variable
    if not is_valid_move(old_board, move_coords):
        raise Exception('Can\'t move to {}, it\'s already taken'.format(move_coords))
    new_board = old_board.copy()
    if player == 'X':
        new_board[move_coords[0]][move_coords[1]] = 'X'
    else:
        new_board[move_coords[0]][move_coords[1]] = 'O'
    return new_board


def is_valid_move(board, move_coords):
    # check whether move is valid
    if board[move_coords[0]][move_coords[1]] == None:
        return 1
    else:
        return 0


def _get_all_lines_value(board):
    # rows
    lines = board.copy()
    # cols
    [lines.append([board[i][j] for i in range(0, height)]) for j in range(0, width)]
    # diags
    lines.append([board[i][j] for i, j in zip([0, 1, 2], [0, 1, 2])])
    lines.append([board[i][j] for i, j in zip([0, 1, 2], [2, 1, 0])])
    return lines


def _get_all_lines_sub(board):
    coords = []
    # cols
    [coords.append([(j, i) for i in range(0, width)]) for j in range(0, height)]
    # rows
    [coords.append([(i, j) for i in range(0, height)]) for j in range(0, width)]
    # diags
    coords.append([(i, j) for i, j in zip([0, 1, 2], [0, 1, 2])])
    coords.append([(i, j) for i, j in zip([0, 1, 2], [2, 1, 0])])
    return coords


def get_winner(board):
    # check whether any player has won and report the winner
    # built a list of all lines
    lines = _get_all_lines_value(board)
    for line in lines:
        if line == ['O', 'O', 'O']:
            return 'O'
        if line == ['X', 'X', 'X']:
            return 'X'
    return False


def check_for_draw(board):
    # check for draw
    k = 0
    for i in range(width):
        for j in range(height):
            if board[i][j] != None:
                k = k + 1
    if k == width * height:
        return True
    else:
        return False


##################################
## Play tic-tac-toe
##################################
if __name__ == '__main__':
    print('welcome to 2 players tic-tac-toe game!')
    board = new_board()
    player = 'X'
    while True:
        while True:
            move_coords = get_move()
            if is_valid_move(board, move_coords):
                break
            else:
                print('invalid move, try again ')
        board = make_move(board, move_coords, player)
        render(board)
        winner = get_winner(board)
        if winner:
            print('Player {} has won!'.format(winner))
            break
        if check_for_draw(board):
            print('It\'s a draw!')
            break
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
