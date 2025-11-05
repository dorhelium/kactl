"""
 * Author: Victor Lecomte, chilli
 * Date: 2019-10-31
 * License: CC0
 * Source: https://vlecomte.github.io/cp-geo.pdf
 * Description: Finds the external tangents of two circles, or internal if r2 is negated.
 * Can return 0, 1, or 2 tangents -- 0 if one circle contains the other (or overlaps it, in the internal case, or if the circles are the same);
 * 1 if the circles are tangent to each other (in which case .first = .second and the tangent line is perpendicular to the line between the centers).
 * first and second give the tangency points at circle 1 and 2 respectively.
 * To find the tangents of a circle with a point set r2 to 0.
 * Status: tested

"""

import math


def tangents(c1, r1, c2, r2):
    """
    Find tangent lines between two circles.
    Returns list of (point1, point2) tuples where point1 is on circle 1 and point2 is on circle 2.
    For external tangents, use positive radii.
    For internal tangents, negate r2.
    To find tangents from a point to a circle, set r2 = 0.
    """
    d = c2 - c1
    dr = r1 - r2
    d2 = d.dist2()
    h2 = d2 - dr * dr

    if d2 == 0 or h2 < 0:
        return []

    out = []
    for sign in [-1, 1]:
        v = (d * dr + d.perp() * math.sqrt(h2) * sign) / d2
        out.append((c1 + v * r1, c2 + v * r2))

    if h2 == 0:
        out.pop()

    return out
