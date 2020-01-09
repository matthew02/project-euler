#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    palindromes = list()

    start = 10 ** (n - 1)
    stop = 10 ** n
    for i in range(start, 2000):
        for j in range(i, 2000):
            product = i * j
            if is_palindrome(product):
                palindromes.append(product)

    return max(palindromes)

def is_palindrome(num: int) -> bool:
    """Checks if a number is a palindrome."""
    return str(num) == str(num)[::-1]

def main(num: int):
    """Prints the solution."""
    print(largest_palindrome_product(int(num)))

if __name__ == '__main__':
    main(sys.argv[1])
