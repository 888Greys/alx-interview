#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island represented by a grid
    of 1s and 0s, where 1s represent land and 0s represent water.
    Args:
        grid (list): A list of lists representing the island.
    Returns:
        The perimeter of the island as an integer.
    """

    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    p += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    p += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    p += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    p += 1
    return p
