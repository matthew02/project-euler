#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 3 from Project Euler.

Find the largest prime factor of a given number.
https://projecteuler.net/problem=3

Usage:
    python3 p0003.py [number]
"""

import sys

def is_prime(num: int) -> bool:
    """Checks a number for primality."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    for divisor in range(3, int(num ** 0.5) + 1, 2):
        if num % divisor == 0:
            return False
    return True

def get_nth_prime(n: int) -> int:
    """Finds the nth prime number."""
    current, count = 2, 1
    while True:
        if count == n:
            return current
        count += 1

        while True:
            current += 1
            if is_prime(current):
                break

def main(num: int):
    """Prints the solution."""
    print(get_nth_prime(int(num)))

if __name__ == '__main__':
    main(int(sys.argv[1]))

