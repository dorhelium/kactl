"""
Author: Håkan Terelius
Date: 2009-08-26
License: CC0
Source: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
Description: Prime sieve for generating all primes up to a certain limit. is_prime[i] is True iff i is a prime.
Time: lim=100'000'000 ≈ 0.8 s. Runs 30% faster if only odd indices are stored.
Status: Tested
"""

def eratosthenes_sieve(lim):
    """
    Generate all primes up to lim using Sieve of Eratosthenes
    Returns a list of primes
    """
    is_prime = [True] * lim
    if lim > 0:
        is_prime[0] = False
    if lim > 1:
        is_prime[1] = False

    for i in range(4, lim, 2):
        is_prime[i] = False

    i = 3
    while i * i < lim:
        if is_prime[i]:
            for j in range(i * i, lim, i * 2):
                is_prime[j] = False
        i += 2

    primes = [i for i in range(2, lim) if is_prime[i]]
    return primes, is_prime
