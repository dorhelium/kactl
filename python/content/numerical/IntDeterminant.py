"""
Author: Unknown
Date: 2014-11-27
Source: somewhere on github
Description: Calculates determinant using modular arithmetics.
Modulos can also be removed to get a pure-integer version.
Time: O(N^3)
Status: bruteforce-tested for N <= 3, mod <= 7
"""

def det(a, mod=12345):
    """Calculate determinant modulo mod (modifies input matrix)"""
    n = len(a)
    ans = 1

    for i in range(n):
        for j in range(i + 1, n):
            while a[j][i] != 0:  # gcd step
                t = a[i][i] // a[j][i]
                if t:
                    for k in range(i, n):
                        a[i][k] = (a[i][k] - a[j][k] * t) % mod
                a[i], a[j] = a[j], a[i]
                ans *= -1
        ans = ans * a[i][i] % mod
        if not ans:
            return 0

    return (ans + mod) % mod
