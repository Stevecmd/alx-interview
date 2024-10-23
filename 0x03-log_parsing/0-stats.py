#!/usr/bin/python3
"""Reads HTTP request logs through stdin line by line
    and prints statistics
    Usage: ./0-stats.py
"""

import sys


def print_stats(file_size, status_codes):
    """Prints the computed metrics"""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


# Initialize metrics
file_size = 0
status_codes = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}

try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            # Split the line and validate format
            parts = line.split()

            # Check if line matches required format
            if len(parts) < 7:
                continue

            # Extract status code and file size from the end
            status_code = parts[-2]
            size = parts[-1]

            # Update metrics if status code is valid
            if status_code in status_codes:
                status_codes[status_code] += 1

            # Add file size
            file_size += int(size)

            # Print stats every 10 lines
            if i % 10 == 0:
                print_stats(file_size, status_codes)

        except (IndexError, ValueError):
            # Skip lines that don't match the expected format
            continue

except KeyboardInterrupt:
    # Handle Ctrl+C
    print_stats(file_size, status_codes)
    raise

# Print final stats
print_stats(file_size, status_codes)
