#!/usr/bin/python3
""" N Queens
"""
import sys


def print_board(board, n):
    """ Prints the board
    """
    b = []
    for i in range(n):
        for j in range(n):
            if j == board[i]:
                b.append([i, j])
    print(b)


def check_is_safe(board, i, j, r):
    """ Check if position in the board is correct
    """
    return board[i] in (j, j - i + r, i - r + j)


def solve_n_queens(board, row, n):
    """ Finds all safe positions
    """
    if row == n:
        print_board(board, n)
    else:
        for j in range(n):
            allowed = True
            for i in range(row):
                if check_is_safe(board, i, j, row):
                    allowed = False
            if allowed:
                board[row] = j
                solve_n_queens(board, row + 1, n)


def create_board(size):
    """ Generate the board
    """
    return [0 * size for _ in range(size)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if (n < 4):
        print("N must be at least 4")
        exit(1)

    board = create_board(int(n))
    row = 0
    solve_n_queens(board, row, int(n))
