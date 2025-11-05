"""
 * Author: chilli
 * Date: 2019-04-25
 * License: CC0
 * Source: http://neerc.ifmo.ru/trains/toulouse/2017/fft2.pdf
 * Description: Higher precision FFT, can be used for convolutions modulo arbitrary integers
 * as long as N*log_2(N)*mod < 8.6*10^14 (in practice 10^16 or higher).
 * Inputs must be in [0, mod).
 * Time: O(N log N), where N = |A|+|B| (twice as slow as NTT or FFT)
 * Status: stress-tested
 * Details: An in-depth examination of precision for both FFT and FFTMod can be found
 * here (https://github.com/simonlindholm/fft-precision/blob/master/fft-precision.md)

"""

import math
from FastFourierTransform import fft

def conv_mod(a, b, M):
    """Compute convolution modulo M using FFT"""
    if not a or not b:
        return []

    res_len = len(a) + len(b) - 1
    B = res_len.bit_length()
    n = 1 << B
    cut = int(math.sqrt(M))

    # Split into high and low parts
    L = [complex((a[i] if i < len(a) else 0) // cut,
                 (a[i] if i < len(a) else 0) % cut) for i in range(n)]
    R = [complex((b[i] if i < len(b) else 0) // cut,
                 (b[i] if i < len(b) else 0) % cut) for i in range(n)]

    fft(L)
    fft(R)

    outs = [0] * n
    outl = [0] * n
    for i in range(n):
        j = (-i) & (n - 1)
        outl[j] = (L[i] + L[j].conjugate()) * R[i] / (2.0 * n)
        outs[j] = (L[i] - L[j].conjugate()) * R[i] / (2.0 * n) / 1j

    fft(outl)
    fft(outs)

    res = []
    for i in range(res_len):
        av = int(outl[i].real + 0.5)
        cv = int(outs[i].imag + 0.5)
        bv = int(outl[i].imag + 0.5) + int(outs[i].real + 0.5)
        res.append(((av % M * cut + bv) % M * cut + cv) % M)

    return res
