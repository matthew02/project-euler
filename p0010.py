#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 10 from Project Euler: Summation of primes

Find the sum of all the prime numbers below a given number.
https://projecteuler.net/problem=10

Usage:
    python3 p0010.py [number]
"""

import sys

from itertools import takewhile

from euler import get_primes


def main(num: int):
    """Prints the solution."""
    return sum(takewhile(lambda x: x < num, get_primes()))

if __name__ == '__main__':
    main(int(sys.argv[1]))

