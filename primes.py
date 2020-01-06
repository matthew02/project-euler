# -*- coding: utf-8 -*-

"""Functions for working with prime numbers."""

import math

from typing import Iterator


def generate_primes(stop: int) -> Iterator[int]:
    """Generates a sequence of prime numbers up to stop.

    Args:
        stop: The largest number to check for prime.

    Yields:
        An iterator of all primes found.
    """
    primes = set()
    for num in range(2, stop + 1):
        if all(num % prime > 0 for prime in primes):
            primes.add(num)
            yield num

def decompose(num: int) -> Iterator[int]:
    """Decomposes a number into its prime factors.

    Args:
        num: The number to decompose.

    Yields:
        An iterator of all prime factors.
    """
    primes = generate_primes(num)

    for prime in primes:
        if prime > num:
            break

        while num % prime == 0:
            yield prime
            num = num // prime

