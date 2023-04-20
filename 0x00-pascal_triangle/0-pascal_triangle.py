#!/usr/bin/python3
"""
A pascal's triangle is an arrangement of numbers in a triangular array
such that the numbers at the end of each row are 1 and the remaining numbers
are the sum of the nearest two numbers in the above row. This concept is
used widely in probability, combinatorics, and algebra. Pascal's triangle
is used to find the likelihood of the outcome of the toss of a coin,
coefficients of binomial expansions in probability, etc.
. """


def pascal_triangle(n):
    """ pascal Triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
