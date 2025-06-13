#!/usr/bin/python3
"""Making Change Problem Solve"""

def makeChange(coins, total):
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for a in range(1, total + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[total] if dp[total] != total + 1 else -1
