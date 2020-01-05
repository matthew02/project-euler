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

def generate_fibonacci_sequence(stop: int) -> Iterator[int]:
    """Generates the sequence of Fibonacci numbers.

    Calculates the Fibonacci numbers below the stop value.

    Args:
        stop: The upper limit of numbers in the sequence.

    Yields:
        An iterator of all Fibonacci numbers calculated.
    """
    previous = 0
    current = 1

    while current < stop:
        yield current
        [previous, current] = [current, previous + current]

def sum_even_fibonacci(stop: int) -> int:
    """Sums all even integers in the Fibonacci sequence.

    Sums all even numbers from the Fibonacci sequence which are below the
    stop value.

    Args:
        stop: The upper limit of Fibonacci numbers at which to stop summing.

    Returns:
        The calculated sum.
    """
    sequence = generate_fibonacci_sequence(stop)
    return sum(num for num in sequence if not num % 2)

def main(num: int):
    """Prints the sums of all even numbers in the Fibonacci sequence below num.

    Args:
        num: The upper limit of fibonacci numbers at which to stop summing.
    """
    print(sum_even_fibonacci(num))

if __name__ == '__main__':
    main(int(sys.argv[1]))

