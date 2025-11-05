"""
Author: chilli
Date: 2019-04-16
License: CC0
Source: based on KACTL's FFT
Description: ntt(a) computes hat{f}(k) = sum_x a[x] * g^{xk} for all k, where g=root^{(mod-1)/N}.
N must be a power of 2.
Useful for convolution modulo specific nice primes of the form 2^a*b+1,
where the convolution result has size at most 2^a. For arbitrary modulo, see FFTMod.
conv(a, b) = c, where c[x] = sum a[i]*b[x-i].
For manual convolution: NTT the inputs, multiply
pointwise, divide by n, reverse(start+1, end), NTT back.
Inputs must be in [0, mod).
Time: O(N log N)
Status: stress-tested
"""

MOD = (119 << 23) + 1  # = 998244353
ROOT = 62
# For p < 2^30 there is also e.g. 5 << 25, 7 << 26, 479 << 21
# and 483 << 21 (same root). The last two are > 10^9.

def mod_pow(base, exp, mod):
    """Compute (base^exp) % mod"""
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

# Static cache for roots
_rt = [1, 1]
_k_cache = 2
_s_cache = 2

def ntt(a, mod=MOD, root=ROOT):
    """Compute NTT in-place on list a"""
    global _rt, _k_cache, _s_cache

    n = len(a)
    L = n.bit_length() - 1

    # Extend roots cache if needed
    k = _k_cache
    s = _s_cache
    while k < n:
        _rt.extend([0] * k)
        z = [1, mod_pow(root, mod >> s, mod)]
        for i in range(k, 2 * k):
            _rt[i] = _rt[i // 2] * z[i & 1] % mod
        k *= 2
        s += 1
    _k_cache = k
    _s_cache = s

    # Bit-reversal permutation
    rev = [0] * n
    for i in range(n):
        rev[i] = (rev[i // 2] | ((i & 1) << L)) // 2
    for i in range(n):
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]

    # NTT computation
    k = 1
    while k < n:
        i = 0
        while i < n:
            for j in range(k):
                z = _rt[j + k] * a[i + j + k] % mod
                a[i + j + k] = (a[i + j] - z + (mod if z > a[i + j] else 0)) % mod
                a[i + j] = (a[i + j] + (z - mod if a[i + j] + z >= mod else z)) % mod
            i += 2 * k
        k *= 2

def conv(a, b, mod=MOD, root=ROOT):
    """Compute convolution modulo mod"""
    if not a or not b:
        return []

    s = len(a) + len(b) - 1
    B = s.bit_length()
    n = 1 << B
    inv = mod_pow(n, mod - 2, mod)

    L = a[:] + [0] * (n - len(a))
    R = b[:] + [0] * (n - len(b))
    out = [0] * n

    ntt(L, mod, root)
    ntt(R, mod, root)

    for i in range(n):
        out[(-i) & (n - 1)] = L[i] * R[i] % mod * inv % mod

    ntt(out, mod, root)

    return out[:s]
