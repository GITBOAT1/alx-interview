#!/usr/bin/python3
import sys
"""
Write a script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line
must be skipped)After every 10 lines and/or a keyboard interruption
(CTRL + C), print these statistics from the beginning
"""


# Initialize metrics dictionaries
file_sizes = []
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

line_count = 0
try:
    # Read input from stdin line by line
    for line in sys.stdin:
        line_count += 1
        # Parse input line
        try:
            ip, date, request, status, size = line.split(' ')
            if request != 'GET /projects/260 HTTP/1.1':
                continue
            size = int(size)
            file_sizes.append(size)
            if int(status) in status_codes:
                status_codes[int(status)] += 1
        except ValueError:
            continue

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print(f'Total file size: {sum(file_sizes)}')
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f'{code}: {status_codes[code]}')

except KeyboardInterrupt:
    # Print final statistics on keyboard interrupt
    print(f'Total file size: {sum(file_sizes)}')
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f'{code}: {status_codes[code]}')
