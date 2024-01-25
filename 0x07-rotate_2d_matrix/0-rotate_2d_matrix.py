#!/usr/bin/python3
""" Rotate 2d Matrix
"""


def rotate_2d_matrix(matrix):
    """ Rotating a 2d matrix 90deg
    """
    n_matrix = list(reversed([row[:] for row in matrix]))
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            matrix[row][col] = n_matrix[col][row]
