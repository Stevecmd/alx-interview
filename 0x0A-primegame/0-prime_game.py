#!/usr/bin/python3
"""
This module contains a function that determines
the winner of a game based on the strategic removal
of prime numbers and their multiples from a set of consecutive integers.
"""


def isWinner(x, nums):
    """
    Returns the winner of the game or None if there is no winner.
    """
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    def is_prime(n):
        """Returns True if n is a prime number, else False."""
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes_up_to(n):
        """Returns a list of prime numbers up to n (inclusive)."""
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    for n in nums:
        primes = get_primes_up_to(n)
        if not primes:
            ben_wins += 1
            continue

        turn = 0  # 0 for Maria, 1 for Ben
        while primes:
            prime = primes.pop(0)
            primes = [p for p in primes if p % prime != 0]
            turn = 1 - turn

        if turn == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
