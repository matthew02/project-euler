#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 3 from Project Euler.

Find the largest prime factor of a given number.
https://projecteuler.net/problem=3

Usage:
    python3 p0003.py [number]
"""

import sys

from math import sqrt
from typing import Iterator


def largest_prime_factor(num: int) -> int:
    """Finds the largest prime factor of a given number.

    Args:
        num: The number to be factored.

    Returns:
        The largest prime factor.
    """
    largest_prime = 0

    stop = int(sqrt(num)) + 1
    primes = generate_prime_numbers(0, stop)

    for prime in primes:
        if num % prime == 0:
            largest_prime = prime

    return largest_prime

def generate_prime_numbers(start: int, stop: int) -> Iterator[int]:
    """Generates a list of prime numbers.

    Finds all prime numbers in the closed interval from start to stop using
    the Sieve of Eratosthenes algorithm.
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    Args:
        start: The lower bound of the interval to search for primes.
        stop: The upper bound of the interval to search for primes.

    Yields:
        An iterator of all primes found.
    """
    is_prime = [True for i in range(stop + 1)]

    num = 2
    while(num * num <= stop):
        if (is_prime[num]):
            for multiple in range(num * 2, stop, num):
                is_prime[multiple] = False
        num += 1

    for num in range(2, stop + 1):
        if num >= start and is_prime[num]:
            yield num

def main(num: int):
    """Prints the largest prime factor of a number.

    Args:
        num: The number to factor.
    """
    print(largest_prime_factor(num))

if __name__ == '__main__':
    main(int(sys.argv[1]))
