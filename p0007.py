#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 7 from Project Euler.

Find the nth prime number.
https://projecteuler.net/problem=7

Usage:
    python3 p0007.py [number]
"""

import sys

from itertools import islice

from euler import *


def get_nth_prime(n: int) -> int:
    """Returns the nth prime number"""
    return nth(get_primes(), n)

def nth(iterable: Iterator, n: int):
    """Returns the nth item or raise StopIteration."""
    return next(islice(iterable, n - 1, None))

def main(num: int):
    """Prints the solution."""
    print(get_nth_prime(num))

if __name__ == '__main__':
    main(int(sys.argv[1]))

