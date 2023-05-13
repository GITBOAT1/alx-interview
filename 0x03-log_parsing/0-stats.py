#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:
"""


import sys
import re

"""
script that reads stdin line by line and computes metrics:
"""

# regular expression to match the input format
regex = r'^([\d\.]+) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+|-)$'
pattern = re.compile(regex)

# initialize variables
total_size = 0
status_codes = {}

try:
    # read input line by line
    for i, line in enumerate(sys.stdin, start=1):
        # check if the line matches the input format
        match = pattern.match(line.strip())
        if not match:
            continue

        # extract the file size and status code from the line
        file_size = int(match.group(4)) if match.group(4) != '-' else 0
        status_code = int(match.group(3))

        # update the total file size and the status code count
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

        # print statistics every 10 lines or on keyboard interruption
        if i % 10 == 0:
            print("Total file size:", total_size)
            for code in sorted(status_codes):
                print(f"{code}: {status_codes[code]}")
            print()

except KeyboardInterrupt:
    # print final statistics on keyboard interruption
    print("Total file size:", total_size)
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")
