#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Project Euler Problem 5: Smallest multiple

Find the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20.
https://projecteuler.net/problem=5

Usage:
    python3 p0005.py [number]
"""

import sys

from math import gcd
from typing import List

def smallest_multiple(numbers: List[int]) -> int:
    """Finds the smallest integer multiple of a list of numbers.

    Calculates the smallest number that is evenly divisible by all numbers in
    given list, also known as the least common multiple.
    """
    result = 1
    for num in numbers:
        result *= num // gcd(num, result)
    return result

def main(stop: int):
    """Prints the result."""
    print(smallest_multiple(range(1, int(stop) + 1)))

if __name__ == '__main__':
    main(int(sys.argv[1]))
