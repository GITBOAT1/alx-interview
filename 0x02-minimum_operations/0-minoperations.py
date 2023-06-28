#!/usr/bin/python3

"""
In a text file, there is a single character
 H. Your text editor can execute only two operations
 in this file: Copy All and Paste. Given a number n,
 write a method that calculates the fewest number of
 operations needed to result in exactly n H characters
 in the file.
"""


def minOperations(n):
    """
    Minimum Operations
    """
    if n == 1:
        return 0
    num_ops = 0
    num_H = 1
    while num_H < n:
        if n % num_H != 0:
            return 0
        num_H *= 2
        num_ops += 1
    return num_ops
