#!/usr/bin/python3
"""Reads HTTP request logs through stdin line by line
    and prints statistics
    Usage: ./0-stats.py
"""

import sys


def print_stats(total_size, status_codes):
    """Prints the computed metrics"""
    print("File size: {}".format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

try:
    for i, line in enumerate(sys.stdin, 1):
        parts = line.split()
        if len(parts) < 7:
            continue
        status_code = parts[-2]
        file_size = parts[-1]
        if status_code in status_codes:
            status_codes[status_code] += 1
        try:
            total_size += int(file_size)
        except ValueError:
            continue
        if i % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

print_stats(total_size, status_codes)
