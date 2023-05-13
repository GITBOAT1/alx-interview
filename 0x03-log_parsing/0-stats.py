#!/usr/bin/python3
import sys
import signal


"""
 Write a script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line
must be skipped) After every 10 lines and/or a keyboard interruption
(CTRL + C), print these statistics from the beginning:Total file size:
File size: <total size> where <total size> is the sum of all previous
<file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
"""


# Initialize dictionaries to store metrics
status_counts = {}
total_size = 0
line_count = 0


def signal_handler(sig, frame):
    """# Define a signal handler to print metrics
    on keyboard interrupt (CTRL+C)
    """
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def print_metrics():
    """
    # Define a function to print the current metrics
    """
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if isinstance(status_code, int):
            print(f"{status_code}: {status_counts[status_code]}")


# Process input from stdin
for line in sys.stdin:
    try:
        # Parse the line and extract the file size and status code
        parts = line.split()
        file_size = int(parts[8])
        status_code = int(parts[10])

        # Update the metrics
        total_size += file_size
        status_counts[status_code] = status_counts.get(status_code, 0) + 1
        line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

    except (ValueError, IndexError):
        # Skip the line if it doesn't match the expected format
        continue

if __name__ == " __main__":
    # Print the final metrics
    print_metrics()
