"""
Author: Johan Sannemo
Date: 2017-04-18
Source: derived from https://gist.github.com/msg555/4963794 by Mark Gordon
Description: Computes all faces of the 3-dimension hull of a point set.
 No four points must be coplanar, or else random results will be returned.
 All faces will point outwards.
Time: O(n^2)
Status: tested on SPOJ CH3D
"""

from Point3D import Point3D


class PR:
    """Pair structure for edge tracking."""
    def __init__(self):
        self.a = -1
        self.b = -1

    def ins(self, x):
        if self.a == -1:
            self.a = x
        else:
            self.b = x

    def rem(self, x):
        if self.a == x:
            self.a = -1
        else:
            self.b = -1

    def cnt(self):
        return (self.a != -1) + (self.b != -1)


class F:
    """Face structure."""
    def __init__(self, q, a, b, c):
        self.q = q
        self.a = a
        self.b = b
        self.c = c


def hull_3d(A):
    """
    Compute 3D convex hull.
    Returns list of faces, each face is an F object with vertices a, b, c.
    No four points must be coplanar.
    """
    assert len(A) >= 4

    n = len(A)
    E = [[PR() for _ in range(n)] for _ in range(n)]

    FS = []

    def mf(i, j, k, l):
        """Make a face."""
        q = (A[j] - A[i]).cross(A[k] - A[i])
        if q.dot(A[l]) > q.dot(A[i]):
            q = q * -1

        f = F(q, i, j, k)
        E[f.a][f.b].ins(k)
        E[f.a][f.c].ins(j)
        E[f.b][f.c].ins(i)
        FS.append(f)

    # Initialize with tetrahedron
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                mf(i, j, k, 6 - i - j - k)

    # Add remaining points
    for i in range(4, len(A)):
        j = 0
        while j < len(FS):
            f = FS[j]
            if f.q.dot(A[i]) > f.q.dot(A[f.a]):
                E[f.a][f.b].rem(f.c)
                E[f.a][f.c].rem(f.b)
                E[f.b][f.c].rem(f.a)
                FS[j] = FS[-1]
                FS.pop()
                j -= 1
            j += 1

        nw = len(FS)
        for j in range(nw):
            f = FS[j]
            if E[f.a][f.b].cnt() != 2:
                mf(f.a, f.b, i, f.c)
            if E[f.a][f.c].cnt() != 2:
                mf(f.a, f.c, i, f.b)
            if E[f.b][f.c].cnt() != 2:
                mf(f.b, f.c, i, f.a)

    # Ensure correct orientation
    for f in FS:
        if (A[f.b] - A[f.a]).cross(A[f.c] - A[f.a]).dot(f.q) <= 0:
            f.b, f.c = f.c, f.b

    return FS
