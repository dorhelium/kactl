import sys
import random
from ModPow import mod_pow

def test_mod_pow():
    # Test small cases exhaustively
    for mod in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        for base in range(mod):
            for exp in range(20):
                result = mod_pow(base, exp, mod)
                expected = pow(base, exp, mod)
                assert result == expected, \
                    f"mod_pow({base}, {exp}, {mod}) = {result}, expected {expected}"

    # Test with larger modulo
    mod = 1000000007
    random.seed(42)

    for _ in range(10000):
        base = random.randint(0, mod - 1)
        exp = random.randint(0, 10**9)
        result = mod_pow(base, exp, mod)
        expected = pow(base, exp, mod)
        assert result == expected, \
            f"mod_pow({base}, {exp}, {mod}) = {result}, expected {expected}"

    # Test edge cases
    assert mod_pow(0, 0, 7) == 1
    assert mod_pow(0, 5, 7) == 0
    assert mod_pow(1, 1000000, 7) == 1
    assert mod_pow(2, 0, 7) == 1

    # Test powers of 2
    base = 2
    mod = 1000000007
    cur = 1
    for i in range(30):
        result = mod_pow(base, i, mod)
        assert result == cur, f"2^{i} mod {mod} = {result}, expected {cur}"
        cur = (cur * 2) % mod

    print("Tests passed!")

if __name__ == "__main__":
    test_mod_pow()
