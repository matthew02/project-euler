# -*- coding: utf-8 -*-

"""A library of helper functions for solving the problems at ProjectEuler.net"""

from functools import reduce
from operator import mul, add
from typing import Iterator, List

def get_factor_pairs(x: int) -> Iterator[List[int]]:
    """Generates a the factor pairs of an integer."""
    stop = int(sqrt(x)) + 1
    for i in range(1, stop):
        if x % i == 0:
            yield [i, x // i]

def product(numbers: List[int]) -> int:
    return reduce(mul, numbers, 1)

def sqrt(n: int) -> float:
    """Gets the square root of an integer."""
    return n ** 0.5
