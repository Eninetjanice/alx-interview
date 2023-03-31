#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """Returns list of lists of int representing Pascal's triangle of n."""

    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Create a list to store the triangle
    triangle = [[1]]

    # Build the triangle row by row
    for i in range(1, n):
        # Create a new row
        row = [1]
        for j in range(1, i):
            # Calculate val of each element in row base on val in previous row
            value = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(value)
        row.append(1)
        # Add the new row to the triangle
        triangle.append(row)

    # Return the completed triangle
    return triangle
