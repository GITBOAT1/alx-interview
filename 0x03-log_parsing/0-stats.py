#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:
"""


import sys


for line in sys.stdin:
    try:
        val = float(line.strip())
        count += 1
        total += val
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val
    except ValueError:
        # ignore lines that are not valid numbers
        pass
