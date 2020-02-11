#!/usr/bin/env python3

"""Problem 11 from Project Euler: Largest product in a grid

Find the greatet product of n adjacent numbers in a grid in one direction,
up, down, left, right, diagonally.
https://projecteuler.net/problem=11

Usage:
    python3 p0011.py [filename] [number]
"""

import numpy
import sys

from itertools import count, islice
from math import prod
from typing import List, Tuple


def largest_product_in_a_grid(grid: List[List[int]], num: int) -> int:
    """Calculates the largest product of a sequence of num numbers in any
    direction in a given square or rectangular grid of numbers."""
    largest = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            product = lambda dx, dy: grid_product(grid, (x, y), (dx, dy), num)
            largest = max([largest,
                           product(1, 0),      # Horizontal
                           product(0, 1),      # Vertical
                           product(1, 1),      # Diagonal down
                           product(1, -1)])    # Diagonal up

    return largest

def grid_product(grid: List[List[int]], start: Tuple[int], direction: Tuple[int], num: int) -> int:
    """Calculate the product of a sequence of numbers in a grid.

    Args:
        grid: A square or rectangular two-dimensional list of numbers.
        start: The coordinates of the first number in the sequence.
        direction: A vector indicating the direction of the subsequent numbers.
        num: The quantity of numbers to choose from the grid.

    Returns:
        The product of all numbers chosen from the grid or 0 if the movement
        would overflow the grid boundaries.
    """
    x, y = start
    dx, dy = direction

    try:
        # Ensure the sequence doesn't start or end below a zero index
        if x < 0 or y < 0 or x + num * dx < 0 or y + num * dy < 0:
            raise IndexError

        return prod(grid[y + dy * i][x + dx * i] for i in range(num))

    except IndexError:
        return 0

def main(fname: str, num: int):
    """Prints the solution."""
    grid = numpy.loadtxt(fname, int, '#', ' ')
    print(largest_product_in_a_grid(grid, num))

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
