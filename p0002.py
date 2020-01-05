#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 2 from Project Euler.

Sum all even numbers below some number X in the Fibonacci sequence.
https://projecteuler.net/problem=2

Usage:
    python3 p0002.py [number]
"""

import sys


def sum_even_fibonacci(stop: int) -> int:
    """Sums all even integers in the Fibonacci sequence.

    Sum all even integers from the Fibonacci sequence which are below the
    stop value.

    Args:
        stop: The upper limit of Fibonacci numbers at which to stop summing.
    """
    sum = 0
    previous = 0
    current = 1

    while current < stop:
        if not current % 2:
            sum += current
        [previous, current] = [current, previous + current]

    return sum

def main(num: int):
    """Sums all even integers in the Fibonacci sequence below num.

    Args:
        num: The upper limit of fibonacci numbers at which to stop summing.
    """
    print(sum_even_fibonacci(num))

if __name__ == '__main__':
    main(int(sys.argv[1]))

