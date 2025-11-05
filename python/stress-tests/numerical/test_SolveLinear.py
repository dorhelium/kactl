import sys
import random
from numerical.SolveLinear import solve_linear, EPS

def test_solve_linear():
    random.seed(42)

    # Test 1: Simple 2x2 system with unique solution
    # 2x + 3y = 8
    # x + y = 3
    # Solution: x=1, y=2
    A = [[2.0, 3.0], [1.0, 1.0]]
    b = [8.0, 3.0]
    x = [0.0, 0.0]
    rank = solve_linear(A, b, x)
    assert rank == 2, "Should have unique solution"
    assert abs(x[0] - 1.0) < EPS and abs(x[1] - 2.0) < EPS, f"Wrong solution: {x}"

    # Test 2: 3x3 system with unique solution
    A = [[2.0, 1.0, -1.0],
         [-3.0, -1.0, 2.0],
         [-2.0, 1.0, 2.0]]
    b = [8.0, -11.0, -3.0]
    x = [0.0, 0.0, 0.0]
    rank = solve_linear(A, b, x)
    assert rank == 3, "Should have unique solution"

    # Verify solution
    A_orig = [[2.0, 1.0, -1.0],
              [-3.0, -1.0, 2.0],
              [-2.0, 1.0, 2.0]]
    b_orig = [8.0, -11.0, -3.0]
    for i in range(3):
        result = sum(A_orig[i][j] * x[j] for j in range(3))
        assert abs(result - b_orig[i]) < 1e-6, f"Solution verification failed at row {i}"

    # Test 3: Inconsistent system (no solution)
    A = [[1.0, 2.0],
         [2.0, 4.0]]
    b = [3.0, 7.0]  # Inconsistent: second equation should be 6.0 for consistency
    x = [0.0, 0.0]
    rank = solve_linear(A, b, x)
    assert rank == -1, "Should have no solution"

    # Test 4: Underdetermined system (infinite solutions)
    A = [[1.0, 2.0, 3.0],
         [2.0, 4.0, 6.0]]
    b = [6.0, 12.0]
    x = [0.0, 0.0, 0.0]
    rank = solve_linear(A, b, x)
    assert rank < 3, "Should have infinite solutions (rank < m)"

    # Verify that the returned solution works
    A_orig = [[1.0, 2.0, 3.0],
              [2.0, 4.0, 6.0]]
    b_orig = [6.0, 12.0]
    for i in range(2):
        result = sum(A_orig[i][j] * x[j] for j in range(3))
        assert abs(result - b_orig[i]) < 1e-6

    # Test 5: Random systems
    for _ in range(100):
        n = random.randint(2, 5)
        m = n

        # Create a well-conditioned system
        A = [[random.uniform(-10, 10) for j in range(m)] for i in range(n)]
        x_true = [random.uniform(-5, 5) for j in range(m)]
        b = [sum(A[i][j] * x_true[j] for j in range(m)) for i in range(n)]

        # Make copies for solving
        A_copy = [row[:] for row in A]
        b_copy = b[:]
        x = [0.0] * m

        rank = solve_linear(A_copy, b_copy, x)

        if rank == m:
            # Verify solution
            for i in range(n):
                result = sum(A[i][j] * x[j] for j in range(m))
                assert abs(result - b[i]) < 1e-4, "Solution verification failed"

    # Test 6: Identity matrix
    A = [[1.0, 0.0, 0.0],
         [0.0, 1.0, 0.0],
         [0.0, 0.0, 1.0]]
    b = [1.0, 2.0, 3.0]
    x = [0.0, 0.0, 0.0]
    rank = solve_linear(A, b, x)
    assert rank == 3
    assert abs(x[0] - 1.0) < EPS and abs(x[1] - 2.0) < EPS and abs(x[2] - 3.0) < EPS

    print("Tests passed!")

if __name__ == "__main__":
    test_solve_linear()
