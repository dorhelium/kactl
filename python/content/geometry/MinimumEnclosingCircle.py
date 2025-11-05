"""
 * Author: Andrew He, chilli
 * Date: 2019-05-07
 * License: CC0
 * Source: folklore
 * Description: Computes the minimum circle that encloses a set of points.
 * Time: expected O(n)
 * Status: stress-tested

"""

import random
from circumcircle import cc_center


def mec(ps):
    """
    Compute minimum enclosing circle of a set of points.
    Returns (center, radius) tuple.
    """
    ps = ps[:]  # Make a copy
    random.shuffle(ps)

    o = ps[0]
    r = 0
    EPS = 1 + 1e-8

    for i in range(len(ps)):
        if (o - ps[i]).dist() > r * EPS:
            o = ps[i]
            r = 0

            for j in range(i):
                if (o - ps[j]).dist() > r * EPS:
                    o = (ps[i] + ps[j]) / 2
                    r = (o - ps[i]).dist()

                    for k in range(j):
                        if (o - ps[k]).dist() > r * EPS:
                            o = cc_center(ps[i], ps[j], ps[k])
                            r = (o - ps[i]).dist()

    return (o, r)
