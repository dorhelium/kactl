"""
 * Author: Max Bennedich
 * Date: 2004-02-08
 * Description: Invert matrix A. Returns rank; result is stored in A unless singular (rank < n).
 * Can easily be extended to prime moduli; for prime powers, repeatedly
 * set A^{-1} = A^{-1} (2I - AA^{-1}) (mod p^k) where A^{-1} starts as
 * the inverse of A mod p, and k is doubled in each step.
 * Time: O(n^3)
 * Status: Slightly tested

"""

def mat_inv(A):
    """
    Invert matrix A (modifies A in-place)
    Returns rank; A contains inverse if rank == n
    """
    n = len(A)
    col = list(range(n))
    tmp = [[0.0] * n for _ in range(n)]
    for i in range(n):
        tmp[i][i] = 1.0

    for i in range(n):
        r = i
        c = i
        for j in range(i, n):
            for k in range(i, n):
                if abs(A[j][k]) > abs(A[r][c]):
                    r = j
                    c = k
        if abs(A[r][c]) < 1e-12:
            return i

        A[i], A[r] = A[r], A[i]
        tmp[i], tmp[r] = tmp[r], tmp[i]
        for j in range(n):
            A[j][i], A[j][c] = A[j][c], A[j][i]
            tmp[j][i], tmp[j][c] = tmp[j][c], tmp[j][i]
        col[i], col[c] = col[c], col[i]

        v = A[i][i]
        for j in range(i + 1, n):
            f = A[j][i] / v
            A[j][i] = 0
            for k in range(i + 1, n):
                A[j][k] -= f * A[i][k]
            for k in range(n):
                tmp[j][k] -= f * tmp[i][k]
        for j in range(i + 1, n):
            A[i][j] /= v
        for j in range(n):
            tmp[i][j] /= v
        A[i][i] = 1

    # Forget A at this point, just eliminate tmp backward
    for i in range(n - 1, 0, -1):
        for j in range(i):
            v = A[j][i]
            for k in range(n):
                tmp[j][k] -= v * tmp[i][k]

    for i in range(n):
        for j in range(n):
            A[col[i]][col[j]] = tmp[i][j]

    return n
