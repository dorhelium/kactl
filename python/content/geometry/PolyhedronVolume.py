"""
 * Author: Mattias de Zalenski
 * Date: 2002-11-04
 * Description: Magic formula for the volume of a polyhedron. Faces should point outwards.
 * Status: tested

"""


def signed_poly_volume(p, trilist):
    """
    Calculate the signed volume of a polyhedron.
    p: list of 3D points
    trilist: list of face objects, each with attributes a, b, c (vertex indices)
    Returns the signed volume (divide by 6 if needed).
    """
    v = 0.0
    for tri in trilist:
        v += p[tri.a].cross(p[tri.b]).dot(p[tri.c])
    return v / 6
