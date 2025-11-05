"""
 * Author: Simon Lindholm
 * Date: 2020-05-30
 * License: CC0
 * Source: https://en.wikipedia.org/wiki/Barrett_reduction
 * Description: Compute a % b about 5 times faster than usual, where b is constant but not known at compile time.
 * Returns a value congruent to a (mod b) in the range [0, 2b).
 * Note: Python's modulo operator is already quite optimized. This implementation demonstrates
 * the Barrett reduction algorithm, but may not provide the same speedup as in C++ due to
 * Python's arbitrary precision integers and different performance characteristics.
 * Status: proven correct, stress-tested
 * Details:
 * More precisely, it can be proven that the result equals 0 only if a = 0,
 * and otherwise lies in [1, (1 + a/2^64) * b).

"""

class FastMod:
    """
    Barrett reduction for fast modulo operation.
    Note: In Python, this may not be faster than built-in % due to
    arbitrary precision integer handling.
    """
    def __init__(self, b):
        """
        Initialize with modulus b.

        Args:
            b: The modulus (must be positive)
        """
        self.b = b
        # Compute m = floor(2^64 / b)
        # In Python, we use a large enough power of 2
        self.m = ((1 << 64) - 1) // b

    def reduce(self, a):
        """
        Compute a % b + (0 or b).
        Returns a value in [0, 2b).

        Args:
            a: The value to reduce

        Returns:
            Value congruent to a (mod b) in range [0, 2b)
        """
        # Barrett reduction: a - floor((m * a) / 2^64) * b
        quotient = (self.m * a) >> 64
        return a - quotient * self.b

# Note: For most Python use cases, simply use the built-in % operator:
# result = a % b
