"""
 * Author: Simon Lindholm
 * License: CC0
 * Source: http://codeforces.com/blog/entry/8219
 * Description: When doing DP on intervals: a[i][j] = min_{i < k < j}(a[i][k] + a[k][j]) + f(i, j),
 * where the (minimal) optimal k increases with both i and j,
 * one can solve intervals in increasing order of length, and search k = p[i][j] for a[i][j]
 * only between p[i][j-1] and p[i+1][j].
 * This is known as Knuth DP. Sufficient criteria for this are if f(b,c) <= f(a,d) and
 * f(a,c) + f(b,d) <= f(a,d) + f(b,c) for all a <= b <= c <= d.
 * Consider also: LineContainer (ch. Data structures), monotone queues, ternary search.
 * Time: O(N^2)

"""

def knuth_dp(n, f):
    """
    Knuth DP optimization for interval DP.

    Args:
        n: Number of elements
        f: Cost function f(i, j) for interval [i, j]

    Returns:
        Tuple of (dp table, optimal k table)

    The DP recurrence is:
        dp[i][j] = min_{i < k < j}(dp[i][k] + dp[k][j]) + f(i, j)

    Where the optimal k is monotone.
    """
    dp = [[0] * n for _ in range(n)]
    p = [[0] * n for _ in range(n)]

    # Initialize
    for i in range(n):
        p[i][i] = i

    # Solve by increasing interval length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # Search range for optimal k
            lo = p[i][j - 1] if j > 0 else i + 1
            hi = p[i + 1][j] if i + 1 < n else j - 1

            best = float('inf')
            best_k = i + 1

            for k in range(max(i + 1, lo), min(j, hi + 1)):
                cost = dp[i][k] + dp[k][j] + f(i, j)
                if cost < best:
                    best = cost
                    best_k = k

            dp[i][j] = best
            p[i][j] = best_k

    return dp, p
