"""
Author: Ulf Lundstrom
Date: 2009-03-21
License: CC0
Source:
Description: Returns where p is as seen from s towards e. 1/0/-1 <=> left/on line/right.
If the optional argument eps is given 0 is returned if p is within distance eps from the line.
P is supposed to be Point where T is e.g. float or int.
It uses products in intermediate steps so watch out for overflow if using int.
Usage:
    left = side_of(p1, p2, q) == 1
Status: tested
"""

from Point import sgn


def side_of(s, e, p, eps=None):
    """
    Returns where p is as seen from s towards e.
    Returns 1 if left, 0 if on line, -1 if right.

    If eps is provided, returns 0 if p is within distance eps from the line.
    """
    if eps is None:
        return sgn(s.cross(e, p))
    else:
        a = (e - s).cross(p - s)
        l = (e - s).dist() * eps
        return (a > l) - (a < -l)
