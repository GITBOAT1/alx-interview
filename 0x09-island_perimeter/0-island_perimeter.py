#!/usr/bin/python3
"""
0x09. Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island represented by a grid.

    Args:
        grid (List[List[int]]): A 2D grid where 1 represents
        land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """

    # Check if the grid is empty
    if not grid or not grid[0]:
        return 0

    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])

    # Initialize the perimeter
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the cell contains land (1)
            if grid[i][j] == 1:
                # Increment the perimeter by 4 for each land cell
                perimeter += 4
                # Check and subtract 2 if there is land to the left
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                # Check and subtract 2 if there is land above
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    # Return the calculated perimeter
    return perimeter
