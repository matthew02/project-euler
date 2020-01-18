#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 11 from Project Euler: Largest product in a grid

Find the greatet product of n adjacent numbers in a grid in one direction,
up, down, left, right, diagonally.
https://projecteuler.net/problem=11

Usage:
    python3 p0010.py [filename] [number]
"""

import sys

from typing import List


def largest_product_in_a_grid(grid: List[List[int]], num: int) -> int:
    """Calculates the largest product of a sequence of num numbers in any
    direction in a given square or rectangular grid of numbers."""
    largest = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            prod = lambda dx, dy: product(grid, [x, y], [dx, dy], num)

            # Calculate the product in the horizontal direction
            largest = max([largest, prod(1, 0)])
    
            # Calculate the product in the vertical direction
            largest = max([largest, prod(0, 1)])
    
            # Calculate the product in the diagonal down direction
            largest = max([largest, prod(1, 1)])
    
            # Calculate the product in the diagonal up direction
            largest = max([largest, prod(1, -1)])
    
    return largest

def product(grid: List[List[int]], start: List[int], direction: List[int], num: int):
    """Calculate the product of a sequence of numbers in a grid.
    
    Args:
        grid: A square or rectangular two-dimensional list of numbers.
        start: The coordinates of the first number in the sequence.
        direction: A unit vector indicating the direction of the next numbers.
        num: The quantity of numbers to choose from the grid.
    
    Returns:
        The product of all numbers chosen from the grid or 0 if the movement
        would overflows the grid boundaries.
    """
    x, y = start
    height = len(grid) - 1
    width = len(grid[0]) - 1

    prod = 1

    for _ in range(num):
        prod *= grid[y][x]
        x += direction[0]
        y += direction[1]
        if x < 0 or x > width or y < 0 or y > width:
            return 0

    return prod

def load_grid_file(fname: str) -> List[List[int]]:
    """Loads the grid from a file."""
    with open (fname, 'r') as myfile:
        data = [[*map(int, line.split(' '))] for line in myfile]
    return data

def main(fname: str, num: int):
    """Prints the solution."""
    print(largest_product_in_a_grid(load_grid_file(fname), 4))

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
