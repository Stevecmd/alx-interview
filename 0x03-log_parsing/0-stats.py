#!/usr/bin/python3
"""Reads HTTP request logs through stdin line by line and prints statistics
Usage: ./0-stats.py
"""

import sys


if __name__ == '__main__':

    # Variable initialization
    total_file_size, line_count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {code: 0 for code in status_codes}

    def print_stats(stats: dict, total_file_size: int) -> None:
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

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                total_file_size += int(data[-1])
            except BaseException:
                pass
            if line_count % 10 == 0:
                print_stats(stats, total_file_size)
        print_stats(stats, total_file_size)
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(stats, total_file_size)
