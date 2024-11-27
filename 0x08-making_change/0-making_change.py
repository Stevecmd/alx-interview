#!/usr/bin/python3
"""Change comes from within
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to meet.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If the total cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0

    # Initialize the dp array with a value greater than the
    # maximum possible number of coins
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
