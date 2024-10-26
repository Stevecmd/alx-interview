#!/usr/bin/python3
"""Reads HTTP request logs through stdin line by line and prints statistics
Usage: ./0-stats.py
"""

import sys


def print_stats(stats, total_file_size):
    """Prints statistics of HTTP request logs.

    Args:
        stats (dict): A dictionary with HTTP status codes as keys and
            their respective counts as values.
        file_size (int): The total size of the log file in bytes.
    """
    print("File size: {:d}".format(total_file_size))
    for status_code, count in sorted(stats.items()):
        if count:
            print("{}: {}".format(status_code, count))


total_file_size = 0
line_count = 0
stats = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        data = data[::-1]

        try:
            total_file_size += int(data[0])
        except (IndexError, ValueError):
            pass

        try:
            code = data[1]
            if code in stats:
                stats[code] += 1
        except IndexError:
            pass

        if line_count % 10 == 0:
            print_msg(stats, total_file_size)
            line_count = 0

    print_stats(stats, total_file_size)

except KeyboardInterrupt:
    print_stats(stats, total_file_size)
    raise
