#!/usr/bin/python3
""" Prime Game
"""


def get_first_prime(values):
    """ Get the first prime number from the list
    """
    for i in values:
        if isPrime(i):
            return [v for v in values if v % i != 0]
    return False


def isPrime(x):
    """ Is a given number a prime number
    """
    if x < 2 or x == 4:
        return False
    for i in range(2, x // 2):
        if x % i == 0:
            return False
    return True


def isWinner(x, nums):
    """ Who is the winner of the Prime Game?
    """
    if x != len(nums):
        return None

    maria = {"Turn": True, "Score": 0}
    ben = {"Turn": False, "Score": 0}
    round = 0
    while (x):
        ben["Turn"] = False
        maria["Turn"] = True
        if round >= len(nums):
            round = 0
        current = [i for i in range(1, nums[round] + 1)]
        while (len(current) > 1):
            if get_first_prime(current):
                current = get_first_prime(current)
                if maria["Turn"]:
                    maria["Turn"] = False
                    ben["Turn"] = True
                else:
                    ben["Turn"] = False
                    maria["Turn"] = True
        if maria["Turn"]:
            ben["Score"] += 1
        else:
            maria["Score"] += 1
        round += 1
        x -= 1
    if ben["Score"] < maria["Score"]:
        return 'Maria'
    return 'Ben'
