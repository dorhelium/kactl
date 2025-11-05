import sys
import random
from numerical.Determinant import det

def naive_det(a):
    """Naive determinant calculation for small matrices"""
    n = len(a)
    if n == 0:
        return 1
    if n == 1:
        return a[0][0]
    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if n == 3:
        return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) -
                a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0]) +
                a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))

    # For larger matrices, use Laplace expansion (slow but correct)
    result = 0
    for j in range(n):
        # Create submatrix without row 0 and column j
        submatrix = [[a[i][k] for k in range(n) if k != j] for i in range(1, n)]
        cofactor = ((-1) ** j) * a[0][j] * naive_det(submatrix)
        result += cofactor
    return result

def test_determinant():
    random.seed(42)

    # Test known matrices
    # Identity matrices
    for n in range(1, 6):
        mat = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
        assert abs(det([row[:] for row in mat]) - 1.0) < 1e-9

    # Zero matrices
    for n in range(1, 6):
        mat = [[0.0 for j in range(n)] for i in range(n)]
        assert abs(det([row[:] for row in mat])) < 1e-9

    # Test 2x2 matrices
    for _ in range(100):
        mat = [[random.uniform(-10, 10) for j in range(2)] for i in range(2)]
        expected = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        result = det([row[:] for row in mat])
        assert abs(expected - result) < 1e-6, f"2x2 determinant failed"

    # Test 3x3 matrices
    for _ in range(100):
        mat = [[random.uniform(-10, 10) for j in range(3)] for i in range(3)]
        expected = naive_det(mat)
        result = det([row[:] for row in mat])
        assert abs(expected - result) < 1e-6, f"3x3 determinant failed"

    # Test larger random matrices against naive implementation
    for n in [4, 5]:
        for _ in range(20):
            mat = [[random.uniform(-5, 5) for j in range(n)] for i in range(n)]
            expected = naive_det(mat)
            result = det([row[:] for row in mat])
            assert abs(expected - result) < 1e-4, \
                f"Determinant failed for {n}x{n} matrix: expected {expected}, got {result}"

    # Test singular matrices (determinant should be 0)
    for n in range(2, 6):
        mat = [[float(i + j) for j in range(n)] for i in range(n)]
        result = det([row[:] for row in mat])
        assert abs(result) < 1e-6, f"Singular matrix should have det = 0, got {result}"

    # Test diagonal matrices
    for n in range(1, 6):
        diag = [random.uniform(1, 10) for _ in range(n)]
        mat = [[diag[i] if i == j else 0.0 for j in range(n)] for i in range(n)]
        expected = 1.0
        for d in diag:
            expected *= d
        result = det([row[:] for row in mat])
        assert abs(expected - result) < 1e-6

    print("Tests passed!")

if __name__ == "__main__":
    test_determinant()
