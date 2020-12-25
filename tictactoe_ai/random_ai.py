import random
from tic_tac_toe import _get_all_lines_sub
width=3
height=3
board = [
  [None, None, 'O'],
  ['X', None, 'X'],
  ['O', 'X', None]
]
def random_ai(board,player):
    #plays randomly on available positions
    avail = [(j,i) for i in range(0,height) for j in range(0,width) if board[i][j]==None]
    r = random.randint(0,len(avail)-1)
    return avail[r]
def find_winning_moves_ai(board,player):
    #finds winning moves if exists, returns random if not
    if _find_winning_moves(board, player):
        return _find_winning_moves(board, player)
    else:# no available moves, return random
        return random_ai(board,player)
def _find_winning_moves(board,player):
    #winning move is the ones with perm(X,X,None) or perm(O,O,None)
    #get all coordinates of the board
    coords = _get_all_lines_sub(board)
    for row in coords:
        n_p = 0
        n_none=0
        for r in row:
            if board[r[0]][r[1]] == player:
                n_p+=1
            elif board[r[0]][r[1]] == None:
                n_none+=1
                coord_move = r
        if n_p == 2 and n_none >0:
            return coord_move
    return None

def _find_blocking_moves(board,player):
    # blocking move is the opponent's winning move!
    if player == 'X':
        opponent = 'O'
    else:
        opponent = 'X'
    coord_block = _find_winning_moves(board, opponent)
    return coord_block
def find_winning_and_losing_moves_ai(board,player):
#a move that wins, a move that block a loss, and a random move
    #first check for win
    if _find_winning_moves(board, player):
        return _find_winning_moves(board, player)
    #then check for loss and block
    if _find_blocking_moves(board,player):
        return _find_blocking_moves(board, player)
    #if none of them work, return a random move
    return random_ai(board,player)

#print (find_winning_moves_ai(board, 'X'))
#print (find_winning_moves_ai(board, 'O'))
print(find_winning_and_losing_moves_ai(board,'X'))
print(find_winning_and_losing_moves_ai(board,'O'))
