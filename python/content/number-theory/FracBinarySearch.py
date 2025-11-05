"""
Author: Lucian Bicsi, Simon Lindholm
Date: 2017-10-31
License: CC0
Description: Given f and N, finds the smallest fraction p/q in [0, 1]
such that f(p/q) is true, and p, q <= N.
You may want to throw an exception from f if it finds an exact solution,
in which case N can be removed.
Usage: frac_bs(lambda f: f[0]>=3*f[1], 10) # (1,3)
Time: O(log(N))
Status: stress-tested for n <= 300
"""

class Frac:
    """
    Class representing a fraction p/q
    """
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __getitem__(self, index):
        """Allow tuple-like access: f[0] for p, f[1] for q"""
        if index == 0:
            return self.p
        elif index == 1:
            return self.q
        else:
            raise IndexError("Frac index out of range")

    def __repr__(self):
        return f"Frac({self.p}, {self.q})"

def frac_bs(f, N):
    """
    Binary search for fractions.
    f: function that takes a Frac and returns a boolean
    N: maximum value for p and q
    Returns a Frac representing the smallest fraction p/q where f returns True
    """
    dir = True
    A = True
    B = True
    lo = Frac(0, 1)
    hi = Frac(1, 1)  # Set hi to Frac(1, 0) to search (0, N]

    if f(lo):
        return lo
    assert f(hi)

    while A or B:
        adv = 0
        step = 1  # move hi if dir, else lo

        si = 0
        while step:
            adv += step
            mid = Frac(lo.p * adv + hi.p, lo.q * adv + hi.q)

            if abs(mid.p) > N or mid.q > N or dir == (not f(mid)):
                adv -= step
                si = 2
            step *= 2
            if si == 2:
                step >>= si

        hi.p += lo.p * adv
        hi.q += lo.q * adv
        dir = not dir
        lo, hi = hi, lo
        A = B
        B = (adv != 0)

    return hi if dir else lo
