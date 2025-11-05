"""
 * Author: Johan Sannemo
 * License: CC0
 * Description: Compute indices of smallest set of intervals covering another interval.
 * Intervals should be [inclusive, exclusive). To support [inclusive, inclusive],
 * change (A) to add "or not R". Returns empty set on failure (or if G is empty).
 * Time: O(N * log N)
 * Status: Tested on kattis:intervalcover

"""

def cover(G, I):
    """
    Find minimum set of interval indices that cover interval G.

    Args:
        G: Target interval as tuple (start, end) [inclusive, exclusive)
        I: List of available intervals as tuples (start, end)

    Returns:
        List of indices of intervals that cover G (empty if impossible)
    """
    n = len(I)
    S = list(range(n))
    S.sort(key=lambda i: I[i])

    R = []
    cur = G[0]
    at = 0

    while cur < G[1]:  # (A)
        mx = (cur, -1)

        while at < n and I[S[at]][0] <= cur:
            mx = max(mx, (I[S[at]][1], S[at]))
            at += 1

        if mx[1] == -1:
            return []

        cur = mx[0]
        R.append(mx[1])

    return R
