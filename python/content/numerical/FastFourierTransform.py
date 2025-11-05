"""
Author: Ludo Pulles, chilli, Simon Lindholm
Date: 2019-01-09
License: CC0
Source: http://neerc.ifmo.ru/trains/toulouse/2017/fft2.pdf (do read, it's excellent)
Accuracy bound from http://www.daemonology.net/papers/fft.pdf
Description: fft(a) computes hat{f}(k) = sum_x a[x] * exp(2*pi*i * k*x / N) for all k.
N must be a power of 2.
Useful for convolution: conv(a, b) = c, where c[x] = sum a[i]*b[x-i].
For convolution of complex numbers or more than two vectors: FFT, multiply
pointwise, divide by n, reverse(start+1, end), FFT back.
Rounding is safe if (sum a_i^2 + sum b_i^2)*log_2(N) < 9*10^14
(in practice 10^16; higher for random inputs).
Otherwise, use NTT/FFTMod.
Time: O(N log N) with N = |A|+|B| (~1s for N=2^22)
Status: somewhat tested
Details: An in-depth examination of precision for both FFT and FFTMod can be found
here (https://github.com/simonlindholm/fft-precision/blob/master/fft-precision.md)
"""

import math
import cmath

# Static variables to cache roots
_R = [1, 1]
_rt = [1, 1]
_k_cache = 2

def fft(a):
    """Compute FFT in-place on list of complex numbers"""
    global _R, _rt, _k_cache

    n = len(a)
    L = n.bit_length() - 1

    # Extend roots cache if needed
    k = _k_cache
    while k < n:
        _R.extend([0] * k)
        _rt.extend([0] * k)
        x = cmath.exp(1j * math.pi / k)
        for i in range(k, 2 * k):
            if i & 1:
                _R[i] = _R[i // 2] * x
            else:
                _R[i] = _R[i // 2]
            _rt[i] = complex(_R[i].real, _R[i].imag)
        k *= 2
    _k_cache = k

    # Bit-reversal permutation
    rev = [0] * n
    for i in range(n):
        rev[i] = (rev[i // 2] | ((i & 1) << L)) // 2
    for i in range(n):
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]

    # FFT computation
    k = 1
    while k < n:
        i = 0
        while i < n:
            for j in range(k):
                z = _rt[j + k] * a[i + j + k]
                a[i + j + k] = a[i + j] - z
                a[i + j] = a[i + j] + z
            i += 2 * k
        k *= 2

def conv(a, b):
    """Compute convolution of two real-valued sequences"""
    if not a or not b:
        return []

    res_len = len(a) + len(b) - 1
    L = res_len.bit_length()
    n = 1 << L

    # Pack a and b into complex array
    in_arr = [complex(a[i] if i < len(a) else 0,
                      b[i] if i < len(b) else 0) for i in range(n)]

    fft(in_arr)

    # Multiply
    for i in range(n):
        in_arr[i] *= in_arr[i]

    # Prepare for inverse FFT
    out = [0] * n
    for i in range(n):
        out[i] = in_arr[(-i) & (n - 1)] - in_arr[i].conjugate()

    fft(out)

    # Extract result
    res = [out[i].imag / (4 * n) for i in range(res_len)]
    return res
