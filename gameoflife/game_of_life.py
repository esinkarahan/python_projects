# Project Game of Life based on Robert Heaton's website
#https://robertheaton.com/2018/07/20/project-2-game-of-life/
# 17 December 2020, Esin
#
# Game of life is determined by following 4 rules:
# 1 Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
# 2 Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
# 3 Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
# 4 Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

import random
def random_state(width,height):
    #every cell is randomly initialized to alive or dead
    board=[[random.randint(0,1) for i in range(width)] for j in range(height)]
    return board

def load_board_state(fname):
    #load board state from a file
    f = open(fname, 'r')
    f1 = f.read()
    board = [[int(i) for i in line] for line in f1.splitlines()]
    f.close()
    return board

def render(board):
    # print board on the screen
    width =len(board[0])
    print('_'*(width*2+2))
    for k,row in enumerate(board):
        print('|',end='')
        for cell in row:
            if cell==1:
                print(str('#'),end=' ')
            else:
                print(' ', end=' ')
        print('|')
    print('_'*(width*2+2))

def next_board_state(initial_state):
    #return the next state of the board
    #by using the 4 rules of life
    height=len(initial_state)
    width =len(initial_state[0])
    next_state=[[0 for i in range(width)] for j in range(height)]
    for i in range(height):
        for j in range(width):
            #edge
            ml=1
            mr=1
            nt=1
            nb=1
            if j-1 < 0:
                ml=0
            if j+1 == width:
                mr=0
            if i-1 < 0:
                nt=0
            if i+1 == height:
                nb=0
            neigh = initial_state[i][j - ml]*ml + initial_state[i][j + mr]*mr \
                       + initial_state[i - nt][j]*nt + initial_state[i + nb][j]*nb \
                       + initial_state[i - nt][j - ml]*ml*nt + initial_state[i - nt][j + mr]*mr*nt \
                       + initial_state[i + nb][j - ml]*ml*nb + initial_state[i + nb][j + mr]*nb*mr
            #print(str(i) + ' ' + str(j) + ' ' + str(neigh))
            if neigh < 2 and initial_state[i][j] == 1: # dead: underpopulation
                next_state[i][j] = 0
            if neigh > 3 and initial_state[i][j] == 1: #dead: overpopulation
                next_state[i][j] = 0
            if (1 < neigh < 4) and (initial_state[i][j] == 1): #alive:just right
                next_state[i][j] = 1
            if neigh == 3 and (initial_state[i][j] == 0): #alive: reproduction
                next_state[i][j] = 1
    return next_state

