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
    palindromes = list()

    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if is_palindrome(product):
                palindromes.append(product)

    return max(palindromes)

def is_palindrome(num: int) -> bool:
    """Checks if a number is a palindrome."""
    return str(num) == str(num)[::-1]

def main():
    """Prints the solution."""
    print(largest_palindrome_product())

if __name__ == '__main__':
    main()
