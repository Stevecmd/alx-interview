#!/usr/bin/python3
"""Reads HTTP request logs through stdin line by line
    and prints statistics
    Usage: ./0-stats.py
"""

import sys


def print_stats(total_size, status_codes):
    """Prints the computed metrics"""
    print("File size: {}".format(total_size))
    for key in sorted(status.keys()):
        if status[key] > 0:
            print("{}: {}".format(key, status[key]))


split = []
total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}

try:
    for i, line in enumerate(sys.stdin, 1):
        split = line.split(" ")
        if len(split) < 2:
            continue
        if split[-2] in status:
            status[split[-2]] = status[split[-2]] + 1
        file_size = file_size + eval(split[-1])
        if i % 10 == 0:
            print("File size: {}".format(file_size))
            for key in sorted(status.keys()):
                if status[key] > 0:
                    print("{}: {}".format(key, status[key]))

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

print_stats(total_size, status_codes)
