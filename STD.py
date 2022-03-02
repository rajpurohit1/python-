'''Basketball Players


The given code includes a list of heights for various basketball players.
You need to calculate and output how many players are in the range of one
standard deviation from the mean.'''







players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

import numpy as np

mean = np.mean(players)
standard_deviation = np.std(players)
#variance = np.var(players)
result = 0
for i in players:
    if i >= mean-standard_deviation and i <= mean+standard_deviation:
        result += 1
print(result)
