"""
Author: Simon Lindholm
Date: 2016-08-27
License: CC0
Source: own work
Description: Solves Ax = b over F_2. If there are multiple solutions, one is returned arbitrarily.
Returns rank, or -1 if no solutions. Destroys A and b.
Time: O(n^2 m)
Status: bruteforce-tested for n, m <= 4
"""

def solve_linear_binary(A, b, x, m):
    """
    Solve linear system Ax = b over GF(2)
    A: coefficient matrix as list of integers (bit vectors) - modified in-place
    b: right-hand side as list of integers (0 or 1) - modified in-place
    x: output solution as list (will be filled with 0/1)
    m: number of variables
    Returns: rank, or -1 if no solution

    Each A[i] is an integer where bit j represents A[i][j]
    """
    n = len(A)
    rank = 0
    br = 0

    col = list(range(m))

    for i in range(n):
        # Find pivot
        for br in range(i, n):
            if A[br] != 0:
                break

        if br == n - 1 and A[br] == 0:
            # No pivot found
            for j in range(i, n):
                if b[j]:
                    return -1
            break

        # Find first set bit >= i
        bc = i
        temp = A[br]
        while bc < m and not (temp & (1 << bc)):
            bc += 1

        if bc >= m:
            for j in range(i, n):
                if b[j]:
                    return -1
            break

        # Swap rows and columns
        A[i], A[br] = A[br], A[i]
        b[i], b[br] = b[br], b[i]
        col[i], col[bc] = col[bc], col[i]

        # Swap columns in all rows
        for j in range(n):
            bit_i = (A[j] >> i) & 1
            bit_bc = (A[j] >> bc) & 1
            if bit_i != bit_bc:
                A[j] ^= (1 << i)
                A[j] ^= (1 << bc)

        # Eliminate
        for j in range(i + 1, n):
            if (A[j] >> i) & 1:
                b[j] ^= b[i]
                A[j] ^= A[i]

        rank += 1

    # Back substitution
    x.clear()
    x.extend([0] * m)
    for i in range(rank - 1, -1, -1):
        if b[i]:
            x[col[i]] = 1
            for j in range(i):
                if (A[j] >> i) & 1:
                    b[j] ^= 1

    return rank  # (multiple solutions if rank < m)
