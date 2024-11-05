#!/usr/bin/python3
import sys
"""
0x05. N Queens
"""


def print_solutions(solutions):
    """
    Print the list of solutions.

    Args:
        solutions (list): A list of solutions to the N-Queens problem.
    """
    for solution in solutions:
        print(solution)


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The chessboard.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the chessboard.

    Returns:
        bool: True if safe, False otherwise.
    """
    # Check this column on upper side
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row=0, board=None, solutions=None):
    """
    Solve the N-Queens problem using backtracking.

    Args:
        n (int): The size of the chessboard (N).
        row (int): The current row to place a queen.
        board (list): The current state of the chessboard.
        solutions (list): A list to store all valid solutions.

    Returns:
        list: A list of all valid solutions.
    """
    if board is None:
        board = [-1] * n
    if solutions is None:
        solutions = []

    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return solutions

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1  # Backtrack

    return solutions


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
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
