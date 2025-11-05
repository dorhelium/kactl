"""
Author: Simon Lindholm
Date: 2015-03-15
License: CC0
Source: own work
Description: Various self-explanatory methods for string hashing.
Use on Codeforces, which lacks 64-bit support and where solutions can be hacked.
Status: stress-tested
"""

import time


C = None  # initialized below


# Arithmetic mod two primes and 2^32 simultaneously.
class A:
    def __init__(self, x=0, b=None):
        if isinstance(x, int) and b is None:
            self.x = x
            self.b = x if not isinstance(x, A) else x.b
        else:
            self.x = x
            self.b = b

    @staticmethod
    def _create(M, B):
        class AMod:
            MOD = M

            def __init__(self, x=0, b=None):
                if b is None:
                    self.x = x
                    self.b = B(x) if not isinstance(x, AMod) else x.b
                else:
                    self.x = x
                    self.b = b

            def __add__(self, o):
                y = self.x + o.x
                return AMod(y - (y >= self.MOD) * self.MOD, self.b + o.b)

            def __sub__(self, o):
                y = self.x - o.x
                return AMod(y + (y < 0) * self.MOD, self.b - o.b)

            def __mul__(self, o):
                return AMod((self.x * o.x) % self.MOD, self.b * o.b)

            def __int__(self):
                return self.x ^ (int(self.b) << 21)

            def __eq__(self, o):
                return int(self) == int(o)

            def __lt__(self, o):
                return int(self) < int(o)

            def __hash__(self):
                return int(self)

        return AMod


class Unsigned:
    def __init__(self, x=0):
        self.x = x & 0xFFFFFFFF

    def __add__(self, o):
        return Unsigned((self.x + o.x) & 0xFFFFFFFF)

    def __sub__(self, o):
        return Unsigned((self.x - o.x) & 0xFFFFFFFF)

    def __mul__(self, o):
        return Unsigned((self.x * o.x) & 0xFFFFFFFF)

    def __int__(self):
        return self.x

    def __eq__(self, o):
        return self.x == o.x

    def __lt__(self, o):
        return self.x < o.x


# Create the hash type
A1 = A._create(1000000009, Unsigned)
H = A._create(1000000007, A1)


class HashInterval:
    def __init__(self, s):
        self.ha = [H(0)] * (len(s) + 1)
        self.pw = [H(0)] * (len(s) + 1)
        self.pw[0] = H(1)

        for i in range(len(s)):
            self.ha[i + 1] = self.ha[i] * H(C) + H(ord(s[i]))
            self.pw[i + 1] = self.pw[i] * H(C)

    def hash_interval(self, a, b):
        """Hash [a, b)"""
        return self.ha[b] - self.ha[a] * self.pw[b - a]


def get_hashes(s, length):
    if len(s) < length:
        return []

    h = H(0)
    pw = H(1)
    for i in range(length):
        h = h * H(C) + H(ord(s[i]))
        pw = pw * H(C)

    ret = [h]
    for i in range(length, len(s)):
        h = h * H(C) + H(ord(s[i])) - pw * H(ord(s[i - length]))
        ret.append(h)

    return ret


def hash_string(s):
    h = H(0)
    for c in s:
        h = h * H(C) + H(ord(c))
    return h


# Initialize C with time-based value
C = int(time.time() * 1000000) % 1000000007
