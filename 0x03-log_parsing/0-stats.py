#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:
"""


import sys
import re


"""
script that reads stdin line by line and computes metrics:
"""


# initialize variables
total_size = 0
status_codes = {}

regex = r'^([\d\.]+) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" \
(\d+) (\d+|-)$'
pattern = re.compile(regex)



