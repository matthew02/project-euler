"""A library of helper functions for solving the problems at ProjectEuler.net"""

from collections import Counter as counter
from math import prod
from itertools import islice
from typing import Any, Dict, Iterator, List


_prime_number_cache: List[int] = [2, 3]
_prime_multiples: Dict[int, List[int]] = {}


def count_factors(num: int) -> int:
    """Calculates the total number of factors for a given integer."""
    if not isinstance(num, int) or num < 1:
        raise ValueError
    if num == 1:
        return 1
    exponents = counter(decompose(num)).values()
    return prod(e + 1 for e in exponents)

def decompose(num: int) -> List[int]:
    """Decomposes a number into its prime factors."""
    if not isinstance(num, int) or num < 2:
        raise ValueError
    factors = []
    for prime in get_primes():
        if prime > num: break
        while num % prime == 0:
            factors.append(prime)
            num //= prime
    return factors

def get_primes() -> Iterator[int]:
    """Generates the prime number sequence."""
    yield from _prime_number_cache
    candidate = _prime_number_cache[-1]
    while True:
        if candidate not in _prime_multiples:
            _prime_multiples[candidate * candidate] = [2 * candidate]
            _prime_number_cache.append(candidate)
            yield candidate
        else:
            for m in _prime_multiples[candidate]:
                _prime_multiples.setdefault(m + candidate, []).append(m)
            del _prime_multiples[candidate]
        candidate += 2

def is_prime(num: int) -> bool:
    """Checks a number for primality."""
    if not isinstance(num, int):
        raise ValueError
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

def nth(iterable: Iterator[Any], n: int) -> Any:
    """Returns the nth item of an iterator or raises StopIteration."""
    return next(islice(iterable, n - 1, None))

def sqrt(n: int) -> int:
    """Gets the integer square root of an integer rounded toward zero."""
    return int(n ** 0.5)

