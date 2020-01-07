#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 3 from Project Euler.

Find the largest prime factor of a given number.
https://projecteuler.net/problem=3

Usage:
    python3 p0003.py [number]
"""

import sys

from typing import Iterator


def generate_primes(stop: int) -> Iterator[int]:
    """Generates a sequence of prime numbers up to stop."""
    primes = set()
    for num in range(2, stop + 1):
        if all(num % prime > 0 for prime in primes):
            primes.add(num)
            yield num

def decompose(num: int) -> Iterator[int]:
    """Decomposes a number into its prime factors."""
    primes = generate_primes(num)

    for prime in primes:
        if prime > num:
            break

        while num % prime == 0:
            yield prime
            num = num // prime

def largest_prime_factor(num: int) -> int:
    """Finds the largest prime factor of a given number."""
    *_, largest = decompose(num)
    return largest

def main(num: int):
    """Prints the solution."""
    print(largest_prime_factor(num))

if __name__ == '__main__':
    main(int(sys.argv[1]))

