#!/usr/bin/python3
import sys

"""
0x05. N Queens

This module solves the N Queens problem,
which involves placing N non-attacking
queens on an N×N chessboard.
A solution requires that no two queens share the
same row, column, or diagonal.
"""


def nqueens(size, row, queens):
    """
    Recursively solves the N Queens problem using backtracking.

    Args:
        size (int): The size of the chessboard (N).
        row (int): The current row being processed.
        queens (list): List of coordinates for placed queens.

    This function attempts to place queens on the board one row at a time,
    checking for valid positions and backtracking when necessary.
    """
    if row == size:
        # When we reach size, we've found a valid solution
        print(queens)
        return

    for col in range(size):
        # Check if the current position is safe
        if is_safe(queens, row, col):
            queens.append([row, col])
            # Recursively try to place queens in next rows
            nqueens(size, row + 1, queens)
            # Backtrack by removing the queen we just placed
            queens.pop()


def is_safe(queens, row, col):
    """
    Checks if a queen can be placed on the board at the given position.

    Args:
        queens (list): Current queen positions on the board.
        row (int): Row to check.
        col (int): Column to check.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for queen in queens:
        # Check if the position conflicts with any existing queen
        if (col == queen[1] or      # Same column
                row - col == queen[0] - queen[1] or  # Same diagonal
                row + col == queen[0] + queen[1]):  # Same reverse diagonal
            return False
    return True


def main():
    """
    Main function to handle command-line arguments and solve N-Queens.

    It checks for the correct number of arguments, validates the input,
    and calls the solve_nqueens function to find solutions.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Start the recursive solution with an empty list of queens
    nqueens(size, 0, [])


if __name__ == "__main__":
    main()
