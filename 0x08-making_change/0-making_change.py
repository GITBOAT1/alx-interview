#!/usr/bin/python3
"""
0x08. Making Change
"""
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins needed to make change for amount 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
