# implements minimax algorithm with alpha/beta pruning for tictactoe game
# December. 2020

from tictactoe_ai_functions import _get_all_possible_moves
from tictactoe_ai_functions import get_winner,check_for_draw,make_move


MAXVAL = 1000
MINVAL = -1000


def _get_opponent(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'


def minimax_score(board, current_player, maximizing_player):
    # terminal state
    winner = get_winner(board)
    if winner:
        if winner == maximizing_player:
            return 10
        else:
            return -10
    elif check_for_draw(board):
        return 0

    # get all possible moves and calculate score
    all_possible_moves = _get_all_possible_moves(board)
    score = []
    for move in all_possible_moves:
        # make move
        next_board = make_move(board, move, current_player)
        # change player
        opponent = _get_opponent(current_player)
        # calculate score of this move
        score.append(minimax_score(next_board, opponent, maximizing_player))

    if current_player == maximizing_player:
        return max(score)
    else:
        return min(score)


def minimax_score_alpha_beta(board, current_player, maximizing_player, alpha, beta):
    # apply alpha-beta pruning to make the algorithm faster which will not check states
    # with lower scores
    # terminal state
    winner = get_winner(board)
    if winner:
        if winner == maximizing_player:
            return 10
        else:
            return -10
    elif check_for_draw(board):
        return 0

    # get all possible moves and calculate score
    all_possible_moves = _get_all_possible_moves(board)
    if current_player == maximizing_player:
        value = MINVAL
        for move in all_possible_moves:
            # make move
            next_board = make_move(board, move, current_player)
            # change player
            opponent = _get_opponent(current_player)
            # calculate score of this move
            value = max(value, minimax_score_alpha_beta(next_board, opponent, maximizing_player, alpha, beta))
            # compare with alpha
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = MAXVAL
        for move in all_possible_moves:
            # make move
            next_board = make_move(board, move, current_player)
            # change player
            opponent = _get_opponent(current_player)
            # calculate score of this move
            value = min(value, minimax_score_alpha_beta(next_board, opponent, maximizing_player, alpha, beta))
            # compare with beta
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


def minimax_ai(board, player):
    all_possible_moves = _get_all_possible_moves(board)
    score = []
    maximizing_player = player
    for move in all_possible_moves:
        alpha = MINVAL
        beta = MAXVAL
        # make move
        next_board = make_move(board, move, player)
        # change player
        opponent = _get_opponent(player)
        # calculate score of this move
        # without pruning
#        score.append(minimax_score(next_board, opponent, maximizing_player))
        # with alpha/beta pruning
        score.append(minimax_score_alpha_beta(next_board, opponent, maximizing_player, alpha, beta))
    # make the move that has the maximum score
    return all_possible_moves[score.index(max(score))]
#    return score

#simple tests
# board = [
#    [None, 'X', 'X'],
#    ['O', None, 'X'],
#    [None, 'O', 'O']
# ]
# board = [
#    [None, 'O', 'O'],
#    ['O', None, 'X'],
#    [None, 'X', 'X']
# ]

# print(minimax_ai(board, 'X'))
