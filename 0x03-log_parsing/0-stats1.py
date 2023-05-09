#!/usr/bin/python3
import sys
from collections import defaultdict

""" Write a script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" 
<status code> <file size> (if the format is not this one, the line
must be skipped) After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
"""


# initialize variables to store metrics
total_size = 0
status_codes = defaultdict(int)
line_count = 0

try:
    # read lines from stdin
    for line in sys.stdin:
        # split the line into its components
        try:
            ip, _, _, date, _, request, status, size, *_ = line.split()
            method, path, protocol = request.split()
        except ValueError:
            continue  # skip lines that don't match the input format

        # update metrics
        total_size += int(size)
        status_codes[status] += 1
        line_count += 1

        # print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f'Total file size: {total_size}')
            for code in sorted(status_codes):
                if code.isdigit():
                    print(f'{code}: {status_codes[code]}')
            print()

except KeyboardInterrupt:
    # print final statistics on keyboard interruption
    print(f'Total file size: {total_size}')
    for code in sorted(status_codes):
        if code.isdigit():
            print(f'{code}: {status_codes[code]}')
