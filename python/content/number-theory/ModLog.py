"""
Author: Bjorn Martinsson
Date: 2020-06-03
License: CC0
Source: own work
Description: Returns the smallest x > 0 s.t. a^x = b (mod m), or
-1 if no such x exists. mod_log(a,1,m) can be used to
calculate the order of a.
Time: O(sqrt(m))
Status: tested for all 0 <= a,x < 500 and 0 < m < 500.

Details: This algorithm uses the baby-step giant-step method to
find (i,j) such that a^(n * i) = b * a^j (mod m), where n > sqrt(m)
and 0 < i, j <= n. If a and m are coprime then a^j has a modular
inverse, which means that a^(i * n - j) = b (mod m).

However this particular implementation of baby-step giant-step works even
without assuming a and m are coprime, using the following idea:

Assume p^x is a prime divisor of m. Then we have 3 cases
   1. b is divisible by p^x
   2. b is divisible only by some p^y, 0<y<x
   3. b is not divisible by p
The important thing to note is that in case 2, mod_log(a,b,m) (if
it exists) cannot be > sqrt(m), (technically it cannot be >= log2(m)).
So once all exponenents of a that are <= sqrt(m) has been checked, you
cannot have case 2. Case 2 is the only tricky case.

So the modification allowing for non-coprime input involves checking all
exponents of a that are <= n, and then handling the non-tricky cases by
a simple gcd(a^n,m) == gcd(b,m) check.
"""

import math

def mod_log(a, b, m):
    """
    Returns the smallest x > 0 such that a^x ≡ b (mod m)
    Returns -1 if no such x exists
    """
    n = int(math.sqrt(m)) + 1
    e = 1
    f = 1
    j = 1
    A = {}

    # Baby step
    while j <= n and (e := (f := e * a % m)) != b % m:
        A[e * b % m] = j
        j += 1

    if e == b % m:
        return j

    # Giant step
    if math.gcd(m, e) == math.gcd(m, b):
        for i in range(2, n + 2):
            e = e * f % m
            if e in A:
                return n * i - A[e]

    return -1
