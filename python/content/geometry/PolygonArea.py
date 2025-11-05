"""
 * Author: Ulf Lundstrom
 * Date: 2009-03-21
 * License: CC0
 * Source: tinyKACTL
 * Description: Returns twice the signed area of a polygon.
 *  Clockwise enumeration gives negative area. Watch out for overflow if using int!
 * Status: Stress-tested and tested on kattis:polygonarea

"""


def polygon_area2(v):
    """
    Returns twice the signed area of a polygon.
    Clockwise enumeration gives negative area.
    Watch out for overflow if using int coordinates!
    """
    a = v[-1].cross(v[0])
    for i in range(len(v) - 1):
        a += v[i].cross(v[i + 1])
    return a
