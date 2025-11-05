"""
 * Author: Simon Lindholm
 * Date: 2016-08-31
 * License: CC0
 * Source: http://eli.thegreenplace.net/2009/03/07/computing-modular-square-roots-in-python/
 * Description: Tonelli-Shanks algorithm for modular square roots. Finds x s.t. x^2 = a (mod p) (-x gives the other solution).
 * Time: O(log^2 p) worst case, O(log p) for most p
 * Status: Tested for all a,p <= 10000

"""

def mod_sqrt(a, p):
    """
    Find x such that x^2 ≡ a (mod p)
    Returns -1 if no solution exists
    """
    a %= p
    if a < 0:
        a += p
    if a == 0:
        return 0

    # Check if solution exists using Euler's criterion
    if pow(a, (p - 1) // 2, p) != 1:
        return -1  # no solution

    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    # a^(n+3)/8 or 2^(n+3)/8 * 2^(n-1)/4 works if p % 8 == 5
    s = p - 1
    r = 0
    while s % 2 == 0:
        r += 1
        s //= 2

    # Find a non-square mod p
    n = 2
    while pow(n, (p - 1) // 2, p) != p - 1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)

    while True:
        t = b
        m = 0
        while m < r and t != 1:
            t = t * t % p
            m += 1

        if m == 0:
            return x

        gs = pow(g, 1 << (r - m - 1), p)
        g = gs * gs % p
        x = x * gs % p
        b = b * g % p
        r = m
