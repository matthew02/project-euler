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


def generate_primes() -> Iterator[int]:
    """Generates the sequence of prime numbers."""
    num = 2
    yield num

    primes = set({2})

    while True:
        num += 1
        if num % 2 > 0 and all(num % prime > 0 for prime in primes):
            primes.add(num)
            yield num

def decompose(num: int) -> Iterator[int]:
    """Decomposes a number into its prime factors."""
    primes = generate_primes()

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

