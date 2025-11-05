"""
Author: Simon Lindholm
Date: 2015-03-18
License: CC0
Source: https://software.intel.com/sites/landingpage/IntrinsicsGuide/
Description: Cheat sheet of SSE/AVX intrinsics, for doing arithmetic on several numbers at once.
Can provide a constant factor improvement of about 4, orthogonal to loop unrolling.
Note: Python does not have direct SIMD support like C++ intrinsics. For vectorized operations,
use NumPy which provides optimized array operations that leverage SIMD under the hood.
This file provides conceptual equivalents using NumPy.
"""

import numpy as np

# NumPy automatically uses SIMD when available
# Here are Python/NumPy equivalents to common SIMD operations:

def example_filtered_dot_product(n, a, b):
    """
    Example: compute dot product where a[i] * b[i] is included only if a[i] < b[i].

    This demonstrates how to achieve SIMD-like performance in Python using NumPy.

    Args:
        n: Length of arrays
        a: First array (numpy array or list)
        b: Second array (numpy array or list)

    Returns:
        Filtered dot product
    """
    # Convert to numpy arrays if needed
    a = np.array(a[:n], dtype=np.int16)
    b = np.array(b[:n], dtype=np.int16)

    # Vectorized filtering and multiplication
    mask = a < b
    filtered = a * mask
    result = np.sum(filtered * b, dtype=np.int64)

    return result

# Common NumPy operations that leverage SIMD:

def simd_operations_guide():
    """
    Guide to achieving SIMD-like performance in Python using NumPy.

    NumPy operations that are automatically vectorized:
    - Element-wise arithmetic: +, -, *, /, //, %, **
    - Comparison operations: <, <=, >, >=, ==, !=
    - Logical operations: &, |, ^, ~ (bitwise)
    - Math functions: np.abs, np.min, np.max, np.sum, np.prod
    - Reductions: np.sum, np.prod, np.min, np.max, np.mean
    - Broadcasting for operations on arrays of different shapes
    """
    # Example usage:
    a = np.arange(16, dtype=np.int32)
    b = np.arange(16, 32, dtype=np.int32)

    # Element-wise operations (SIMD-accelerated internally)
    result = a + b
    result = np.maximum(a, b)
    result = a & b  # Bitwise AND

    # Filtering with boolean masks
    mask = a > 5
    filtered = a[mask]

    # Dot products (highly optimized)
    dot = np.dot(a, b)

    # Reductions
    total = np.sum(a)

    return result

# For absolute maximum performance, consider:
# 1. Using NumPy with MKL (Math Kernel Library) backend
# 2. Using numba.jit for JIT compilation with vectorization
# 3. Using Cython with explicit SIMD pragmas
# 4. Using PyTorch or TensorFlow for GPU acceleration

def sum_i32(arr):
    """Sum of int32 array (NumPy equivalent of SIMD sum)"""
    return np.sum(arr, dtype=np.int32)

def example_with_numba():
    """
    For JIT compilation with auto-vectorization, use numba:

    from numba import jit, vectorize

    @jit(nopython=True)
    def fast_function(a, b):
        result = 0
        for i in range(len(a)):
            if a[i] < b[i]:
                result += a[i] * b[i]
        return result

    @vectorize(['int32(int32, int32)'])
    def vectorized_func(a, b):
        return a + b if a < b else 0
    """
    pass
