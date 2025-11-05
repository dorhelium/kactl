"""
Author: Victor Lecomte, chilli
Date: 2019-04-27
License: CC0
Source: https://vlecomte.github.io/cp-geo.pdf
Description:
If a unique intersection point between the line segments going from s1 to e1 and from s2 to e2 exists then it is returned.
If no intersection point exists an empty list is returned.
If infinitely many exist a list with 2 elements is returned, containing the endpoints of the common line segment.
The wrong position will be returned if P is Point with int and the intersection point does not have integer coordinates.
Products of three coordinates are used in intermediate steps so watch out for overflow if using int.
Usage:
    inter = seg_inter(s1, e1, s2, e2)
    if len(inter) == 1:
        print("segments intersect at", inter[0])
Status: stress-tested, tested on kattis:intersection
"""

from Point import sgn
from OnSegment import on_segment


def seg_inter(a, b, c, d):
    """
    Find intersection of two line segments.
    Returns:
    - Empty list: no intersection
    - List with 1 point: unique intersection
    - List with 2 points: segments overlap
    """
    oa = c.cross(d, a)
    ob = c.cross(d, b)
    oc = a.cross(b, c)
    od = a.cross(b, d)

    # Checks if intersection is single non-endpoint point
    if sgn(oa) * sgn(ob) < 0 and sgn(oc) * sgn(od) < 0:
        return [(a * ob - b * oa) / (ob - oa)]

    s = set()
    if on_segment(c, d, a):
        s.add(a)
    if on_segment(c, d, b):
        s.add(b)
    if on_segment(a, b, c):
        s.add(c)
    if on_segment(a, b, d):
        s.add(d)

    return list(s)
