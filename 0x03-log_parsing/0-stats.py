#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:
"""


import sys
import re


"""
script that reads stdin line by line and computes metrics:
"""

regex = r'^([\d\.]+) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+|-)$'
pattern = re.compile(regex)
