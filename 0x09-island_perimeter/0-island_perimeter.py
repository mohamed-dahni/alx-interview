#!/usr/bin/python3
"""Define the island perimeter finding function."""


def island_perimeter(grid):
    """Count the perimeter of an island.

    Args:
        grid (list): A list of lists of integers representing an island.
    Returns:
        int: The perimeter of the island defined in the grid.
    """
    perimeter = 0

    for ri, row in enumerate(grid):
        for ci, column in enumerate(row):
            if column:
                # Check top part
                if ri == 0 or grid[ri - 1][ci] == 0:
                    perimeter += 1
                # Check left part
                if ci == 0 or grid[ri][ci - 1] == 0:
                    perimeter += 1
                # Check right part
                if ci == len(row) - 1 or grid[ri][ci + 1] == 0:
                    perimeter += 1
                # Check bottom part
                if ri == len(grid) - 1 or grid[ri + 1][ci] == 0:
                    perimeter += 1

    return perimeter
