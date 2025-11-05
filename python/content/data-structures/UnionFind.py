"""
Author: Lukas Polacek
Date: 2009-10-26
License: CC0
Source: folklore
Description: Disjoint-set data structure.
Time: O(alpha(N))
"""

class UF:
    def __init__(self, n):
        self.e = [-1] * n

    def same_set(self, a, b):
        return self.find(a) == self.find(b)

    def size(self, x):
        return -self.e[self.find(x)]

    def find(self, x):
        if self.e[x] < 0:
            return x
        self.e[x] = self.find(self.e[x])
        return self.e[x]

    def join(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.e[a] > self.e[b]:
            a, b = b, a
        self.e[a] += self.e[b]
        self.e[b] = a
        return True
