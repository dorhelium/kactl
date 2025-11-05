"""
Author: Ulf Lundstrom
Date: 2009-02-26
License: CC0
Source: My head with inspiration from tinyKACTL
Description: Class to handle points in the plane.
    T can be e.g. float or int. (Avoid using only int for division operations.)
Status: Works fine, used a lot
"""

import math


def sgn(x):
    """Return sign of x: 1 if positive, -1 if negative, 0 if zero."""
    return (x > 0) - (x < 0)


class Point:
    """2D Point class with geometric operations."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __lt__(self, p):
        return (self.x, self.y) < (p.x, p.y)

    def __eq__(self, p):
        return (self.x, self.y) == (p.x, p.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, d):
        return Point(self.x * d, self.y * d)

    def __rmul__(self, d):
        return Point(self.x * d, self.y * d)

    def __truediv__(self, d):
        return Point(self.x / d, self.y / d)

    def dot(self, p):
        """Dot product with another point."""
        return self.x * p.x + self.y * p.y

    def cross(self, *args):
        """Cross product. Can be called as:
        - p.cross(q): returns cross product of self and q
        - p.cross(a, b): returns cross product of (a-self) and (b-self)
        """
        if len(args) == 1:
            p = args[0]
            return self.x * p.y - self.y * p.x
        elif len(args) == 2:
            a, b = args
            return (a - self).cross(b - self)
        else:
            raise ValueError("cross() takes 1 or 2 arguments")

    def dist2(self):
        """Squared distance from origin."""
        return self.x * self.x + self.y * self.y

    def dist(self):
        """Distance from origin."""
        return math.sqrt(self.dist2())

    def angle(self):
        """Angle to x-axis in interval [-pi, pi]."""
        return math.atan2(self.y, self.x)

    def unit(self):
        """Return unit vector (distance = 1)."""
        return self / self.dist()

    def perp(self):
        """Return perpendicular vector (rotated +90 degrees)."""
        return Point(-self.y, self.x)

    def normal(self):
        """Return normalized perpendicular vector."""
        return self.perp().unit()

    def rotate(self, a):
        """Return point rotated 'a' radians ccw around the origin."""
        return Point(self.x * math.cos(a) - self.y * math.sin(a),
                    self.x * math.sin(a) + self.y * math.cos(a))

    def __repr__(self):
        return f"({self.x},{self.y})"
