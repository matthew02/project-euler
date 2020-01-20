#!/usr/bin/env python3

"""Problem 7 from Project Euler.

Find the nth prime number.
https://projecteuler.net/problem=7

Usage:
    python3 p0007.py [number]
"""

import sys

from itertools import islice
from typing import Iterator

from euler import get_primes


def nth(iterable: Iterator, n: int):
    """Returns the nth item or raise StopIteration."""
    return next(islice(iterable, n - 1, None))

def main(num: int):
    """Prints the solution."""
    print(nth(get_primes(), num))

if __name__ == '__main__':
    main(int(sys.argv[1]))

