"""
Author: Mattias de Zalenski
Date: Unknown
Source: Geometry in C
Description: Computes the Delaunay triangulation of a set of points.
 Each circumcircle contains none of the input points.
 If any three points are collinear or any four are on the same circle, behavior is undefined.
Time: O(n^2)
Status: stress-tested
"""

from Point3D import Point3D


def delaunay(ps, trifun):
    """
    Compute Delaunay triangulation.
    ps: list of 2D points
    trifun: callback function that takes three vertex indices (a, b, c)
    """
    if len(ps) == 3:
        d = 1 if ps[0].cross(ps[1], ps[2]) < 0 else 0
        trifun(0, 1 + d, 2 - d)
        return

    # Lift points to 3D paraboloid
    p3 = []
    for p in ps:
        p3.append(Point3D(p.x, p.y, p.dist2()))

    if len(ps) > 3:
        # Import and use 3D hull
        from hull_3d import hull_3d
        faces = hull_3d(p3)

        for t in faces:
            # Check if face points upward (visible from infinity above)
            if (p3[t.b] - p3[t.a]).cross(p3[t.c] - p3[t.a]).dot(Point3D(0, 0, 1)) < 0:
                trifun(t.a, t.c, t.b)
