"""
Author: Simon Lindholm
Date: 2015-03-20
License: CC0
Source: me
Description: Split a monotone function on [from, to) into a minimal set of half-open intervals on which it has the same value.
Runs a callback g for each such interval.
Usage: constant_intervals(0, len(v), lambda x: v[x], lambda lo, hi, val: ...)
Time: O(k*log(n/k))
Status: tested
"""

def _rec(from_idx, to_idx, f, g, i, p, q):
    """Recursive helper for constant_intervals"""
    if p == q:
        return i, p
    if from_idx == to_idx:
        g(i[0], to_idx, p)
        i[0] = to_idx
        return i, q
    else:
        mid = (from_idx + to_idx) >> 1
        i, p = _rec(from_idx, mid, f, g, i, p, f(mid))
        i, p = _rec(mid + 1, to_idx, f, g, i, p, q)
        return i, p

def constant_intervals(from_idx, to_idx, f, g):
    """
    Split a monotone function into intervals with constant values.

    Args:
        from_idx: Starting index (inclusive)
        to_idx: Ending index (exclusive)
        f: Function that takes an index and returns a value
        g: Callback function(lo, hi, val) called for each constant interval
    """
    if to_idx <= from_idx:
        return
    i = [from_idx]
    p = f(i[0])
    q = f(to_idx - 1)
    i, p = _rec(from_idx, to_idx - 1, f, g, i, p, q)
    g(i[0], to_idx, q)
