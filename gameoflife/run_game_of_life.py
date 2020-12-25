# Project Game of Life based on Robert Heaton's website
#https://robertheaton.com/2018/07/20/project-2-game-of-life/
# 17 December 2020, Esin
#
# Run game of life from 6 initial conditions:
# Toad, Beacon, Blinker, Glider, Gosper Glider Gun and Random
#
import time
from game_of_life import next_board_state, random_state, render
from game_of_life import load_board_state
resp = input('Start game of life from: Toad, Beacon, Blinker, Glider, Gosper Glider Gun (ggg) or Random \n')
if resp.lower() == 'toad':
    s0 = load_board_state('./toad.txt')
elif resp.lower() == 'beacon':
    s0 = load_board_state('./beacon.txt')
elif resp.lower() == 'blinker':
    s0 = load_board_state('./blinker.txt')
elif resp.lower() == 'glider':
    s0 = load_board_state('./glider.txt')
elif resp.lower() == 'ggg':
    s0 = load_board_state('./ggg.txt')
elif resp.lower() == 'random':
    s0 = random_state(5,5)
else:
    print('you did not pick any pattern, starting from random')
    s0 = random_state(5,5)

render(s0)
while (1):
    s_next = next_board_state(s0)
    render(s_next)
    time.sleep(0.5)  # Pause .5 seconds
    s0 = s_next
