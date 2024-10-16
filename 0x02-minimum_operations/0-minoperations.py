#!/usr/bin/python3
"""
Calculates the minimum number of operations to achieve
a given number of characters using only “Copy All”
and “Paste” operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    in order to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
