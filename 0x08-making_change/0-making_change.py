#!/usr/bin/python3
""" Making Change
"""


def makeChange(coins, total):
    """ Returns the fewest number of coins needed to meet a given amount total
    """
    if total < 0:
        return 0

    s_coins = sorted(coins, reverse=True)
    coin_sum = 0
    n_coins = 0
    for coin in s_coins:
        while (coin + coin_sum) <= total:
            coin_sum += coin
            n_coins += 1
        if coin_sum == total:
            return n_coins

    if coin_sum != total:
        return -1
