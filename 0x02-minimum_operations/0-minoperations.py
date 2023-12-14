#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ Calculates the minimum amount of operations needed to
        reach n number of 'H's
    """
    if n <= 1:
        return 0
    ops = 0
    divider = 2
    while n > 1:
        if n % divider == 0:
            ops += divider
            n //= divider
        else:
            divider += 1
    return ops
