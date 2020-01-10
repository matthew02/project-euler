#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem 7 from Project Euler.

Find the nth prime number.
https://projecteuler.net/problem=7

Usage:
    python3 p0007.py [number]
"""

import sys

from numpy import gcd
from typing import List


def special_pythagorean_triplet(n: int) -> List:
    """Finds a pythagorean triplet whose numbers sum to n."""
    n2 = n / 2
    stop = int(n2 ** 0.5 - 1)
    for m in range(2, stop):
        if n2 % m == 0:
            nm = n2 // m
            while nm % 2 == 0:
                nm //= 2
            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1
            while k < 2 * m and k <= nm:
                if nm % k == 0 and gcd(k, m) == 1:
                    d = n2 // (k * m)
                    n = k - m
                    a = d * (m ** 2 - n ** 2)
                    b = 2 * d * m * n
                    c = d * (m ** 2 + n ** 2)
                    return([a, b, c])
                k += 1

    for x in range(1, n):
        for y in range(1, n):
            z = (x ** 2 + y ** 2) ** 0.5
            if sum([x, y, z]) == n:
                return [x, y, z]

def special_pythagorean_triplet_old(n: int) -> List:
    """Finds a pythagorean triplet whose numbers sum to n."""
    for x in range(1, n):
        for y in range(1, n):
            z = (x ** 2 + y ** 2) ** 0.5
            if sum([x, y, z]) == n:
                return [x, y, z]

def special_pythagorean_triplet_x(n: int) -> List:
    """Finds a pythagorean triplet whose numbers sum to n."""
    a = 3
    while True:
        b = (a ** 2 + 1) / 2 - 1
        c = b + 1
        s = sum([a, b, c])
        print(f'a = {a}, b = {b}, c = {c}')
        if s == n:
            return [a, b, c]
        if s > n:
            return None
        a += 2

def main(num: int):
    """Prints the solution."""
    triplet = special_pythagorean_triplet(num)
    if triplet is None:
        print('None found.')
    else:
        print(triplet[0] * triplet[1] * triplet[2])

if __name__ == '__main__':
    main(int(sys.argv[1]))

