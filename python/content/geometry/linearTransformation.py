"""
 * Author: Per Austrin, Ulf Lundstrom
 * Date: 2009-04-09
 * License: CC0
 * Source:
 * Description:
 * Apply the linear transformation (translation, rotation and scaling) which takes line p0-p1 to line q0-q1 to point r.
 * Status: not tested

"""

from Point import Point


def linear_transformation(p0, p1, q0, q1, r):
    """
    Apply the linear transformation (translation, rotation, scaling)
    that takes line p0-p1 to line q0-q1, applied to point r.
    """
    dp = p1 - p0
    dq = q1 - q0
    num = Point(dp.cross(dq), dp.dot(dq))
    return q0 + Point((r - p0).cross(num), (r - p0).dot(num)) / dp.dist2()
