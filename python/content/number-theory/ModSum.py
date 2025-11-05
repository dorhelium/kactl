"""
Author: Simon Lindholm
Date: 2015-06-23
License: CC0
Source: own work
Description: Sums of mod'ed arithmetic progressions.

modsum(to, c, k, m) = sum_{i=0}^{to-1} (ki+c) % m
divsum is similar but for floored division.
Time: O(log(m)), with a large constant.
Status: Tested for all |k|,|c|,to,m <= 50, and on kattis:aladin
"""

def sumsq(to):
    """
    Sum of 0 + 1 + 2 + ... + (to-1)
    Written in a weird way to deal with overflows correctly
    """
    return to // 2 * ((to - 1) | 1)

def divsum(to, c, k, m):
    """
    Sum of floor((ki + c) / m) for i from 0 to to-1
    """
    res = k // m * sumsq(to) + c // m * to
    k %= m
    c %= m
    if not k:
        return res
    to2 = (to * k + c) // m
    return res + (to - 1) * to2 - divsum(to2, m - 1 - c, m, k)

def modsum(to, c, k, m):
    """
    Sum of (ki + c) % m for i from 0 to to-1
    """
    c = ((c % m) + m) % m
    k = ((k % m) + m) % m
    return to * c + k * sumsq(to) - m * divsum(to, c, k, m)
