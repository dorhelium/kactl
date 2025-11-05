import sys
import random
import math
import cmath
from numerical.FastFourierTransform import fft, conv

def test_fft():
    random.seed(42)

    # Test basic FFT
    n = 8
    a = [complex(random.randint(-5, 4), random.randint(-5, 4)) for _ in range(n)]
    aorig = a[:]

    fft(a)

    # Verify FFT computation
    for k in range(n):
        expected = sum(aorig[x] * cmath.exp(2j * math.pi * k * x / n) for x in range(n))
        assert abs(expected - a[k]) < 1e-6, \
            f"FFT verification failed at k={k}: expected {expected}, got {a[k]}"

    # Test convolution
    A = [random.uniform(-5, 5) for _ in range(4)]
    B = [random.uniform(-5, 5) for _ in range(6)]

    C = conv(A, B)

    # Verify convolution
    eps = 1e-8
    for i in range(len(A) + len(B) - 1):
        expected = sum(A[j] * B[i - j] for j in range(len(A))
                       if 0 <= i - j < len(B))
        assert abs(expected - C[i]) < eps, \
            f"Convolution failed at i={i}: expected {expected}, got {C[i]}"

    # Test more convolutions
    for _ in range(100):
        n1 = random.randint(1, 20)
        n2 = random.randint(1, 20)

        A = [random.uniform(-10, 10) for _ in range(n1)]
        B = [random.uniform(-10, 10) for _ in range(n2)]

        C = conv(A, B)

        # Verify
        for i in range(len(A) + len(B) - 1):
            expected = sum(A[j] * B[i - j] for j in range(len(A))
                           if 0 <= i - j < len(B))
            assert abs(expected - C[i]) < 1e-6, \
                f"Convolution failed"

    # Test edge cases
    assert conv([], [1, 2, 3]) == []
    assert conv([1, 2, 3], []) == []

    # Test simple convolutions
    C = conv([1], [2])
    assert abs(C[0] - 2) < 1e-6

    C = conv([1, 2], [3, 4])
    expected = [3, 10, 8]  # 1*3, 1*4+2*3, 2*4
    for i in range(len(expected)):
        assert abs(C[i] - expected[i]) < 1e-6

    print("Tests passed!")

if __name__ == "__main__":
    test_fft()
