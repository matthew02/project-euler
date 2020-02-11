#!/usr/bin/env python3

"""Project Euler Problem 4 - Largest palindrome product

Find the largest palindrome made from the product of two three-digit numbers.
https://projecteuler.net/problem=4

Usage:
    python3 p0004.py
"""

import sys

from typing import Iterator


def largest_palindrome_product(n: int) -> int:
    """Finds the largest palindromic product of two n-digit numbers."""
    largest = 0

    start = 10 ** (n - 1)
    stop = 10 ** n
    for i in range(stop, start, -1):
        for j in range(i, start, -1):
            product = i * j
            if product > largest and is_palindrome(product):
                largest = product

    return largest

def is_palindrome(num: int) -> bool:
    """Checks if a number is a palindrome."""
    return str(num) == str(num)[::-1]

def main(num: int):
    """Prints the solution."""
    print(largest_palindrome_product(num))

if __name__ == '__main__':
    main(int(sys.argv[1]))
