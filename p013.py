#!/usr/bin/env python3

"""Problem 13 from Project Euler: Large sum

Calculate the first n digits of the sum of a list of numbers.
https://projecteuler.net/problem=13

Usage:
    python3 p013.py [filename] [number]
"""

import sys

from typing import List


def euler13(numbers: List[int], count: int) -> str:
    """Calculates the sum of numbers and returns the first count digits."""
    return str(sum(numbers))[:10]

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        numbers = [int(n or 0) for n in f.read().split('\n')]
    count = sys.argv[2]
    solution = euler13(numbers, count)
    print(f'The first {count} digits in the sum of the given list of numbers '
          f'is {solution}.')

