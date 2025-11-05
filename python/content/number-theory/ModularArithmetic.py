"""
 * Author: Lukas Polacek
 * Date: 2009-09-28
 * License: CC0
 * Source: folklore
 * Description: Operators for modular arithmetic. You need to set mod to
 * some number first and then you can use the structure.

"""

def euclid(a, b):
    """
    Returns (gcd, x, y) such that ax + by = gcd(a, b)
    """
    if not b:
        return (a, 1, 0)
    d, y, x = euclid(b, a % b)
    y -= (a // b) * x
    return (d, x, y)

MOD = 17  # change to something else

class Mod:
    """
    Class for modular arithmetic operations
    """
    def __init__(self, x):
        self.x = x % MOD

    def __add__(self, other):
        return Mod((self.x + other.x) % MOD)

    def __sub__(self, other):
        return Mod((self.x - other.x + MOD) % MOD)

    def __mul__(self, other):
        return Mod((self.x * other.x) % MOD)

    def __truediv__(self, other):
        return self * other.invert()

    def invert(self):
        """
        Compute modular inverse
        """
        g, x, y = euclid(self.x, MOD)
        assert g == 1
        return Mod((x + MOD) % MOD)

    def __pow__(self, e):
        """
        Compute self^e mod MOD
        """
        if e == 0:
            return Mod(1)
        r = self ** (e // 2)
        r = r * r
        return self * r if e & 1 else r

    def __repr__(self):
        return f"Mod({self.x})"
