"""
 * Author: Mårten Wiman
 * License: CC0
 * Source: Pisinger 1999, "Linear Time Algorithms for Knapsack Problems with Bounded Weights"
 * Description: Given N non-negative integer weights w and a non-negative target t,
 * computes the maximum S <= t such that S is the sum of some subset of the weights.
 * Time: O(N * max(w_i))
 * Status: Tested on kattis:eavesdropperevasion, stress-tested

"""

def knapsack(w, t):
    """
    Fast knapsack for bounded weights.

    Args:
        w: List of non-negative integer weights
        t: Target sum (non-negative)

    Returns:
        Maximum sum S <= t achievable as a subset sum
    """
    a = 0
    b = 0

    # Greedy phase: add weights while possible
    while b < len(w) and a + w[b] <= t:
        a += w[b]
        b += 1

    if b == len(w):
        return a

    # DP phase
    m = max(w)
    v = [-1] * (2 * m)
    v[a + m - t] = b

    for i in range(b, len(w)):
        u = v[:]
        for x in range(m):
            if v[x + w[i]] < u[x]:
                v[x + w[i]] = u[x]

        x = 2 * m - 1
        while x > m:
            for j in range(max(0, u[x]), v[x]):
                if v[x - w[j]] < j:
                    v[x - w[j]] = j
            x -= 1

    # Find maximum achievable sum
    a = t
    while v[a + m - t] < 0:
        a -= 1

    return a
