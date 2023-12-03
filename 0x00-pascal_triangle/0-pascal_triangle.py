#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """ Prints the Pascal Triangle """
    arr = []
    if (n <= 0):
        return (arr)
    for i in range(n):
        a = []
        for j in range(i + 1):
            if j == 0 or j == i:
                a.append(1)
            else:
                value = arr[i - 1][j - 1] + arr[i - 1][j]
                a.append(value)
        arr.append(a)
    return (arr)
