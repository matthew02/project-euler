#!/usr/bin/env python3

"""Project Euler Problem 6: Sum square difference

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
https://projecteuler.net/problem=6

Usage:
    python3 p0006.py
"""

import sys


def sum_first_n(n: int) -> int:
    """Finds the sum of the integers from 1 to n."""
    return n * (n + 1) // 2

def sum_first_n_squares(n: int) -> int:
    """Finds the sum of the squares of the integers from 1 to n."""
    return n * (n + 1) * (2 * n + 1) // 6

def sum_square_difference(n: int) -> int:
    """Finds the difference of the sum of the squares of the first n numbers
    and the square of the sum of the first n numbers."""
    return sum_first_n(n) ** 2 - sum_first_n_squares(n)

def main(n: int):
    """Prints the solution."""
    print(sum_square_difference(n))

if __name__ == '__main__':
    main(int(sys.argv[1]))
