#!/usr/bin/python3
"""
Script that reads  HTTP request logs from stdin line by line.
compute metrics, and print statistics after every 10 lines
or upon a keyboard interruption (CTRL + C).
The statistics include the total file size
and the number of lines by status code
Usage: ./0-stats.py
"""

import sys
import re


def parse_log_line(input_line):
    '''Parses a given HTTP request log line.

    Args:
        input_line (str): The line of input from which to parse the metrics.

    Returns:
        dict: The parsed metrics.
    '''
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_stats(stats, total_file_size):
    '''Prints the metrics from a given HTTP request log.

    Args:
        stats (dict): The metrics to print.
        total_file_size (int): The total file size.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(stats.keys()):
        count = stats.get(status_code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count), flush=True)


def update_stats(line, total_file_size, stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    line_info = parse_log_line(line)
    status_code = line_info.get('status_code', '0')
    if status_code in stats.keys():
        stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    '''Starts the log parser.
    '''
    line_count = 0
    total_file_size = 0
    stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            total_file_size = update_stats(line, total_file_size, stats)
            line_count += 1
            if line_count % 10 == 0:
                print_stats(stats, total_file_size)
    except (KeyboardInterrupt, EOFError):
        print_stats(stats, total_file_size)


if __name__ == '__main__':
    run()
