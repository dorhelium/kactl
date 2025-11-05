"""
Author: Simon Lindholm
Date: 2016-07-24
License: CC0
Source: Russian page
Description: Pre-computation of modular inverses. Assumes LIM <= mod and that mod is a prime.
Status: Works
"""

# Example usage:
# MOD = 1000000007
# LIM = 200000

def compute_inverses(lim, mod):
    """
    Pre-compute modular inverses for all numbers from 1 to lim-1
    Returns a list where inv[i] is the modular inverse of i modulo mod
    """
    inv = [0] * lim
    inv[1] = 1
    for i in range(2, lim):
        inv[i] = mod - (mod // i) * inv[mod % i] % mod
    return inv
