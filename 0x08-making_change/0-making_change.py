#!/usr/bin/python3
"""
Interview Question on: fewest number of coins needed to
meet a given amount total

This script contains a function makeChange(coins, total) that calculates
the fewest number of coins needed to meet a given amount total. It takes
two parameters:
    - coins: a list of integers representing the available coin denominations
    - total: an integer representing the target amount to be achieved

The function sorts the coins in descending order and iterates through them,
calculating the number of coins needed to reach the total amount. It returns
the minimum number of coins needed, or -1 if it is not possible to reach the
total amount using the given coins.
"""
def makeChange(coins, total):
    """ fewest number of coins needed to meet total """
    if total <= 0:
        return 0
    # sort the coins in descending order
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change

