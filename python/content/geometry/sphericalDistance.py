"""
Author: Ulf Lundstrom
Date: 2009-04-07
License: CC0
Source: My geometric reasoning
Description: Returns the shortest distance on the sphere with radius radius between the points
with azimuthal angles (longitude) f1 (phi_1) and f2 (phi_2) from x axis and zenith angles
(latitude) t1 (theta_1) and t2 (theta_2) from z axis (0 = north pole). All angles measured
in radians. The algorithm starts by converting the spherical coordinates to cartesian coordinates
so if that is what you have you can use only the two last rows. dx*radius is then the difference
between the two points in the x direction and d*radius is the total distance between the points.
Status: tested on kattis:airlinehub
"""

import math


def spherical_distance(f1, t1, f2, t2, radius):
    """
    Calculate the shortest distance on a sphere between two points.
    f1, f2: azimuthal angles (longitude) in radians
    t1, t2: zenith angles (latitude) in radians, 0 = north pole
    radius: sphere radius
    """
    dx = math.sin(t2) * math.cos(f2) - math.sin(t1) * math.cos(f1)
    dy = math.sin(t2) * math.sin(f2) - math.sin(t1) * math.sin(f1)
    dz = math.cos(t2) - math.cos(t1)
    d = math.sqrt(dx * dx + dy * dy + dz * dz)
    return radius * 2 * math.asin(d / 2)
