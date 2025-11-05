"""
Author: Stjepan Glavina, chilli
Date: 2019-05-05
License: Unlicense
Source: https://github.com/stjepang/snippets/blob/master/convex_hull.cpp
Description:
Returns a list of the points of the convex hull in counter-clockwise order.
Points on the edge of the hull between two other points are not considered part of the hull.
Time: O(n log n)
Status: stress-tested, tested with kattis:convexhull
"""


def convex_hull(pts):
    """
    Compute convex hull of a set of points.
    Returns points in counter-clockwise order.
    Points on edges are not included.
    """
    if len(pts) <= 1:
        return pts

    pts = sorted(pts)
    h = [None] * (len(pts) + 1)
    s = 0
    t = 0

    for it in range(2):
        for p in pts:
            while t >= s + 2 and h[t - 2].cross(h[t - 1], p) <= 0:
                t -= 1
            h[t] = p
            t += 1
        s = t - 1
        pts = pts[::-1]

    return h[:t - (t == 2 and h[0] == h[1])]
