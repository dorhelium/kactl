"""
 * Author: Ulf Lundstrom
 * Date: 2009-03-21
 * License: CC0
 * Source:
 * Description:
 * Returns the shortest distance between point p and the line segment from point s to e.
 * Usage:
 *     a = Point(0, 0)
 *     b = Point(2, 2)
 *     p = Point(1, 1)
 *     on_segment = seg_dist(a, b, p) < 1e-10
 * Status: tested

"""


def seg_dist(s, e, p):
    """
    Returns the shortest distance between point p and the line segment from s to e.
    """
    if s == e:
        return (p - s).dist()
    d = (e - s).dist2()
    t = min(d, max(0.0, (p - s).dot(e - s)))
    return ((p - s) * d - (e - s) * t).dist() / d
