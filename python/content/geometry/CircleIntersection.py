"""
Author: Simon Lindholm
Date: 2015-09-01
License: CC0
Description: Computes the pair of points at which two circles intersect.
Returns None in case of no intersection, otherwise returns tuple of two points.
Status: stress-tested
"""

import math


def circle_inter(a, b, r1, r2):
    """
    Find intersection points of two circles.
    Circle 1: center a, radius r1
    Circle 2: center b, radius r2
    Returns None if no intersection, otherwise tuple of (point1, point2).
    """
    if a == b:
        assert r1 != r2
        return None

    vec = b - a
    d2 = vec.dist2()
    sum_r = r1 + r2
    dif = r1 - r2

    if sum_r * sum_r < d2 or dif * dif > d2:
        return None

    p = (d2 + r1 * r1 - r2 * r2) / (d2 * 2)
    h2 = r1 * r1 - p * p * d2

    mid = a + vec * p
    per = vec.perp() * (math.sqrt(max(0, h2)) / math.sqrt(d2))

    return (mid + per, mid - per)
