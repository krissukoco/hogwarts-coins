# QUESTION:
# In Hogwarts the currency is made up of galleon (G) and Sickle (s), 
# and there are seven coins in general circulation:
# 1s, 5s, 10s, 25s, 50s, G1(100s), and G2(200s)
# It's possible to make G3.5 in the following way:
# 1xG2 +1xG1 + 4x10s +1x5s + 5x1s
# How many different ways can G3.5 be made using any number of coins?

# Using Dynamic Programming: Bottom Up Memoization

from typing import List

def count(coins: List[int], sum: int):
    n = len(coins)
    # Initiate a table to store results
    # The rows represent the sum, and the columns represent the coins
    # The value of table[i][j] will be the number of solutions for
    # sum = i and coins[0..j]
    table = [[0 for x in range(n)] for x in range(sum+1)]

    # Fill the entries for 0 sum
    for i in range(n):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner
    for i in range(1, sum+1):
        for j in range(n):
            coin = coins[j]
            # Count of solutions which include the coin
            x = table[i - coin][j] if i-coin >= 0 else 0
            # Count of solutions which do not include the coin
            y = table[i][j-1] if j >= 1 else 0
            # total count
            table[i][j] = x + y
    # for i, row in enumerate(table):
    #     print(f"{i}: {row}")
    return table[sum][n-1]

# Hogwart coins as presented in the question
coins = [1, 5, 10, 25, 50, 100, 200]
sum = 350
print(f"There are {count(coins, sum)} ways to make {sum} using the following coins: {coins}")