"""
 * Author: Simon Lindholm
 * Date: 2015-01-31
 * License: CC0
 * Source: me
 * Description: A class for ordering angles (as represented by int points and
 *  a number of rotations around the origin). Useful for rotational sweeping.
 *  Sometimes also represents points or vectors.
 * Usage:
 *  v = [w[0], w[0].t360(), ...]  // sorted
 *  j = 0
 *  for i in range(n):
 *      while v[j] < v[i].t180():
 *          j += 1
 *  // sweeps j such that (j-i) represents the number of positively oriented triangles with vertices at 0 and i
 * Status: Used, works well

"""


class Angle:
    """Class for ordering angles with rotation tracking."""

    def __init__(self, x, y, t=0):
        self.x = x
        self.y = y
        self.t = t

    def __sub__(self, b):
        return Angle(self.x - b.x, self.y - b.y, self.t)

    def half(self):
        """Return which half-plane this angle is in."""
        assert self.x or self.y
        return self.y < 0 or (self.y == 0 and self.x < 0)

    def t90(self):
        """Rotate by 90 degrees."""
        return Angle(-self.y, self.x, self.t + (self.half() and self.x >= 0))

    def t180(self):
        """Rotate by 180 degrees."""
        return Angle(-self.x, -self.y, self.t + self.half())

    def t360(self):
        """Add one full rotation."""
        return Angle(self.x, self.y, self.t + 1)

    def __lt__(self, b):
        """Compare angles (add dist2() to also compare distances)."""
        return (self.t, self.half(), self.y * b.x) < \
               (b.t, b.half(), self.x * b.y)

    def __repr__(self):
        return f"Angle({self.x},{self.y},t={self.t})"


def segment_angles(a, b):
    """
    Given two points, this calculates the smallest angle between
    them, i.e., the angle that covers the defined line segment.
    """
    if b < a:
        a, b = b, a
    if b < a.t180():
        return (a, b)
    else:
        return (b, a.t360())


def angle_add(a, b):
    """Point a + vector b."""
    r = Angle(a.x + b.x, a.y + b.y, a.t)
    if a.t180() < r:
        r.t -= 1
    return r.t360() if r.t180() < a else r


def angle_diff(a, b):
    """Angle b - angle a."""
    tu = b.t - a.t
    a_temp = Angle(a.x, a.y, b.t)
    return Angle(a.x * b.x + a.y * b.y,
                a.x * b.y - a.y * b.x,
                tu - (b < a_temp))
