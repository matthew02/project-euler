#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Project Euler Problem 4 - Largest palindrome product

Find the largest palindrome made from the product of two three-digit numbers.
https://projecteuler.net/problem=4

Usage:
    python3 p0004.py
"""

from typing import Iterator


def largest_palindrome_product() -> int:
    """Finds the largest palindromic product of two three-digit numbers."""
    return max(generate_palindromes())

def generate_palindromes() -> Iterator[int]:
    """Generates a list of palindromic numbers.

    Finds all numbers which are the product of two three-digit numbers and
    are palindromes.

    Yields:
        An iterator of all palindromes found.
    """
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if str(product) == str(product)[::-1]:
                yield product

def main():
    """Prints the solution."""
    print(largest_palindrome_product())

if __name__ == '__main__':
    main()
