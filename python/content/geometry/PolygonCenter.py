"""
Author: Ulf Lundstrom
Date: 2009-04-08
License: CC0
Source:
Description: Returns the center of mass for a polygon.
Time: O(n)
Status: Tested
"""


def polygon_center(v):
    """
    Returns the center of mass (centroid) of a polygon.
    The polygon vertices should be ordered (either CW or CCW).
    """
    res_x = 0.0
    res_y = 0.0
    A = 0.0

    j = len(v) - 1
    for i in range(len(v)):
        cross_prod = v[j].cross(v[i])
        res_x += (v[i].x + v[j].x) * cross_prod
        res_y += (v[i].y + v[j].y) * cross_prod
        A += cross_prod
        j = i

    from Point import Point
    return Point(res_x / A / 3, res_y / A / 3)
