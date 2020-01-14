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


def get_primes() -> Iterator[int]:
    """Generates the prime number sequence"""
    yield 2
    prime_multiples = {}
    num = 3
    while True:
        if num not in prime_multiples:
            yield num
            prime_multiples[num * num] = [2 * num]
        else:
            for multiple in prime_multiples[num]:
                prime_multiples.setdefault(multiple + num, []).append(multiple)
            del prime_multiples[num]
        num += 2

def decompose(num: int) -> Iterator[int]:
    """Decomposes a number into its prime factors."""
    prime, primes = 2, get_primes()

    while prime <= num:
        prime = next(primes)

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

