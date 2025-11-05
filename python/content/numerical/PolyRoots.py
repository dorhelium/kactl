"""
Author: Per Austrin
Date: 2004-02-08
License: CC0
Description: Finds the real roots to a polynomial.
Usage: poly_roots(Poly([2, -3, 1]), -1e9, 1e9) # solve x^2-3x+2 = 0
Time: O(n^2 log(1/epsilon))
"""

from Polynomial import Poly

def poly_roots(p, xmin, xmax):
    """
    Find all real roots of polynomial p in interval [xmin, xmax]
    Returns list of roots
    """
    if len(p.a) == 2:
        return [-p.a[0] / p.a[1]]

    ret = []
    der = Poly(p.a[:])
    der.diff()
    dr = poly_roots(der, xmin, xmax)
    dr.append(xmin - 1)
    dr.append(xmax + 1)
    dr.sort()

    for i in range(len(dr) - 1):
        l = dr[i]
        h = dr[i + 1]
        sign = p(l) > 0
        if sign != (p(h) > 0):
            for _ in range(60):  # while h - l > 1e-8
                m = (l + h) / 2
                f = p(m)
                if (f <= 0) != sign:
                    l = m
                else:
                    h = m
            ret.append((l + h) / 2)

    return ret
