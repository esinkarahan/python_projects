##################################
## Play tic-tac-toe with 2 players
##################################
# Players can be AI or human
# Project based on https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-b/
#
# December. 2020

from tictactoe_ai_functions import *
from tictactoe_minimax import minimax_ai


def tictactoe(alg1, alg2):
    board = new_board()
    render(board)
    player = 'X'
    player_name = alg1
    while True:
        while True:
            if player_name == 'random_ai':
                move_coords = random_ai(board, player)
            elif player_name == 'find_winning_moves_ai':
                move_coords = find_winning_moves_ai(board, player)
            elif player_name == 'find_winning_and_losing_moves_ai':
                move_coords = find_winning_and_losing_moves_ai(board, player)
            elif player_name == 'minimax_ai':
                move_coords = minimax_ai(board, player)
            elif player_name == 'human_player':
                move_coords = human_player(board, player)

            if is_valid_move(board, move_coords):
                break
            else:
                print('invalid move, try again ')
        board = make_move(board, move_coords, player)
        render(board)
        winner = get_winner(board)
        if winner:
            if winner == 'X':
                winner_name = alg1
            else:
                winner_name = alg2
            print('Player {} , {} has won!'.format(winner, winner_name))
            return winner_name
        #            break
        if check_for_draw(board):
            print('It\'s a draw!')
            return None
        #            break
        if player == 'X':
            player = 'O'
            player_name = alg2
        else:
            player = 'X'
            player_name = alg1


# only when run, not when imported
if __name__ == '__main__':
    print('welcome to AI supported tic-tac-toe game!')
    print('Choose your players from: ')
    print('(1) random_ai')
    print('(2) find_winning_moves_ai')
    print('(3) find_winning_and_losing_moves_ai')
    print('(4) minimax_ai')
    print('(5) human_player')
    alg1 = int(input('Enter your response for first player: '))
    alg2 = int(input('Enter your response for second player: '))
    player_names = ['random_ai', 'find_winning_moves_ai',
                    'find_winning_and_losing_moves_ai',
                    'minimax_ai',
                    'human_player']
    tictactoe(player_names[alg1 - 1], player_names[alg2 - 1])
