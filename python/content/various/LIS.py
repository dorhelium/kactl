"""
Author: Johan Sannemo
License: CC0
Description: Compute indices for the longest increasing subsequence.
Time: O(N * log N)
Status: Tested on kattis:longincsubseq, stress-tested
"""

from bisect import bisect_left

def lis(S):
    """
    Compute indices of the longest increasing subsequence.

    Args:
        S: Input sequence

    Returns:
        List of indices forming the longest increasing subsequence
    """
    if not S:
        return []

    n = len(S)
    prev = [0] * n
    res = []

    for i in range(n):
        # Change bisect_left to bisect_right for longest non-decreasing subsequence
        pos = bisect_left(res, (S[i], 0))

        if pos == len(res):
            res.append((S[i], i))
        else:
            res[pos] = (S[i], i)

        prev[i] = 0 if pos == 0 else res[pos - 1][1]

    # Reconstruct the sequence
    L = len(res)
    cur = res[-1][1]
    ans = [0] * L

    while L > 0:
        L -= 1
        ans[L] = cur
        cur = prev[cur]

    return ans
