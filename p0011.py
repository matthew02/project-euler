#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 11 from Project Euler: Largest product in a grid

Find the greatet product of n adjacent numbers in a grid in one direction,
up, down, left, right, diagonally.
https://projecteuler.net/problem=11

Usage:
    python3 p0011.py [filename] [number]
"""

import numpy
import operator
import sys

from functools import reduce
from itertools import accumulate, count, islice, repeat, takewhile
from math import prod
from typing import List


def largest_product_in_a_grid(grid: List[List[int]], num: int) -> int:
    """Calculates the largest product of a sequence of num numbers in any
    direction in a given square or rectangular grid of numbers."""
    largest = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            prod = lambda dx, dy: product(grid, [x, y], [dx, dy], num)
            largest = max([largest,
                           prod(1, 0),      # Horizontal
                           prod(0, 1),      # Vertical
                           prod(1, 1),      # Diagonal down
                           prod(1, -1)])    # Diagonal up

    return largest

def product(grid: List[List[int]], start: List[int], direction: List[int], num: int) -> int:
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

    w, h = len(grid[0]) - 1, len(grid) - 1
    end_x, end_y = x + num * direction[0], y + num * direction[1]
    if x < 0 or end_x < 0 or x > w or end_x > w or\
       y < 0 or end_y < 0 or y > h or end_y > h:
        return 0

    #prod = 1
    #dx, dy = direction
    #for _ in range(num):
    #    prod *= grid[y][x]
    #    x += dx
    #    y += dy
    #return prod

    dx, dy = direction
    return product(grid[y + dy * i][x + dx * i] for i in range(num))

    #x_coords = islice(count(x, direction[0]), 0, num)
    #y_coords = islice(count(y, direction[1]), 0, num)
    #return prod(grid[dy][dx] for dx, dy in zip(x_coords, y_coords))

def main(fname: str, num: int):
    """Prints the solution."""
    grid = numpy.loadtxt(fname, int, '#', ' ')
    print(largest_product_in_a_grid(grid, num))

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
