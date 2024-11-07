#!/usr/bin/python3
import sys
from typing import List


def is_safe(board: List[List[int]], row: int, column: int) -> bool:
    """Check if a queen can be placed on board at given position."""
    for current_row, current_column in board:
        if (column == current_column or
                current_row - current_column == row - column or
                current_row + current_column == row + column):
            return False
    return True


def solve_n_queens(n: int, current_row: int,
                   placed_queens: List[List[int]]) -> None:
    """Recursively solve N queens problem using backtracking."""
    if current_row == n:
        print(placed_queens)
        return

    for column in range(n):
        if is_safe(placed_queens, current_row, column):
            placed_queens.append([current_row, column])
            solve_n_queens(n, current_row + 1, placed_queens)
            placed_queens.pop()


def main():
    """Validate command line arguments and solve N queens problem."""
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

    solve_n_queens(n, 0, [])


if __name__ == "__main__":
    main()
