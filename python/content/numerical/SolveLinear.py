"""
Author: Per Austrin, Simon Lindholm
Date: 2004-02-08
License: CC0
Description: Solves A * x = b. If there are multiple solutions, an arbitrary one is returned.
Returns rank, or -1 if no solutions. Data in A and b is lost.
Time: O(n^2 m)
Status: tested on kattis:equationsolver, and bruteforce-tested mod 3 and 5 for n,m <= 3
"""

EPS = 1e-12

def solve_linear(A, b, x):
    """
    Solve linear system Ax = b
    A: coefficient matrix (modified in-place)
    b: right-hand side (modified in-place)
    x: output solution vector (list, will be filled)
    Returns: rank, or -1 if no solution
    """
    n = len(A)
    m = len(x)
    rank = 0
    br = 0
    bc = 0

    if n:
        assert len(A[0]) == m

    col = list(range(m))

    for i in range(n):
        bv = 0.0
        for r in range(i, n):
            for c in range(i, m):
                v = abs(A[r][c])
                if v > bv:
                    br = r
                    bc = c
                    bv = v

        if bv <= EPS:
            for j in range(i, n):
                if abs(b[j]) > EPS:
                    return -1
            break

        A[i], A[br] = A[br], A[i]
        b[i], b[br] = b[br], b[i]
        col[i], col[bc] = col[bc], col[i]
        for j in range(n):
            A[j][i], A[j][bc] = A[j][bc], A[j][i]

        bv = 1.0 / A[i][i]
        for j in range(i + 1, n):
            fac = A[j][i] * bv
            b[j] -= fac * b[i]
            for k in range(i + 1, m):
                A[j][k] -= fac * A[i][k]
        rank += 1

    x.clear()
    x.extend([0.0] * m)
    for i in range(rank - 1, -1, -1):
        b[i] /= A[i][i]
        x[col[i]] = b[i]
        for j in range(i):
            b[j] -= A[j][i] * b[i]

    return rank  # (multiple solutions if rank < m)
