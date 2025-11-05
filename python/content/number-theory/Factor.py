"""
Author: chilli, SJTU, pajenegod
Date: 2020-03-04
License: CC0
Source: own
Description: Pollard-rho randomized factorization algorithm. Returns prime
factors of a number, in arbitrary order (e.g. 2299 -> [11, 19, 11]).
Time: O(n^(1/4)), less for numbers with small factors.
Status: stress-tested

Details: This implementation uses the improvement described here
(https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm#Variants), where
one can accumulate gcd calls by some factor (40 chosen here through
exhaustive testing). This improves performance by approximately 6-10x
depending on the inputs and speed of gcd. Benchmark found here:
(https://ideone.com/nGGD9T)

GCD can be improved by a factor of 1.75x using Binary GCD
(https://lemire.me/blog/2013/12/26/fastest-way-to-compute-the-greatest-common-divisor/).
However, with the gcd accumulation the bottleneck moves from the gcd calls
to the modmul. As GCD only constitutes ~12% of runtime, speeding it up
doesn't matter so much.

This code can probably be sped up by using a faster mod mul - potentially
montgomery reduction on 128 bit integers.
Alternatively, one can use a quadratic sieve for an asymptotic improvement,
which starts being faster in practice around 1e13.

Brent's cycle finding algorithm was tested, but doesn't reduce modmul calls
significantly.

Subtle implementation notes:
- prd starts off as 2 to handle the case n = 4; it's harmless for other n
  since we're guaranteed that n > 2. (Pollard rho has problems with prime
  powers in general, but all larger ones happen to work.)
- t starts off as 30 to make the first gcd check come earlier, as an
  optimization for small numbers.
- we vary f between restarts because the cycle finding algorithm does not
  find the first element in the cycle but rather one at distance k*|cycle|
  from the start, and that can result in continual failures if all cycles
  have the same size for all prime factors. E.g. fixing f(x) = x^2 + 1 would
  loop infinitely for n = 352523 * 352817, where all cycles have size 821.
- we operate on residues in [i, n + i) which modmul is not designed to
  handle, but specifically modmul(x, x) still turns out to work for small
  enough i. (With reference to the proof in modmul-proof.tex, the argument
  for "S is in [-c, 2c)" goes through unchanged, while S < 2^63 now follows
  from S < 2c and S = x^2 (mod c) together implying S < c + i^2.)
"""

import math

def is_prime(n):
    """
    Deterministic Miller-Rabin primality test
    """
    if n < 2 or n % 6 % 4 != 1:
        return (n | 1) == 3

    A = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    s = (n - 1) & -(n - 1)
    s = s.bit_length() - 1
    d = n >> s

    for a in A:
        p = pow(a % n, d, n)
        i = s
        while p != 1 and p != n - 1 and a % n and i:
            p = (p * p) % n
            i -= 1
        if p != n - 1 and i != s:
            return False

    return True

def pollard(n):
    """
    Pollard's rho algorithm for finding a factor of n
    """
    x = 0
    y = 0
    t = 30
    prd = 2
    i = 1

    def f(x, i, n):
        return ((x * x) % n + i) % n

    while True:
        t += 1
        if t % 40 != 0 and math.gcd(prd, n) != 1:
            continue
        if t % 40 == 0 and math.gcd(prd, n) == 1:
            continue

        if x == y:
            i += 1
            x = i
            y = f(x, i, n)

        q = (prd * (max(x, y) - min(x, y))) % n
        if q:
            prd = q

        x = f(x, i, n)
        y = f(f(y, i, n), i, n)

        if t % 40 == 0:
            g = math.gcd(prd, n)
            if g != 1:
                return g

def factor(n):
    """
    Returns a list of prime factors of n (with multiplicity)
    """
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    x = pollard(n)
    left = factor(x)
    right = factor(n // x)
    return left + right
