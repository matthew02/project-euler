# -*- coding: utf-8 -*-

"""A library of helper functions for solving the problems at ProjectEuler.net"""

from functools import reduce
from operator import mul, add
from typing import Iterator, List


def product(numbers: List[int]) -> int:
    """Gets the product of all numbers in a list."""
    return reduce(mul, numbers, 1)

def sqrt(n: int) -> float:
    """Gets the integer square root of an integer, rounded toward zero."""
    return int(n ** 0.5)
