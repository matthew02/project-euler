#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Project Euler Problem 5: Smallest multiple

Find the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20.
https://projecteuler.net/problem=5

Usage:
    python3 p0005.py
"""

import math
import sys

from typing import List

from primes import decompose

def smallest_multiple(numbers: List) -> int:
    """Finds the smallest integer multiple of a list of numbers.

    Calculates the smallest number that is evenly divisible by all numbers in
    given list, also known as the least common multiple.

    Args:
        numbers: The list of numbers to compute.

    Returns:
        The least common multiple.
    """
    result = 1
    for num in numbers:
        result *= num // math.gcd(num, result)
    return result

def main(stop: int):
    """Prints the smallest common factor in a sequence of numbers.

    Prints the smallest common factor in a sequence of numbers from one to
    stop.

    Args:
        stop: The upper bound of the sequence.
    """
    print(smallest_multiple([*range(1, stop)]))

if __name__ == '__main__':
    main(int(sys.argv[1]))
