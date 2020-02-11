#!/usr/bin/env python3

"""Problem 2 from Project Euler.

Sum all even numbers from the Fibonacci sequence below a given number.
https://projecteuler.net/problem=2

Usage:
    python3 p0002.py [number]
"""

import sys

from itertools import islice, takewhile
from typing import Iterator


def get_fibonacci() -> Iterator[int]:
    """Generates the sequence of Fibonacci numbers."""
    a, b = 0, 1

    while True:
        yield a
        b = a + b
        yield b
        a = a + b

def sum_even_fibonacci(stop: int) -> int:
    """Sums all even integers in the Fibonacci sequence up to stop."""
    every_third_fib = islice(get_fibonacci(), 3, None, 3)
    return sum(takewhile(lambda x: x < stop, every_third))

def main(num: int):
    """Prints the result."""
    print(sum_even_fibonacci(num))

if __name__ == '__main__':
    main(int(sys.argv[1]))
