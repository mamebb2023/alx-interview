#!/usr/bin/python3
""" Island Perimeter
"""


def island_perimeter(grid):
    """ Returns the perimeter of a rectangular island
    """
    row_index = None
    island_index = None
    for i, row in enumerate(grid):
        if 1 in row:
            island_index = row.index(1)
            row_index = i
            break

    if row_index is None or island_index is None:
        return 0

    width = 0
    for row in grid[row_index:]:
        if row[island_index] != 1:
            break
        width += 1

    length = 0
    for i in range(width):
        length = max(length, grid[island_index + i].count(1))

    return (2 * width) + (2 * length)
