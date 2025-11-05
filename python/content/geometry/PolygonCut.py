"""
 * Author: Ulf Lundstrom
 * Date: 2009-03-21
 * License: CC0
 * Source:
 * Description:
 * Returns a list with the vertices of a polygon with everything to the left of the line going from s to e cut away.
 * Usage:
 *     p = [...]
 *     p = polygon_cut(p, Point(0, 0), Point(1, 0))
 * Status: tested but not extensively

"""


def polygon_cut(poly, s, e):
    """
    Cut polygon with a line from s to e.
    Returns the part of the polygon to the right of the line (as seen from s to e).
    """
    res = []

    for i in range(len(poly)):
        cur = poly[i]
        prev = poly[i - 1] if i > 0 else poly[-1]

        a = s.cross(e, cur)
        b = s.cross(e, prev)

        if (a < 0) != (b < 0):
            res.append(cur + (prev - cur) * (a / (a - b)))
        if a < 0:
            res.append(cur)

    return res
