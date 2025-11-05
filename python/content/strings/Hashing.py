"""
 * Author: Simon Lindholm
 * Date: 2015-03-15
 * License: CC0
 * Source: own work
 * Description: Self-explanatory methods for string hashing.
 * Status: stress-tested

"""


# Arithmetic mod 2^64-1. 2x slower than mod 2^64 and more
# code, but works on evil test data (e.g. Thue-Morse, where
# ABBA... and BAAB... of length 2^10 hash the same mod 2^64).
# "Use simple integer hash instead" if you think test data is random,
# or work mod 10^9+7 if the Birthday paradox is not a problem.

class H:
    MOD = (1 << 64) - 1

    def __init__(self, x=0):
        self.x = x & self.MOD

    def __add__(self, o):
        result = self.x + o.x
        # Handle overflow
        result = (result & self.MOD) + (result >> 64)
        return H(result)

    def __sub__(self, o):
        return self + H(~o.x & self.MOD)

    def __mul__(self, o):
        # Simulate 128-bit multiplication
        m = self.x * o.x
        low = m & self.MOD
        high = m >> 64
        return H(low) + H(high)

    def get(self):
        return self.x if self.x != self.MOD else 0

    def __eq__(self, o):
        return self.get() == o.get()

    def __lt__(self, o):
        return self.get() < o.get()

    def __hash__(self):
        return self.get()


C = H(int(1e11) + 3)  # (order ~ 3e9; random also ok)


class HashInterval:
    def __init__(self, s):
        self.ha = [H(0)] * (len(s) + 1)
        self.pw = [H(0)] * (len(s) + 1)
        self.pw[0] = H(1)

        for i in range(len(s)):
            self.ha[i + 1] = self.ha[i] * C + H(ord(s[i]))
            self.pw[i + 1] = self.pw[i] * C

    def hash_interval(self, a, b):
        """Hash [a, b)"""
        return self.ha[b] - self.ha[a] * self.pw[b - a]


def get_hashes(s, length):
    if len(s) < length:
        return []

    h = H(0)
    pw = H(1)
    for i in range(length):
        h = h * C + H(ord(s[i]))
        pw = pw * C

    ret = [h]
    for i in range(length, len(s)):
        h = h * C + H(ord(s[i])) - pw * H(ord(s[i - length]))
        ret.append(h)

    return ret


def hash_string(s):
    h = H(0)
    for c in s:
        h = h * C + H(ord(c))
    return h
