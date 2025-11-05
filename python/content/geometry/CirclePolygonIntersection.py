"""
Author: chilli, Takanori MAEHARA
Date: 2019-10-31
License: CC0
Source: https://github.com/spaghetti-source/algorithm/blob/master/geometry/_geom.cc#L744
Description: Returns the area of the intersection of a circle with a
ccw polygon.
Time: O(n)
Status: Tested on GNYR 2019 Gerrymandering, stress-tested
"""

import math


def circle_poly(c, r, ps):
    """
    Calculate the area of intersection between a circle and a polygon.
    c: center of circle
    r: radius of circle
    ps: list of polygon vertices in CCW order
    """

    def arg(p, q):
        """Calculate angle using atan2."""
        return math.atan2(p.cross(q), p.dot(q))

    def tri(p, q):
        """Calculate area of circular segment for edge p-q."""
        r2 = r * r / 2
        d = q - p
        a = d.dot(p) / d.dist2()
        b = (p.dist2() - r * r) / d.dist2()
        det = a * a - b

        if det <= 0:
            return arg(p, q) * r2

        s = max(0.0, -a - math.sqrt(det))
        t = min(1.0, -a + math.sqrt(det))

        if t < 0 or 1 <= s:
            return arg(p, q) * r2

        u = p + d * s
        v = q + d * (t - 1)
        return arg(p, u) * r2 + u.cross(v) / 2 + arg(v, q) * r2

    total = 0.0
    for i in range(len(ps)):
        total += tri(ps[i] - c, ps[(i + 1) % len(ps)] - c)

    return total
