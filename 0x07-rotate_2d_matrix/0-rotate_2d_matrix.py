#!/usr/bin/python3
""" This script rotates a 2D matrix """


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list[list]): A 2D matrix of size n x n

    Returns:
        None. The matrix is edited in-place.
    """
    n = len(matrix)
    # Transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse rows
    for i in range(n):
        matrix[i] = matrix[i][::-1]
