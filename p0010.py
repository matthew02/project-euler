#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 10 from Project Euler: Summation of primes

Find the sum of all the prime numbers below a given number.
https://projecteuler.net/problem=10

Usage:
    python3 p0010.py [number]
"""

import sys

from euler import *


def summation_of_primes(stop: int) -> int:
    return sum(p for p in range(2, stop) if is_prime(p))

def main(num: int):
    """Prints the solution."""
    print(summation_of_primes(num))

if __name__ == '__main__':
    main(int(sys.argv[1]))

