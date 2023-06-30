#!/usr/bin/python3
"""Script to calculate fewest num of coins needed to meet a given total"""


def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin values.
        total (int): Target total.

    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if total < 0:
        return 0
    if total == 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]


if __name__ == "__main__":
    coins = [1, 2, 5]
    total = 11
    result = makeChange(coins, total)
    print(result)
