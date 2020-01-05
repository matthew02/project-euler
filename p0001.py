#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Project Euler Problem 1 - Multiples of 3 and 5

Sum all natural numbers below a given number which are multiples of 3 or 5.
https://projecteuler.net/problem=1

Usage:
    python3 p0001.py [number]
"""

import sys


def multiples_of_3_and_5(start: int, stop: int) -> int:
    """Sums all integers divisible by 3 and 5.

    Sum all integers which are in the closed interval from start to stop and
    are also divisible by 3 and 5.

    Args:
        start: The first number in the interval (inclusive).
        stop: The last number in the interval (inclusive).

    """
    sum = 0
    for number in range(start, stop):
        if not number % 3 or not number % 5:
            sum += number

    return sum

def main(num: int):
    """Prints the sum of all integers below num which are multiples of 3 or 5.

    Args:
        num: The upper limit of the range of numbers to sum.
    """
    print(multiples_of_3_and_5(0, num))

if __name__ == '__main__':
    main(int(sys.argv[1]))

