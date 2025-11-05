"""
 * Author: Ulf Lundstrom with inspiration from tinyKACTL
 * Date: 2009-04-14
 * License: CC0
 * Source:
 * Description: Class to handle points in 3D space.
 *     T can be e.g. float or int.
 * Usage:
 * Status: tested, except for phi and theta

"""

import math


class Point3D:
    """3D Point class with geometric operations."""

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __lt__(self, p):
        return (self.x, self.y, self.z) < (p.x, p.y, p.z)

    def __eq__(self, p):
        return (self.x, self.y, self.z) == (p.x, p.y, p.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __add__(self, p):
        return Point3D(self.x + p.x, self.y + p.y, self.z + p.z)

    def __sub__(self, p):
        return Point3D(self.x - p.x, self.y - p.y, self.z - p.z)

    def __mul__(self, d):
        return Point3D(self.x * d, self.y * d, self.z * d)

    def __rmul__(self, d):
        return Point3D(self.x * d, self.y * d, self.z * d)

    def __truediv__(self, d):
        return Point3D(self.x / d, self.y / d, self.z / d)

    def dot(self, p):
        """Dot product with another point."""
        return self.x * p.x + self.y * p.y + self.z * p.z

    def cross(self, p):
        """Cross product with another point."""
        return Point3D(
            self.y * p.z - self.z * p.y,
            self.z * p.x - self.x * p.z,
            self.x * p.y - self.y * p.x
        )

    def dist2(self):
        """Squared distance from origin."""
        return self.x * self.x + self.y * self.y + self.z * self.z

    def dist(self):
        """Distance from origin."""
        return math.sqrt(self.dist2())

    def phi(self):
        """Azimuthal angle (longitude) to x-axis in interval [-pi, pi]."""
        return math.atan2(self.y, self.x)

    def theta(self):
        """Zenith angle (latitude) to the z-axis in interval [0, pi]."""
        return math.atan2(math.sqrt(self.x * self.x + self.y * self.y), self.z)

    def unit(self):
        """Return unit vector (distance = 1)."""
        return self / self.dist()

    def normal(self, p):
        """Return unit vector normal to self and p."""
        return self.cross(p).unit()

    def rotate(self, angle, axis):
        """Return point rotated 'angle' radians ccw around axis."""
        s = math.sin(angle)
        c = math.cos(angle)
        u = axis.unit()
        return u * self.dot(u) * (1 - c) + self * c - self.cross(u) * s

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"
