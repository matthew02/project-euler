#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 8 from Project Euler.

Find the n adjacent digits in the given number that have the greatest product.

https://projecteuler.net/problem=8

Usage:
    python3 p0008.py [filename] [number]

    [filename] points to a file containing the numerical sequence with or
    without newline characters
"""

import sys

from typing import List

import euler


def largest_product_in_a_series(sequence: List[int], n: int) -> int:
    """Finds the largest product of n consecutive numbers in sequence."""
    largest = 0
    for start in range(len(sequence) - n):
        stop = start + n
        largest = max(largest, product(sequence[start:stop]))
    return largest

def main(fname: str, length: int):
    """Prints the solution."""
    with open (fname, 'r') as myfile:
        data = [*map(int, myfile.read().replace('\n', ''))]
    print(largest_product_in_a_series(data, length))

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))

