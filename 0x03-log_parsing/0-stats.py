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


total_size = 0
status_codes = {}

ode}: {status_codes[code]}")
            print()

except KeyboardInterrupt:
    print("Total file size:", total_size)
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")
