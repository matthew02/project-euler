# -*- coding: utf-8 -*-

"""A library of helper functions for solving the problems at ProjectEuler.net"""

from functools import reduce
from operator import mul, add
from typing import Iterator, List


def get_primes() -> Iterator[int]:
    """Generates the sequence of prime numbers."""
    num = 2
    yield num

    primes = set({2})

    while True:
        num += 1
        if num % 2 > 0 and all(num % prime > 0 for prime in primes):
            primes.add(num)
            yield num

def is_prime(num: int) -> bool:
    """Checks a number for primality."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    for divisor in range(3, sqrt(num) + 1, 2):
        if num % divisor == 0:
            return False
    return True

def product(numbers: List[int]) -> int:
    """Gets the product of all numbers in a list."""
    return reduce(mul, numbers, 1)

def sqrt(n: int) -> float:
    """Gets the integer square root of an integer, rounded toward zero."""
    return int(n ** 0.5)
