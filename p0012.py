#!/usr/bin/env python3

"""Problem 12 from Project Euler: Highly divisible triangular number

Find the first triangle number to have over five hundred divisors.

Usage:
    python3 p0012.py [number]
"""

import sys

from collections import Counter as counter
from math import prod
from itertools import dropwhile, accumulate, count
from typing import Iterator

from euler import decompose, get_primes


def count_factors(num: int) -> int:
    """Calculates the total number of factors for a given integer."""
    exponents = counter(decompose(num)).values()
    return prod(e + 1 for e in exponents)

def get_triangle_numbers(n: int=1) -> Iterator[int]:
    """Generates the sequence of triangle numbers starting with the nth."""
    return accumulate(count())

def euler12(num: int) -> int:
    """Calculates the first triangle number to have more than num divisors."""
    primes = get_primes()
    for _ in range(1000):
        trash = next(primes)

    test = lambda n: count_factors(n) < num
    return next(dropwhile(test, get_triangle_numbers()))

def main(num: str):
    """Prints the solution."""
    print(euler12(int(num)))

if __name__ == '__main__':
    main(sys.argv[1])
