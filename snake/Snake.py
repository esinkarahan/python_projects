# Project Snake based on Robert Heaton's website
# https://robertheaton.com/2018/12/02/programming-project-5-snake/
#
# October 2020, Esin

from define_class import *

# play Snake game by pressing
# W for up, S for down
# A for left, D for right

def game_over(score):
    print('Sorry, You lost the game!')
    print('Score: ', score)
    exit()

def where_to_move(x):
    return {
        'W': UP,
        'S': DOWN,
        'A': LEFT,
        'D': RIGHT
    }.get(x)


def check_wall(head_new, matrix):
    if head_new[0] >= matrix.height-2 or head_new[0] <= -1 or head_new[1] >= matrix.width - 2 or head_new[1] <= -1 :
        dead = 1
    else:
        dead = 0
    return dead


print('Welcome to Snake 1.0! ')
print('Play Snake game by pressing W for up, S for down, A for left, D for right')
print('After entering direction, press Enter to make the move')

height = input('Enter the board height you want to play e.g. 10: ')
width = input('Enter the board width you want to play e.g. 20: ')
if len(height) == 0:
    height = 10
if len(width) == 0:
    width = 20
game = Game(int(height), int(width))
game.render()

## If the player presses W and then Enter, their snake will slink one square up.
# If they press S then Enter then it will slink one square down.
## And it they just hit Enter without pressing any other key, then it will slink
# one square in whichever direction it was traveling before.
## if they choose a direction opposite of snake's direction ignore it
## Update our game so that if the player crashes their snake into itself then their game is over.
## Print a message of condolence and exit the program.
# players were also killed if they bashed into a wall.
while(1):
    move = str(input()).upper()
    if len(move) == 0:#empty string
        # if player only presses enter, ignore
        game.Snake.set_direction()
        game.Snake.take_step(game.Snake.direction)
    else:
        move = move[0]
        m = where_to_move(move)
        # if it wants to move opposite direction ignore it
        if tuple([i*-1 for i in m]) != game.Snake.direction:
            head_new = tuple(map(sum, zip(game.Snake.head(), m)))
            if head_new in game.Snake.body:
                # crashing on itself, stop the game
                game_over(game.score)
            else:
                if check_wall(head_new, game) == 1:
                    # bumping into the wall stop the game
                    game_over(game.score)
                else:
                    game.Snake.take_step(m)
        # check whether apple is eaten
        if head_new == game.Apple.loc:
            # make a new apple
            game.Apple.update_loc(game)
            # extend body of snake
            game.Snake.extend_body()
            # When the player eats an apple, increment their score by 1
            game.update_score()
    game.render()