"""
 * Author: chilli, Ramchandra Apte, Noam527, Simon Lindholm
 * Date: 2019-04-24
 * License: CC0
 * Source: https://github.com/RamchandraApte/OmniTemplate/blob/master/src/number_theory/modulo.hpp
 * Description: Calculate a·b mod c (or a^b mod c) for 0 <= a, b <= c <= 7.2·10^18.
 * Time: O(1) for modmul, O(log b) for modpow
 * Status: stress-tested, proven correct
 * Details:
 * This runs ~2x faster than the naive (a * b) % M in C++.
 * In Python, integers have arbitrary precision, so we can use built-in pow(b, e, mod) for modular exponentiation.
 * However, for compatibility with the original algorithm, we provide both implementations.

"""

def mod_mul(a, b, m):
    """
    Calculate (a * b) % m
    In Python, this is straightforward due to arbitrary precision integers
    """
    return (a * b) % m

def mod_pow(b, e, mod):
    """
    Calculate b^e mod mod
    Python's built-in pow function handles this efficiently
    """
    return pow(b, e, mod)
