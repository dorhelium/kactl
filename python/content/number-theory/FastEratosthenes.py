"""
Author: Jakob Kogler, chilli, pajenegod
Date: 2020-04-12
License: CC0
Description: Prime sieve for generating all primes smaller than LIM.
Time: LIM=1e9 ≈ 1.5s
Status: Stress-tested
Details: Despite its n log log n complexity, segmented sieve is still faster
than other options, including bitset sieves and linear sieves. This is
primarily due to its low memory usage, which reduces cache misses. This
implementation skips even numbers.

Benchmark can be found here: https://ideone.com/e7TbX4

The line `for i in range(idx, S+L, p)` is done on purpose for performance reasons.
See https://github.com/kth-competitive-programming/kactl/pull/166#discussion_r408354338
"""

def eratosthenes(lim):
    """
    Segmented sieve of Eratosthenes for generating primes up to lim
    Returns a list of primes and a boolean list is_prime
    """
    import math

    S = int(round(math.sqrt(lim)))
    R = lim // 2

    primes = [2]
    sieve = [False] * (S + 1)
    cp = []  # list of (prime, current_index) pairs

    # Small sieve
    for i in range(3, S + 1, 2):
        if not sieve[i]:
            cp.append([i, i * i // 2])
            for j in range(i * i, S + 1, 2 * i):
                sieve[j] = True

    # Segmented sieve
    for L in range(1, R + 1, S):
        block = [False] * S

        for p_idx in range(len(cp)):
            p, idx = cp[p_idx]
            i = idx
            while i < S + L:
                if i - L >= 0 and i - L < S:
                    block[i - L] = True
                cp[p_idx][1] = i + p
                i += p

        for i in range(min(S, R - L)):
            if not block[i]:
                primes.append((L + i) * 2 + 1)

    # Create is_prime boolean list
    is_prime = [False] * lim
    for p in primes:
        if p < lim:
            is_prime[p] = True

    return primes
