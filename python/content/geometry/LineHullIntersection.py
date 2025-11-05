"""
 * Author: Oleksandr Bacherikov, chilli
 * Date: 2019-05-07
 * License: Boost Software License
 * Source: https://github.com/AlCash07/ACTL/blob/master/include/actl/geometry/algorithm/intersect/line_convex_polygon.hpp
 * Description: Line-convex polygon intersection. The polygon must be ccw and have no collinear points.
 * line_hull(line, poly) returns a tuple describing the intersection of a line with the polygon:
 *   (-1, -1) if no collision,
 *   (i, -1) if touching the corner i,
 *   (i, i) if along side (i, i+1),
 *   (i, j) if crossing sides (i, i+1) and (j, j+1).
 * In the last case, if a corner i is crossed, this is treated as happening on side (i, i+1).
 * The points are returned in the same order as the line hits the polygon.
 * extr_vertex returns the point of a hull with the max projection onto a line.
 * Time: O(log n)
 * Status: stress-tested

"""

from Point import sgn


def extr_vertex(poly, dir):
    """
    Find vertex of convex polygon with maximum projection in direction dir.
    """
    n = len(poly)

    def cmp(i, j):
        return sgn(dir.perp().cross(poly[i % n] - poly[j % n]))

    def extr(i):
        return cmp(i + 1, i) >= 0 and cmp(i, i - 1 + n) < 0

    lo = 0
    hi = n

    if extr(0):
        return 0

    while lo + 1 < hi:
        m = (lo + hi) // 2
        if extr(m):
            return m
        ls = cmp(lo + 1, lo)
        ms = cmp(m + 1, m)
        if ls < ms or (ls == ms and ls == cmp(lo, m)):
            hi = m
        else:
            lo = m

    return lo


def line_hull(a, b, poly):
    """
    Find intersection of line (through points a and b) with convex polygon.
    Returns (i, j) as described in the header comment.
    """
    n = len(poly)

    def cmp_l(i):
        return sgn(a.cross(poly[i], b))

    end_a = extr_vertex(poly, (a - b).perp())
    end_b = extr_vertex(poly, (b - a).perp())

    if cmp_l(end_a) < 0 or cmp_l(end_b) > 0:
        return (-1, -1)

    res = [0, 0]

    for i in range(2):
        lo = end_b
        hi = end_a

        while (lo + 1) % n != hi:
            m = ((lo + hi + (0 if lo < hi else n)) // 2) % n
            if cmp_l(m) == cmp_l(end_b):
                lo = m
            else:
                hi = m

        res[i] = (lo + (0 if cmp_l(hi) else 1)) % n
        end_a, end_b = end_b, end_a

    if res[0] == res[1]:
        return (res[0], -1)

    if not cmp_l(res[0]) and not cmp_l(res[1]):
        diff = (res[0] - res[1] + n + 1) % n
        if diff == 0:
            return (res[0], res[0])
        elif diff == 2:
            return (res[1], res[1])

    return tuple(res)
