#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 2 from Project Euler.

Sum all even numbers from the Fibonacci sequence below a given number.
https://projecteuler.net/problem=2

Usage:
    python3 p0002.py [number]
"""

import sys

from typing import Iterator

def generate_fibonacci_sequence() -> Iterator[int]:
    """Generates the sequence of Fibonacci numbers."""
    a, b = 0, 1

    while True:
        yield a
        b = a + b
        yield b
        a = a + b

def sum_even_fibonacci(stop: int) -> int:
    """Sums all even integers in the Fibonacci sequence up to stop."""
    result, current = 0, 0

    fib = generate_fibonacci_sequence()

    while current < stop:
        result += current
        current = next(fib)
        # Only every third number is even, so skip two
        next(fib)
        next(fib)
    return result

def main(num: int):
    """Prints the result."""
    print(sum_even_fibonacci(num))

if __name__ == '__main__':
    main(int(sys.argv[1]))

