import sys
import random
import math
from euclid import euclid

def test_euclid():
    random.seed(42)

    # Test that ax + by = gcd(a, b)
    for _ in range(10000):
        a = random.randint(1, 10000)
        b = random.randint(1, 10000)

        g, x, y = euclid(a, b)

        # Check that g is actually the gcd
        expected_gcd = math.gcd(a, b)
        assert g == expected_gcd, f"euclid({a}, {b}) returned gcd={g}, expected {expected_gcd}"

        # Check that ax + by = gcd
        assert a * x + b * y == g, f"euclid({a}, {b}): {a}*{x} + {b}*{y} = {a*x + b*y}, expected {g}"

    # Test with one number being zero
    g, x, y = euclid(5, 0)
    assert g == 5 and x == 1 and y == 0

    g, x, y = euclid(0, 7)
    assert g == 7 and 0 * x + 7 * y == 7

    # Test coprime numbers (modular inverse)
    for _ in range(1000):
        a = random.randint(2, 1000)
        # Find a coprime b
        b = random.randint(2, 1000)
        while math.gcd(a, b) != 1:
            b = random.randint(2, 1000)

        g, x, y = euclid(a, b)
        assert g == 1, f"Numbers {a} and {b} should be coprime"

        # x should be the inverse of a mod b
        assert (a * x) % b == 1, f"x={x} is not the inverse of {a} mod {b}"

    # Test specific known cases
    g, x, y = euclid(10, 6)
    assert g == 2
    assert 10 * x + 6 * y == 2

    g, x, y = euclid(35, 15)
    assert g == 5
    assert 35 * x + 15 * y == 5

    g, x, y = euclid(17, 13)
    assert g == 1
    assert 17 * x + 13 * y == 1

    print("Tests passed!")

if __name__ == "__main__":
    test_euclid()
