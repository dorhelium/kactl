"""
Author: Simon Lindholm
Date: 2016-12-08
Source: The regular matrix inverse code
Description: Invert matrix A modulo a prime.
Returns rank; result is stored in A unless singular (rank < n).
For prime powers, repeatedly set A^{-1} = A^{-1} (2I - AA^{-1}) (mod p^k) where A^{-1} starts as
the inverse of A mod p, and k is doubled in each step.
Time: O(n^3)
Status: Slightly tested
"""

def mod_pow(base, exp, mod):
    """Compute (base^exp) % mod"""
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

def mat_inv(A, mod):
    """
    Invert matrix A modulo mod (modifies A in-place)
    Returns rank; A contains inverse if rank == n
    """
    n = len(A)
    col = list(range(n))
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        tmp[i][i] = 1

    for i in range(n):
        r = i
        c = i
        found = False
        for j in range(i, n):
            for k in range(i, n):
                if A[j][k]:
                    r = j
                    c = k
                    found = True
                    break
            if found:
                break
        if not found:
            return i

        A[i], A[r] = A[r], A[i]
        tmp[i], tmp[r] = tmp[r], tmp[i]
        for j in range(n):
            A[j][i], A[j][c] = A[j][c], A[j][i]
            tmp[j][i], tmp[j][c] = tmp[j][c], tmp[j][i]
        col[i], col[c] = col[c], col[i]

        v = mod_pow(A[i][i], mod - 2, mod)
        for j in range(i + 1, n):
            f = A[j][i] * v % mod
            A[j][i] = 0
            for k in range(i + 1, n):
                A[j][k] = (A[j][k] - f * A[i][k]) % mod
            for k in range(n):
                tmp[j][k] = (tmp[j][k] - f * tmp[i][k]) % mod
        for j in range(i + 1, n):
            A[i][j] = A[i][j] * v % mod
        for j in range(n):
            tmp[i][j] = tmp[i][j] * v % mod
        A[i][i] = 1

    for i in range(n - 1, 0, -1):
        for j in range(i):
            v = A[j][i]
            for k in range(n):
                tmp[j][k] = (tmp[j][k] - v * tmp[i][k]) % mod

    for i in range(n):
        for j in range(n):
            A[col[i]][col[j]] = tmp[i][j] % mod + (tmp[i][j] < 0) * mod

    return n
