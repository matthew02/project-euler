#!/usr/bin/env python3

"""Problem 12 from Project Euler: Highly divisible triangular number

Find the first triangle number to have over five hundred divisors.

Usage:
    python3 p0012.py [number]
"""

import itertools
import sys


from collections import Counter as counter
from itertools import accumulate, count
from math import prod
from typing import Iterator

from euler import decompose


def count_factors(num: int) -> int:
    """Calculates the total number of factors for a given integer."""
    exponents = counter(decompose(num)).values()
    return prod(e + 1 for e in exponents)

def triangle_numbers() -> Iterator:
    """Generates the sequence of triangle numbers."""
    return accumulate(count())

def euler12(num: int) -> int:
    """Calculates the first triangle number to have more than num divisors."""
    for t in triangle_numbers():
        if count_factors(t) > num:
            return t

def main(num: str):
    """Prints the solution."""
    print(euler12(int(num)))

if __name__ == '__main__':
    main(sys.argv[1])
