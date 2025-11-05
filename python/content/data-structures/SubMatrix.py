"""
 * Author: Johan Sannemo
 * Date: 2014-11-28
 * License: CC0
 * Source: Folklore
 * Description: Calculate submatrix sums quickly, given upper-left and lower-right corners (half-open).
 * Usage:
 *  m = SubMatrix(matrix)
 *  m.sum(0, 0, 2, 2)  // top left 4 elements
 * Time: O(N^2 + Q)
 * Status: Tested on Kattis

"""

class SubMatrix:
    def __init__(self, v):
        R = len(v)
        C = len(v[0]) if R > 0 else 0
        self.p = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                self.p[r + 1][c + 1] = v[r][c] + self.p[r][c + 1] + self.p[r + 1][c] - self.p[r][c]

    def sum(self, u, l, d, r):
        return self.p[d][r] - self.p[d][l] - self.p[u][r] + self.p[u][l]
