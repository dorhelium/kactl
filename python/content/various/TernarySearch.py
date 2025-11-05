"""
Author: Simon Lindholm
Date: 2015-05-12
License: CC0
Source: own work
Description:
Find the smallest i in [a,b] that maximizes f(i), assuming that f(a) < ... < f(i) >= ... >= f(b).
To reverse which of the sides allows non-strict inequalities, change the < marked with (A) to <=,
and reverse the loop at (B).
To minimize f, change it to >, also at (B).
Usage:
    ind = tern_search(0, n-1, lambda i: a[i])
Time: O(log(b-a))
Status: tested
"""

def tern_search(a, b, f):
    """
    Ternary search to find index that maximizes f.

    Args:
        a: Left bound (inclusive)
        b: Right bound (inclusive)
        f: Function to maximize

    Returns:
        Index in [a, b] that maximizes f(i)
    """
    assert a <= b

    while b - a >= 5:
        mid = (a + b) // 2
        if f(mid) < f(mid + 1):  # (A)
            a = mid
        else:
            b = mid + 1

    # Linear search in remaining range
    for i in range(a + 1, b + 1):  # (B)
        if f(a) < f(i):
            a = i

    return a
