#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the rotation
    for i in range(n):
        matrix[i].reverse()