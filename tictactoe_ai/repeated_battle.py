# Find which AI is the best
# Compare 3 (not so smart) AIs and plot statistics
# Players are:  ['random_ai',
#                'find_winning_moves_ai',
#                'find_winning_and_losing_moves_ai']
# December 2020
#
import matplotlib.pyplot as plt
from tictactoe_ai_functions import *
from tictactoe import tictactoe

def play(player1_name, player2_name):
  # Returns:
  # * 0 if the game is drawn
  # * 1 if player 1 wins
  # * 2 if player 2 wins
  winner = tictactoe(player1_name, player2_name)
  if winner == player1_name:
    return 1
  elif winner == player2_name:
    return 2
  else:
    return 0

def repeated_battle(player1_name, player2_name,nmax=100):
  # Repeatedly call the `play` function and tally the results
  stats=[]
  for n in range(nmax):
    stats.append(play(player1_name, player2_name))
  wins=[]
  wins.append(len(list(filter(lambda i:i==1,stats))))
  wins.append(len(list(filter(lambda i:i==2,stats))))
  draw = len(list(filter(lambda i: i==0,stats)))
  return (wins,draw)


player_names = ['random_ai', 'find_winning_moves_ai',
                'find_winning_and_losing_moves_ai']
wins=[]
draws=[]
for i,j in zip([0,0,1],[1,2,2]):
  w,d = repeated_battle(player_names[i], player_names[j],nmax=1000)
  wins.append(w)
  draws.append(d)

#plot results
labels = ['random vs find_winning_moves',
          'random vs find_winning_and_losing_moves',
          'find_winning_moves vs find_winning_and_losing_moves']

x=range(0,2*len(labels),2)
width=0.35
fig, ax = plt.subplots()
rects1 = ax.bar(list(map(lambda i:i-width/2,x)), [i[0] for i in wins] , 0.3, label='win player 1')
rects2 = ax.bar(list(map(lambda i:i+width/2,x)), [i[1] for i in wins] , 0.3, label='win player 2')
rects3 = ax.bar(list(map(lambda i:i+width*2,x)), draws , 0.3, label='draws')
ax.set_ylabel('Scores')
ax.set_title('Wins and draws for AIs')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
fig.tight_layout()

###
fig, ax = plt.subplots()
rects1 = ax.bar([0, 2], [wins[0][0],wins[1][0]] , 0.2, label=player_names[0])
rects2 = ax.bar([0+width, 4], [wins[0][1],wins[2][0]] , 0.2, label=player_names[1])
rects3 = ax.bar([2+width, 4+width], [wins[1][1],wins[2][1]] , 0.2, label=player_names[2])
rects4 = ax.bar([0+2*width, 2+2*width, 4+2*width], draws , 0.2, label='draw')
ax.set_ylabel('Scores')
ax.set_title('Wins and draws for AIs')
ax.set_xticks([0+width,2+width,4+width])
ax.set_xticklabels(['Game1', 'Game2','Game3'])
ax.legend(bbox_to_anchor=(1, 1))
fig.tight_layout()