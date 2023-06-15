#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """
    implementation uses a dynamic
    programming approach to solve the problem.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
