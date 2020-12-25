import random
# Define directions
global UP, DOWN, LEFT, RIGHT
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, position):
        # add this position to the front of the snake’s body,
        # and pop off the back position
        self.body = self.body[1:] + [tuple(map(sum, zip(self.head(), position)))]
        # every time it moves, update direction
        self.set_direction()

#    def set_direction(self, direction):
    def set_direction(self):
        # sets the argument as the snake’s direction
        direction = (self.head()[0]-self.body[-2][0], self.head()[1]-self.body[-2][1])
        self.direction = direction

    def head(self):
        # returns the position of the front of the snake's body
        return self.body[-1]

    def extend_body(self):
        # add inline with the direction of tail
        direction = (self.body[0][0] - self.body[1][0], self.body[0][1] - self.body[1][1])
        b = [tuple(map(sum, zip(self.body[0], direction)))]
        for i, v in enumerate(self.body):
            b.append(v)
        self.body = b


class Apple:
    def __init__(self, init_loc):
        self.loc = init_loc

    def update_loc(self, Game):
        self.loc = gen_random_loc(Game.height,Game.width,Game.Snake.body)


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.Snake = Snake([(0, 0), (1, 0), (2, 0), (3, 0)], DOWN)
        #self.Snake = Snake([(3, 3), (2, 3), (2, 2), (2, 1), (1, 1), (0, 1)], UP)
        self.Apple = Apple(gen_random_loc(height, width, self.Snake.body))
        self.score = 0

    def update_score(self):
        self.score = len(self.Snake.body)

    def board_matrix(self):
        m = self.width
        n = self.height
        matrix = [[' ' for i in range(m)] for j in range(n)]
        # add borders to matrix
        # edges are | -
        for i in range(m):
            matrix[0][i] = '-'
            matrix[n - 1][i] = '-'
        for j in range(n):
            matrix[j][0] = '|'
            matrix[j][m - 1] = '|'
        # corners are +
        matrix[0][0] = '+'
        matrix[n - 1][m - 1] = '+'
        matrix[0][m - 1] = '+'
        matrix[n - 1][0] = '+'
        return matrix

    def render(self):
#        print("Height: ", self.height)
#        print("Width: ", self.width)
        matrix = self.board_matrix()
        # update matrix with snake
        for pp in self.Snake.body:
            matrix[pp[0] + 1][pp[1] + 1] = 'o'
        matrix[self.Snake.head()[0] + 1][self.Snake.head()[1] + 1] = 'x'
        # update matrix with apple
        matrix[self.Apple.loc[0] + 1][self.Apple.loc[1] + 1] = '@'

        # print matrix
        for row in matrix:
            for e in row:
                print(e, end='')
            print('\n')


def gen_random_loc(height,width,body):
    # generate all possible combinations
    seq = [(i, j) for i in range(height-2) for j in range(width-2)]
    # remove snake body from random locations
    seq_f = [i for i in seq if i not in body]
    return seq_f[random.randrange(len(seq_f))]
