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

try:
    for i, line in enumerate(sys.stdin, start=1):
        match = pattern.match(line.strip())
        if not match:
            continue

        file_size = int(match.group(4)) if match.group(4) != '-' else 0
        status_code = int(match.group(3))

        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

        if i % 10 == 0:
            print("Total file size:", total_size)
            for code in sorted(status_codes):
                print(f"{code}: {status_codes[code]}")
            print()

except KeyboardInterrupt:
    print("Total file size:", total_size)
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")
