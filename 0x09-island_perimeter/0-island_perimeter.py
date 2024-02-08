#!/usr/bin/python3
""" Island Perimeter
"""


def island_perimeter(grid):
    """ Returns the perimeter of a rectangular island
    """
    row_idx = None
    land = None

    for i, row in enumerate(grid):
        if 1 in row:
            land = row.index(1)
            row_idx = i
            break

    if row_idx is None or land is None:
        return 0

    width = 0
    for row in grid[row_idx:]:
        if row[land] != 1:
            break
        width += 1

    length = 0
    for i in range(width):
        length = max(length, grid[land + i].count(1))

    return 2 * (width + length)
