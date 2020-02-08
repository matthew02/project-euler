#!/usr/bin/env python3

"""Problem 12 from Project Euler: Highly divisible triangular number

Find the first triangle number to have over five hundred divisors.

Usage:
    python3 p0012.py [number]
"""

import sys

from collections import Counter as counter
from math import prod
from itertools import accumulate, dropwhile, count
from typing import Iterator

from euler import decompose, get_primes


def count_factors(num: int) -> int:
    """Calculates the total number of factors for a given integer."""
    if not isinstance(num, int) or num < 1:
        raise ValueError
    if num == 1:
        return 1
    exponents = counter(decompose(num)).values()
    return prod(e + 1 for e in exponents)

def get_triangle_numbers() -> Iterator[int]:
    """Generates the sequence of triangle numbers."""
    return accumulate(count(1))

def euler12(num: int) -> int:
    """Calculates the first triangle number to have more than num divisors."""
    # Warm up the prime number generator here.
    # This eliminates a lot of future context switching between the decompose
    # and get_primes functions and cuts our execution time in half.
    primes = get_primes()
    for _ in range(num * 2):
        trash = next(primes)

    test = lambda n: count_factors(n) < num
    return next(dropwhile(test, get_triangle_numbers()))

def main(num: str) -> None:
    """Prints the solution."""
    print(f'The first triangle number to have more than {num} divisors is {euler12(int(num))}')

if __name__ == '__main__':
    main(sys.argv[1])

