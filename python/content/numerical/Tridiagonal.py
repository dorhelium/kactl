"""
 * Author: Ulf Lundstrom, Simon Lindholm
 * Date: 2009-08-15
 * License: CC0
 * Source: https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
 * Description: x=tridiagonal(d,p,q,b) solves the equation system
 *     b = diag_matrix * x
 * where diag_matrix is a tridiagonal matrix with:
 * - d[i] on the main diagonal
 * - p[i] on the superdiagonal
 * - q[i] on the subdiagonal

 * This is useful for solving problems on the type
 *     a[i] = b[i]*a[i-1] + c[i]*a[i+1] + d[i], 1 <= i <= n,
 * where a[0], a[n+1], b[i], c[i] and d[i] are known. a can then be obtained from
 *     {a[i]} = tridiagonal({1,-1,-1,...,-1,1}, {0,c[1],c[2],...,c[n]},
 *                          {b[1],b[2],...,b[n],0}, {a[0],d[1],d[2],...,d[n],a[n+1]})

 * Fails if the solution is not unique.

 * If |d[i]| > |p[i]| + |q[i-1]| for all i, or |d[i]| > |p[i-1]| + |q[i]|,
 * or the matrix is positive definite, the algorithm is numerically stable and
 * neither tr nor the check for diag[i] == 0 is needed.
 * Time: O(N)
 * Status: Brute-force tested mod 5 and 7 and stress-tested for real matrices obeying the criteria above.

"""

def tridiagonal(diag, super_diag, sub, b):
    """
    Solve tridiagonal system
    diag: main diagonal
    super_diag: superdiagonal (above main)
    sub: subdiagonal (below main)
    b: right-hand side
    Returns: solution vector x
    """
    n = len(b)
    diag = diag[:]  # Copy to avoid modifying input
    b = b[:]
    tr = [0] * n

    for i in range(n - 1):
        if abs(diag[i]) < 1e-9 * abs(super_diag[i]):  # diag[i] == 0
            b[i + 1] -= b[i] * diag[i + 1] / super_diag[i]
            if i + 2 < n:
                b[i + 2] -= b[i] * sub[i + 1] / super_diag[i]
            diag[i + 1] = sub[i]
            i += 1
            tr[i] = 1
        else:
            diag[i + 1] -= super_diag[i] * sub[i] / diag[i]
            b[i + 1] -= b[i] * sub[i] / diag[i]

    for i in range(n - 1, -1, -1):
        if tr[i]:
            b[i], b[i - 1] = b[i - 1], b[i]
            diag[i - 1] = diag[i]
            b[i] /= super_diag[i - 1]
        else:
            b[i] /= diag[i]
            if i:
                b[i - 1] -= b[i] * super_diag[i - 1]

    return b
