#!/usr/bin/python3
''' Island Perimeter '''


def island_perimeter(grid):
    """
    Args:
        grid (list): A list of lists representing the grid.
    Returns:
        int: The perimeter of the island described in a gird.
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Assume that all sides are exposed

                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2  # Minus 2 if the cell above is also land

                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2  # Minus 2 if cell to the left is also land
    return perimeter
