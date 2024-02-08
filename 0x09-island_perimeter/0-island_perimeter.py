#!/usr/bin/python3
""" Island Perimeter
"""


def island_perimeter(grid):
    """ Returns the perimeter of a rectangular island
    """
    land = 0
    for row in grid:
        for col in row:
            if col == 1:
                land += 1
    land += 1

    perimeter = 2 * land
    return perimeter
