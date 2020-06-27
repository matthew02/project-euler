#!/usr/bin/env python3

"""Problem 15 from Project Euler: Lattice Paths

Determine the number of NE routes in an n x n grid.

Usage:
    python3 p015.py [num]
"""

import sys

from math import factorial


def lattice_paths(n: int) -> int:
    k = 2 * n
    return factorial(k) // (factorial(n) * factorial(k - n))

def euler15(num: int) -> int:
    """Calculates the number of NE routes in an n x n grid."""
    return lattice_paths(num)

def main(num: str) -> None:
    """Prints the solution."""
    print(f'The number of NE routes in a {num} x {num} grid is {euler15(int(num))}.')

if __name__ == '__main__':
    main(sys.argv[1])

