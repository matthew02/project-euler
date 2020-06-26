#!/usr/bin/env python3

"""Problem 14 from Project Euler: Longes Collatz Sequence

Find the largest Collatz sequence under one million.

Usage:
    python3 p0014.py [number]
"""

import sys


cache = {1: 0}

def collatz_sequence_length(num: int) -> int:
    if num not in cache:
        if num % 2 == 0:
            cache[num] = 1 + collatz_sequence_length(num // 2)
        else:
            cache[num] = 1 + collatz_sequence_length(3 * num + 1)

    return cache[num]

def euler14(num: int) -> int:
    """Calculates the largest Collatz sequence under num."""
    longest = 1, 1

    for i in range(num // 2, num):
        c = collatz_sequence_length(i)
        if c > longest[1]:
            longest = i, c

    return longest

def main(num: str) -> None:
    """Prints the solution."""
    collatz = euler14(int(num))
    print(f'The longest Collatz sequence under {num} is {collatz[0]} with a length of {collatz[1]}')

if __name__ == '__main__':
    main(sys.argv[1])

