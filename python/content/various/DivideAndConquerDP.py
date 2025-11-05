"""
Author: Simon Lindholm
License: CC0
Source: Codeforces
Description: Given a[i] = min_{lo(i) <= k < hi(i)}(f(i, k)) where the (minimal)
optimal k increases with i, computes a[i] for i = L..R-1.
Time: O((N + (hi-lo)) * log N)
Status: tested on http://codeforces.com/contest/321/problem/E
"""

class DivideAndConquerDP:
    """
    Divide and conquer DP optimization.
    Modify the methods to match your specific problem.
    """
    def __init__(self):
        self.dp = None  # Your DP table
        self.res = None  # Result storage

    def lo(self, ind):
        """Minimum k value for index ind"""
        return 0

    def hi(self, ind):
        """Maximum k value for index ind"""
        return ind

    def f(self, ind, k):
        """Cost function f(ind, k)"""
        return self.dp[ind][k]

    def store(self, ind, k, v):
        """Store the result"""
        self.res[ind] = (k, v)

    def rec(self, L, R, LO, HI):
        """Recursive divide and conquer"""
        if L >= R:
            return

        mid = (L + R) >> 1
        best = (float('inf'), LO)

        # Find best k for mid
        for k in range(max(LO, self.lo(mid)), min(HI, self.hi(mid))):
            best = min(best, (self.f(mid, k), k))

        self.store(mid, best[1], best[0])
        self.rec(L, mid, LO, best[1] + 1)
        self.rec(mid + 1, R, best[1], HI)

    def solve(self, L, R):
        """Solve for range [L, R)"""
        self.rec(L, R, -float('inf'), float('inf'))
