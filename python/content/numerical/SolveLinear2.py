"""
Author: Simon Lindholm
Date: 2016-09-06
License: CC0
Source: me
Description: To get all uniquely determined values of x back from SolveLinear, make the following changes:
Status: tested on kattis:equationsolverplus, stress-tested
"""

# This file contains modifications to SolveLinear.py
# To use: import SolveLinear and modify as follows:

# In solve_linear function, change:
#   for j in range(i + 1, n):  # to:
#   for j in range(n):
#       if j != i:

# Then at the end, replace x assignment with:
#   x.clear()
#   undefined = float('nan')  # or some sentinel value
#   x.extend([undefined] * m)
#   for i in range(rank):
#       valid = True
#       for j in range(rank, m):
#           if abs(A[i][j]) > EPS:
#               valid = False
#               break
#       if valid:
#           x[col[i]] = b[i] / A[i][i]

"""
Complete modified version for reference:
"""

EPS = 1e-12

def solve_linear_unique(A, b, x):
    """
    Solve linear system Ax = b, marking non-unique variables
    A: coefficient matrix (modified in-place)
    b: right-hand side (modified in-place)
    x: output solution vector (NaN for non-unique values)
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
        # Modified: eliminate in all rows, not just below
        for j in range(n):
            if j != i:
                fac = A[j][i] * bv
                b[j] -= fac * b[i]
                for k in range(i + 1, m):
                    A[j][k] -= fac * A[i][k]
        rank += 1

    # Modified ending: mark non-unique values as NaN
    undefined = float('nan')
    x.clear()
    x.extend([undefined] * m)
    for i in range(rank):
        valid = True
        for j in range(rank, m):
            if abs(A[i][j]) > EPS:
                valid = False
                break
        if valid:
            x[col[i]] = b[i] / A[i][i]

    return rank
