"""
Author: Ulf Lundstrom
Date: 2009-03-21
License: CC0
Source: Basic math
Description:
Returns the signed distance between point p and the line containing points a and b.
Positive value on left side and negative on right as seen from a towards b. a==b gives nan.
P is supposed to be Point or Point3D where T is e.g. float or int.
It uses products in intermediate steps so watch out for overflow if using int.
Using Point3D will always give a non-negative distance. For Point3D, call .dist on the result of the cross product.
Status: tested
"""


def line_dist(a, b, p):
    """
    Returns the signed distance between point p and the line containing points a and b.
    Positive value on left side, negative on right as seen from a towards b.
    """
    return (b - a).cross(p - a) / (b - a).dist()
