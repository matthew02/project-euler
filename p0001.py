#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Project Euler Problem 1 - Multiples of 3 and 5

Sum all natural numbers below a given number which are multiples of 3 or 5.
https://projecteuler.net/problem=1

Usage:
    python3 p0001.py [number]
"""

import sys

from typing import List


def multiples_of_3_and_5(start: int, stop: int) -> int:
    """Sums all integers divisible by 3 and 5 in the range start to stop."""
    numbers = set()
    numbers.update(get_all_divisible_by(start, stop, 3))
    numbers.update(get_all_divisible_by(start, stop, 5))
    return sum(list(numbers))

def get_all_divisible_by(start: int, stop: int, n: int) -> List[int]:
    """Gets all numbers between start and stop which are divisible by n."""
    while start % n:
        start += 1
    return range(start, stop, n)

def main(num: int):
    """Prints the solution."""
    print(multiples_of_3_and_5(0, num))

if __name__ == '__main__':
    main(int(sys.argv[1]))

