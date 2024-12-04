#!/usr/bin/python3
"""Island Perimeter

"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the given grid.

    The grid is represented as a list of lists of integers, where 0 represents
    water and 1 represents land. The function returns the perimeter of the
    island in the given grid.

    The perimeter is calculated by counting the number of cells that are
    adjacent to water.

    The function assumes that the grid is rectangular, with its width
    and height not exceeding 100.
    The grid is completely surrounded by water, and there is
    only one island (or nothing).

    The function returns an integer representing the perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check up
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check down
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check right
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
