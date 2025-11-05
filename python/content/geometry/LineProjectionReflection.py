"""
Author: Victor Lecomte, chilli
Date: 2019-10-29
License: CC0
Source: https://vlecomte.github.io/cp-geo.pdf
Description: Projects point p onto line ab. Set refl=True to get reflection
of point p across line ab instead. The wrong point will be returned if P is
an integer point and the desired point doesn't have integer coordinates.
Products of three coordinates are used in intermediate steps so watch out
for overflow.
Status: stress-tested
"""


def line_proj(a, b, p, refl=False):
    """
    Project point p onto line ab.
    If refl=True, return reflection of p across line ab.
    """
    v = b - a
    return p - v.perp() * (1 + refl) * v.cross(p - a) / v.dist2()
