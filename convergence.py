from zombieGame import PlayerWithThreshold
import random
import time
from matplotlib import pyplot as plt
import numpy as np

start = time.time()
win = 13
player1turn = True
player1 = PlayerWithThreshold(2, 10)
player2 = PlayerWithThreshold(3, 10)
results = []

player1_win_count = 0
player2_win_count = 0
gameCount = 100000
for game in range(0, gameCount):
    # Play game until someone wins
    while (player1.score != win) and (player2.score != win) :
        if player1turn:
            currScore = 0
            while True:
                roll = random.randint(1, 6)
                if (roll == 3) or (roll == 6):
                    currScore = 0
                    player1turn = False
                    break
                else:
                    currScore += 1
                    if currScore + player1.score == win:
                        player1.score = win
                        break
                    if player2.score >= player1.threshold:
                        continue
                    if currScore == player1.target:
                        player1.score += currScore
                        player1turn = False
                        break
        else:   # Player 2 turn
            currScore = 0
            while True:
                roll = random.randint(1, 6)
                if (roll == 3) or (roll == 6):
                    currScore = 0
                    player1turn = True
                    break
                else:
                    currScore += 1
                    if currScore + player2.score == win:
                        player2.score = win
                        break
                    if player1.score >= player2.threshold:
                        continue
                    if currScore == player2.target:
                        player2.score += player2.target
                        player1turn = True
                        break
    if player1.score == win:
        player1_win_count += 1
        player1.score = 0
    if player2.score == win:
        player2.score = 0
    results.append(player1_win_count/(game+1))

print(results)

end = time.time()
print("Time taken to run: " + str(round(end - start, 3)))

plt.plot(np.arange(0, gameCount, 1), results)
plt.title('Strategy 1 vs Strategy 2')
plt.xlabel('Number of Games Played')
plt.ylabel('Win Ratio')
plt.show()
