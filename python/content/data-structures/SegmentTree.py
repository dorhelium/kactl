"""
Author: Lucian Bicsi
Date: 2017-10-31
License: CC0
Source: folklore
Description: Zero-indexed max-tree. Bounds are inclusive to the left and exclusive to the right.
Can be changed by modifying T, f and unit.
Time: O(log N)
Status: stress-tested
"""

class Tree:
    def __init__(self, n=0, def_val=None):
        self.n = n
        self.unit = float('-inf')  # INT_MIN equivalent
        if def_val is None:
            def_val = self.unit
        self.s = [def_val] * (2 * n)

    def f(self, a, b):
        """Associative function - max in this case"""
        return max(a, b)

    def update(self, pos, val):
        pos += self.n
        self.s[pos] = val
        while pos > 1:
            pos //= 2
            self.s[pos] = self.f(self.s[pos * 2], self.s[pos * 2 + 1])

    def query(self, b, e):
        """Query [b, e)"""
        ra = self.unit
        rb = self.unit
        b += self.n
        e += self.n
        while b < e:
            if b % 2:
                ra = self.f(ra, self.s[b])
                b += 1
            if e % 2:
                e -= 1
                rb = self.f(self.s[e], rb)
            b //= 2
            e //= 2
        return self.f(ra, rb)
