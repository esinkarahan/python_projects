# useful auxiliary functions and 3 simple AIs
# for tictactoe game
# December. 2020

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


def make_move(old_board, move_coords, player):
    # makes move and updates board by creating new variable
    if not is_valid_move(old_board, move_coords):
        raise Exception('Can\'t move to {}, it\'s already taken'.format(move_coords))
    next_board = [i[:] for i in old_board]
    if player == 'X':
        next_board[move_coords[0]][move_coords[1]] = 'X'
    else:
        next_board[move_coords[0]][move_coords[1]] = 'O'
    return next_board


def is_valid_move(board, move_coords):
    # check whether move is valid
    if board[move_coords[0]][move_coords[1]] is None:
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


def _get_all_possible_moves(board):
    return [(i, j) for i in range(0, height) for j in range(0, width) if board[i][j] is None]


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
            if board[i][j] is not None:
                k = k + 1
    if k == width * height:
        return True
    else:
        return False


# AI
def random_ai(board, player):
    # plays randomly on available positions
    avail = _get_all_possible_moves(board)
    r = random.randint(0, len(avail) - 1)
    return avail[r]


def find_winning_moves_ai(board, player):
    # finds winning moves if exists, returns random if not
    if _find_winning_moves(board, player):
        return _find_winning_moves(board, player)
    else:  # no available moves, return random
        return random_ai(board, player)


def _find_winning_moves(board, player):
    # winning move is the ones with perm(X,X,None) or perm(O,O,None)
    # get all coordinates of the board
    coords = _get_all_lines_sub(board)
    for row in coords:
        n_p = 0
        n_none = 0
        for r in row:
            if board[r[0]][r[1]] == player:
                n_p += 1
            elif board[r[0]][r[1]] is None:
                n_none += 1
                coord_move = r
        if n_p == 2 and n_none > 0:
            return coord_move
    return None


def _find_blocking_moves(board, player):
    # blocking move is the opponent's winning move!
    if player == 'X':
        opponent = 'O'
    else:
        opponent = 'X'
    coord_block = _find_winning_moves(board, opponent)
    return coord_block


def find_winning_and_losing_moves_ai(board, player):
    # a move that wins, a move that block a loss, and a random move
    # first check for win
    if _find_winning_moves(board, player):
        return _find_winning_moves(board, player)
    # then check for loss and block
    if _find_blocking_moves(board, player):
        return _find_blocking_moves(board, player)
    # if none of them work, return a random move
    return random_ai(board, player)


def human_player(board, player):
    # gets input from human player
    # asks user coordinates of their next move
    while True:
        x = int(input('Enter your next move\'s row number? '))
        if x >= height:
            print('You entered invalid coordinate')
        else:
            break
    while True:
        y = int(input('Enter your next move\'s column number? '))
        if y >= width:
            print('You entered invalid coordinate')
        else:
            break
    return int(x), int(y)
