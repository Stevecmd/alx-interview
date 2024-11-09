#!/usr/bin/python3
"""
0x05. N Queens
This module solves the N Queens problem,
which involves placing N non-attacking
queens on an N×N chessboard.
A solution requires that no two queens share the
same row, column, or diagonal.
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]

    Args:
        board (list): The current board configuration
        row (int): Row to check
        col (int): Column to check
        n (int): Size of the board

    Returns:
        bool: True if the position is safe, False otherwise
    """
    # Check this row on left side
    if col in board:
        return False

    # Check upper diagonal on left side
    for i, j in enumerate(board):
        if j != -1:
            if abs(row - i) == abs(col - j):
                return False

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and print all solutions

    Args:
        n (int): Size of the board and number of queens
    """
    board = [-1] * n
    solve_nqueens_util(board, 0, n)


def solve_nqueens_util(board, row, n):
    """
    Utility function to solve N Queens problem using backtracking

    Args:
        board (list): Current board configuration
        row (int): Current row being processed
        n (int): Size of the board
    """
    if row == n:
        solution = []
        for i in range(n):
            solution.append([i, board[i]])
        print(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens_util(board, row + 1, n)
            board[row] = -1


def main():
    """
    Main function: Handles command-line arguments and solve N-Queens
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
