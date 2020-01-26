# -*- coding: utf-8 -*-

"""A library of helper functions for solving the problems at ProjectEuler.net"""

from functools import reduce
from itertools import islice
from operator import mul, add
from typing import Iterator, List


def decompose(num: int) -> Iterator[int]:
    """Decomposes a number into its prime factors."""
    prime, primes = 2, get_primes()

    while prime <= num:
        prime = next(primes)

        while num % prime == 0:
            yield prime
            num = num // prime

def get_primes() -> Iterator[int]:
    """Generates the prime number sequence."""
    yield 2
    prime_multiples = {}
    num = 3
    while True:
        if num not in prime_multiples:
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
    if num % 2 == 0:
        return False
    for divisor in range(3, sqrt(num) + 1, 2):
        if num % divisor == 0:
            return False
    return True

def nth(iterable: Iterator, n: int):
    """Returns the nth item of an iterator  or raise StopIteration."""
    return next(islice(iterable, n - 1, None))

def sqrt(n: int) -> float:
    """Gets the integer square root of an integer, rounded toward zero."""
    return int(n ** 0.5)
