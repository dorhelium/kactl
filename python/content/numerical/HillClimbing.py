"""
 * Author: Simon Lindholm
 * Date: 2015-02-04
 * License: CC0
 * Source: Johan Sannemo
 * Description: Poor man's optimization for unimodal functions.
 * Status: used with great success

"""

def hill_climb(start, f):
    """
    Hill climbing optimization starting from point start
    f: function to minimize, takes a point (list/tuple of 2 floats)
    Returns: (value, point) tuple
    """
    cur = (f(start), start[:])
    jmp = 1e9

    while jmp > 1e-20:
        for _ in range(100):
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    p = cur[1][:]
                    p[0] += dx * jmp
                    p[1] += dy * jmp
                    cur = min(cur, (f(p), p))
        jmp /= 2

    return cur
