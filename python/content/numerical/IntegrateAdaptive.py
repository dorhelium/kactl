"""
Author: Simon Lindholm
Date: 2015-02-11
License: CC0
Source: Wikipedia
Description: Fast integration using an adaptive Simpson's rule.
Usage:
    sphere_volume = quad(-1, 1, lambda x:
        quad(-1, 1, lambda y:
        quad(-1, 1, lambda z:
        x*x + y*y + z*z < 1)))
Status: mostly untested
"""

def _simpson(f, a, b):
    """Simpson's rule for interval [a, b]"""
    return (f(a) + 4 * f((a + b) / 2) + f(b)) * (b - a) / 6

def _rec(f, a, b, eps, S):
    """Recursive adaptive Simpson's rule"""
    c = (a + b) / 2
    S1 = _simpson(f, a, c)
    S2 = _simpson(f, c, b)
    T = S1 + S2
    if abs(T - S) <= 15 * eps or b - a < 1e-10:
        return T + (T - S) / 15
    return _rec(f, a, c, eps / 2, S1) + _rec(f, c, b, eps / 2, S2)

def quad(a, b, f, eps=1e-8):
    """
    Adaptive integration of function f from a to b
    eps: desired precision
    """
    return _rec(f, a, b, eps, _simpson(f, a, b))
