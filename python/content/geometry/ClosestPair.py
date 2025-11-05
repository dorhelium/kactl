"""
 * Author: Simon Lindholm
 * Date: 2019-04-17
 * License: CC0
 * Source: https://codeforces.com/blog/entry/58747
 * Description: Finds the closest pair of points.
 * Time: O(n log n)
 * Status: stress-tested

"""

import sys


def closest(v):
    """
    Find the closest pair of points.
    Returns tuple of two points with minimum distance.
    """
    assert len(v) > 1

    S = set()
    v = sorted(v, key=lambda p: p.y)

    ret_dist2 = sys.maxsize
    ret_pts = (v[0], v[1])

    j = 0
    for p in v:
        d_x = 1 + int((ret_dist2) ** 0.5)

        while v[j].y <= p.y - d_x:
            S.discard(v[j])
            j += 1

        # Find points in S within the bounding box
        candidates = []
        for pt in S:
            if abs(pt.x - p.x) <= d_x:
                candidates.append(pt)

        for lo in candidates:
            dist2 = (lo - p).dist2()
            if dist2 < ret_dist2:
                ret_dist2 = dist2
                ret_pts = (lo, p)

        S.add(p)

    return ret_pts
