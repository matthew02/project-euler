# -*- coding: utf-8 -*-

"""A library of helper functions for solving the problems at ProjectEuler.net"""

import math

from functools import reduce
from itertools import islice, takewhile
from operator import mul, add
from typing import Iterator, List


def decompose(num: int) -> List[int]:
    """Decomposes a number into its prime factors."""
    factors = []

    primes = get_primes()
    while (prime:= next(primes)) <= num:
        while num % prime == 0:
            factors.append(prime)
            num //= prime

    return factors

def get_primes(cache=[2]) -> Iterator[int]:
    """Generates the prime number sequence."""
    yield from cache
    prime_multiples = {}
    num = 3
    while True:
        if num not in prime_multiples:
            cache.append(num)
            yield num
            prime_multiples[num * num] = [2 * num]
        else:
            for multiple in prime_multiples[num]:
                prime_multiples.setdefault(multiple + num, []).append(multiple)
            del prime_multiples[num]
        num += 2

def is_prime(num: int) -> bool:
    """Checks a number for primality."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False
    for divisor in range(7, sqrt(num) + 1, 6):
        if num % divisor == 0:
            return False
    return True

def nth(iterable: Iterator, n: int):
    """Returns the nth item of an iterator or raises StopIteration."""
    return next(islice(iterable, n - 1, None))

def solve_quadratic(a: int, b: int, c: int) -> List[int]:
    d = (b**2) - (4*a*c)
    sol_1 = (-b-(0.5**d))/(2*a)
    sol_2 = (-b+(0.5**d))/(2*a)
    return (sol_1, sol_2)

    #d = (b**2) - (4 * a * c)
    #return [(-b - (0.5**d)) / (2 * a)
    #        (-b + (0.5**d)) / (2 * a)]
    #return [(-b - math.sqrt(d)) / (2 * a),
    #        (-b + math.sqrt(d)) / (2 * a)]

def sqrt(n: int) -> float:
    """Gets the integer square root of an integer rounded toward zero."""
    return int(n ** 0.5)

