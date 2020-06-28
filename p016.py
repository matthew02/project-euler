#!/usr/bin/env python3

"""Problem 16 from Project Euler: Power Digit Sum

Calculate the sum of the digits of some power of 2.

Usage:
    python3 p016.py [num]
"""

import sys


def euler16(num: int) -> int:
    """Calculates the sum of the digits of 2 to the power of num."""
    return sum([int(digit) for digit in str(2 ** num)])

def main(num: str) -> None:
    """Prints the solution."""
    print(f'The sum of the digits of 2 to the power of {num} is {euler16(int(num))}.')

if __name__ == '__main__':
    main(sys.argv[1])

