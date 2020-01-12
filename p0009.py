#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 9 from Project Euler: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
a^2 + b^2 = c^2

Find a Pythagorean triplet for which a + b + c is equal to a given number n
and return the product abc.
https://projecteuler.net/problem=7

Usage:
    python3 p0009.py [number]
"""

import sys

from typing import Iterator, List

from euler import *


def special_pythagorean_triplet(n: int) -> List[int]:
    """Finds a Pythagorean triplet whose sum is equal to n."""
    for a, b, c in get_dicksons_triplets(n):
        if a + b + c == n:
            return [a, b, c]

def get_dicksons_triplets(stop: int) -> Iterator[List[int]]:
    """Generates Pythagorean triplets.

    Uses Dickson's method, for all values of r from 1 to stop.

    To find integer solutions to a^2 + b^2 = c^2...
    Take positive integers r, s, and t, where r^2 = 2st is a perfect square...
    Then a = r + s, b = r + t, c = r + s + t

    https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#Dickson's_method
    """
    for r in range(1, stop):
        for s, t in get_factor_pairs(r ** 2 // 2):
            yield [r + s, r + t, r + s + t]

def main(num: int):
    """Prints the solution."""
    triplet = special_pythagorean_triplet(num)
    if triplet == None:
        print('None found.')
    else:
        #print(triplet)
        print(product(triplet))

if __name__ == '__main__':
    main(int(sys.argv[1]))

