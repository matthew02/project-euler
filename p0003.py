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

from primes import decompose


def largest_prime_factor(num: int) -> int:
    """Finds the largest prime factor of a given number.

    Args:
        num: The number to be factored.

    Returns:
        The largest prime factor.
    """
    *_, largest = decompose(num)
    return largest

def main(num: int):
    """Prints the largest prime factor of a number.

    Args:
        num: The number to factor.
    """
    print(largest_prime_factor(num))

if __name__ == '__main__':
    main(int(sys.argv[1]))
