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
    """Sums all integers divisible by 3 and 5 in the range start to stop."""
    sum = 0
    for num in range(start, stop):
        if not num % 3 or not num % 5:
            sum += num

    return sum

def main(num: int):
    """Prints the solution."""
    print(multiples_of_3_and_5(0, num))

if __name__ == '__main__':
    main(int(sys.argv[1]))

