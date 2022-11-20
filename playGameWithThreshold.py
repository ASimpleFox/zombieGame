from zombieGame import PlayerWithThreshold
import random
import time

arr_2d = [
    [PlayerWithThreshold(2, 10), PlayerWithThreshold(2, 10)],
    [PlayerWithThreshold(2, 10), PlayerWithThreshold(3, 10)],
    [PlayerWithThreshold(2, 10), PlayerWithThreshold(4, 10)],
    [PlayerWithThreshold(2, 10), PlayerWithThreshold(5, 10)],
    [PlayerWithThreshold(2, 10), PlayerWithThreshold(6, 10)],
    [PlayerWithThreshold(3, 10), PlayerWithThreshold(2, 10)],
    [PlayerWithThreshold(3, 10), PlayerWithThreshold(3, 10)],
    [PlayerWithThreshold(3, 10), PlayerWithThreshold(4, 10)],
    [PlayerWithThreshold(3, 10), PlayerWithThreshold(5, 10)],
    [PlayerWithThreshold(3, 10), PlayerWithThreshold(6, 10)],
    [PlayerWithThreshold(4, 10), PlayerWithThreshold(2, 10)],
    [PlayerWithThreshold(4, 10), PlayerWithThreshold(3, 10)],
    [PlayerWithThreshold(4, 10), PlayerWithThreshold(4, 10)],
    [PlayerWithThreshold(4, 10), PlayerWithThreshold(5, 10)],
    [PlayerWithThreshold(4, 10), PlayerWithThreshold(6, 10)],
    [PlayerWithThreshold(5, 10), PlayerWithThreshold(2, 10)],
    [PlayerWithThreshold(5, 10), PlayerWithThreshold(3, 10)],
    [PlayerWithThreshold(5, 10), PlayerWithThreshold(4, 10)],
    [PlayerWithThreshold(5, 10), PlayerWithThreshold(5, 10)],
    [PlayerWithThreshold(5, 10), PlayerWithThreshold(6, 10)],
    [PlayerWithThreshold(6, 10), PlayerWithThreshold(2, 10)],
    [PlayerWithThreshold(6, 10), PlayerWithThreshold(3, 10)],
    [PlayerWithThreshold(6, 10), PlayerWithThreshold(4, 10)],
    [PlayerWithThreshold(6, 10), PlayerWithThreshold(5, 10)],
    [PlayerWithThreshold(6, 10), PlayerWithThreshold(6, 10)],
]
start = time.time()
arr_res = []
win = 13
for arr in arr_2d:
    player1turn = True
    player1 = arr[0]
    player2 = arr[1]

    conf_interval = []
    for i in range(0, 10):
        player1_win_count = 0
        player2_win_count = 0
        gameCount = 100000
        for game in range(1, gameCount):
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
            else:
                player2_win_count += 1
                player2.score = 0
        conf_interval.append(player1_win_count/gameCount)
    res = [min(conf_interval), max(conf_interval)]
    print(res)
    arr_res.append(res)


end = time.time()
print("Time taken to run: " + str(round(end - start, 3)))
print(arr_res)
