"""
Author: Simon Lindholm
Date: 2015-02-11
License: CC0
Source: Wikipedia
Description: Simple integration of a function over an interval using
Simpson's rule. The error should be proportional to h^4, although in
practice you will want to verify that the result is stable to desired
precision when epsilon changes.
Status: mostly untested
"""

def quad(a, b, f, n=1000):
    """
    Integrate function f from a to b using Simpson's rule
    n: number of intervals (more = better precision)
    """
    h = (b - a) / 2 / n
    v = f(a) + f(b)
    for i in range(1, n * 2):
        v += f(a + i * h) * (4 if i & 1 else 2)
    return v * h / 3
