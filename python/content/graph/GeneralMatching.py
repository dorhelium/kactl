"""
 * Author: Simon Lindholm
 * Date: 2016-12-09
 * License: CC0
 * Source: http://www.mimuw.edu.pl/~mucha/pub/mucha_sankowski_focs04.pdf
 * Description: Matching for general graphs.
 * Fails with probability N / mod.
 * Time: O(N^3)
 * Status: not very well tested

"""

# Note: This requires MatrixInverse-mod.py from numerical section
# The implementation below is incomplete without the matrix inverse function

import random

MOD = 10**9 + 7  # Should match the mod used in MatrixInverse

def modpow(base, exp, mod):
    """Compute base^exp mod mod"""
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

def general_matching(N, edges):
    """
    Find maximum matching in general graph.
    N: number of vertices
    edges: list of (a, b) edges
    Returns: list of matched pairs (i, j)

    Note: Requires mat_inv function from MatrixInverse-mod.py
    """
    # Build skew-symmetric matrix
    mat = [[0] * N for _ in range(N)]

    for a, b in edges:
        r = random.randint(0, MOD - 1)
        mat[a][b] = r
        mat[b][a] = (MOD - r) % MOD

    # r = mat_inv(mat)  # Requires MatrixInverse implementation
    # M = 2 * N - r
    # assert r % 2 == 0

    # Code below requires matrix inverse functionality
    # This is a placeholder showing the algorithm structure

    # if M != N:
    #     # Expand matrix and retry
    #     pass

    # has = [1] * M
    # ret = []

    # for _ in range(M // 2):
    #     # Find edge in matching
    #     fi, fj = -1, -1
    #     for i in range(M):
    #         if has[i]:
    #             for j in range(i + 1, M):
    #                 if A[i][j] and mat[i][j]:
    #                     fi, fj = i, j
    #                     break
    #             if fi != -1:
    #                 break
    #
    #     if fj < N:
    #         ret.append((fi, fj))
    #
    #     has[fi] = has[fj] = 0
    #
    #     # Update matrix (Gaussian elimination)
    #     for sw in range(2):
    #         a = modpow(A[fi][fj], MOD - 2, MOD)
    #         for i in range(M):
    #             if has[i] and A[i][fj]:
    #                 b = (A[i][fj] * a) % MOD
    #                 for j in range(M):
    #                     A[i][j] = (A[i][j] - A[fi][j] * b) % MOD
    #         fi, fj = fj, fi

    # return ret

    raise NotImplementedError("Requires MatrixInverse-mod.py implementation")
