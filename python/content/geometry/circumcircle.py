"""
 * Author: Ulf Lundstrom
 * Date: 2009-04-11
 * License: CC0
 * Source: http://en.wikipedia.org/wiki/Circumcircle
 * Description:
 * The circumcircle of a triangle is the circle intersecting all three vertices. cc_radius returns the radius of the circle going through points A, B and C and cc_center returns the center of the same circle.
 * Status: tested

"""


def cc_radius(A, B, C):
    """
    Returns the radius of the circumcircle of triangle ABC.
    """
    return ((B - A).dist() * (C - B).dist() * (A - C).dist() /
            abs((B - A).cross(C - A)) / 2)


def cc_center(A, B, C):
    """
    Returns the center of the circumcircle of triangle ABC.
    """
    b = C - A
    c = B - A
    return A + (b * c.dist2() - c * b.dist2()).perp() / b.cross(c) / 2
