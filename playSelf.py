from zombieGame import Player
import numpy as np
import random
from matplotlib import pyplot as plt
import time

### Plays the game with self, using a target score of 3 per turn
start = time.time()
player1 = Player(3)
win = 13
turnsTaken = []

# Do 1000 runs of 1000 games
for gameSet in range(1, 1000):
    totalTurns = 0
    totalGames = 1000
    for game in range(1, totalGames):
        # Play game
        turns = 0
        while player1.score != win:
            currScore = 0
            turns += 1
            while currScore < player1.target:
                roll = random.randint(1, 6)
                if (roll == 3) or (roll == 6):
                    currScore = 0
                    break
                else:
                    currScore += 1
                    if currScore + player1.score == win:
                        player1.score = win
                        break
                    if currScore == player1.target:
                        player1.score += currScore
                        player1turn = False
                        break
        totalTurns += turns  # Add to turns
        player1.score = 0    # Reset score
    turnsTaken.append(totalTurns / totalGames)

end = time.time()
print("Time taken to run: " + str(round(end - start, 3)))

# Plotting Histogram
plt.xlim([min(turnsTaken)-0.3, max(turnsTaken)+0.3])
bins = np.arange(0, 100, 0.1)  # Fixed bin size
plt.hist(turnsTaken, bins=bins-0.2)
plt.title('Player with strategic target score of 3')
plt.xlabel('Turns Taken')
plt.ylabel('Number of Games')

plt.show()
