"""
 * Author: Victor Lecomte, chilli
 * Date: 2019-04-26
 * License: CC0
 * Source: https://vlecomte.github.io/cp-geo.pdf
 * Description: Returns true if p lies within the polygon. If strict is true,
 * it returns false for points on the boundary. The algorithm uses
 * products in intermediate steps so watch out for overflow.
 * Time: O(n)
 * Usage:
 *     v = [Point(4, 4), Point(1, 2), Point(2, 1)]
 *     in_poly = in_polygon(v, Point(3, 3), False)
 * Status: stress-tested and tested on kattis:pointinpolygon

"""

from OnSegment import on_segment


def in_polygon(p, a, strict=True):
    """
    Check if point a is inside polygon p.
    If strict=True, returns False for points on boundary.
    If strict=False, returns True for points on boundary.
    """
    cnt = 0
    n = len(p)

    for i in range(n):
        q = p[(i + 1) % n]
        if on_segment(p[i], q, a):
            return not strict
        # or: if seg_dist(p[i], q, a) <= eps: return not strict
        cnt ^= ((a.y < p[i].y) - (a.y < q.y)) * a.cross(p[i], q) > 0

    return cnt
