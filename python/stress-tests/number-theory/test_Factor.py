import sys
import random
from Factor import factor, is_prime

def assert_valid(n, factors):
    """Verify that factors are all prime and multiply to n"""
    product = 1
    for f in factors:
        assert is_prime(f), f"{f} is not prime in factorization of {n}"
        product *= f
    assert product == n, f"Factors {factors} multiply to {product}, expected {n}"

def test_factor():
    # Test specific known cases
    assert factor(1) == []
    assert factor(2) == [2]
    assert sorted(factor(2299)) == sorted([11, 19, 11])
    assert factor(4) == [2, 2]
    assert factor(6) == [2, 3] or factor(6) == [3, 2]

    # Test small numbers
    for n in range(2, 1000):
        factors = factor(n)
        assert_valid(n, factors)

        # Also test n^2
        factors_sq = factor(n * n)
        assert_valid(n * n, factors_sq)

    # Test some larger numbers
    random.seed(42)
    for _ in range(1000):
        n = random.randint(2, 10**9)
        factors = factor(n)
        assert_valid(n, factors)

    # Test prime powers
    assert sorted(factor(32)) == [2] * 5
    assert sorted(factor(27)) == [3] * 3
    assert sorted(factor(125)) == [5] * 3

    # Test products of two primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for i in range(len(primes)):
        for j in range(i, min(i + 5, len(primes))):
            n = primes[i] * primes[j]
            factors = factor(n)
            assert_valid(n, factors)
            assert sorted(factors) == sorted([primes[i], primes[j]])

    print("Tests passed!")

if __name__ == "__main__":
    test_factor()
