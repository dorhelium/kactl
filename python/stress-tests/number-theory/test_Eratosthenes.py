import sys
from Eratosthenes import eratosthenes_sieve

def naive_primes(lim):
    """Naive prime generation for testing"""
    if lim <= 2:
        return []
    primes = []
    for n in range(2, lim):
        is_prime = True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

def test_eratosthenes():
    # Test small cases
    for lim in range(2, 100):
        primes, is_prime = eratosthenes_sieve(lim)
        expected = naive_primes(lim)
        assert primes == expected, f"Primes up to {lim}: got {primes}, expected {expected}"

        # Verify is_prime array
        for i in range(lim):
            expected_prime = i in primes
            assert is_prime[i] == expected_prime, \
                f"is_prime[{i}] = {is_prime[i]}, expected {expected_prime}"

    # Test larger cases
    for lim in [1000, 5000, 10000]:
        primes, is_prime = eratosthenes_sieve(lim)
        expected = naive_primes(lim)
        assert primes == expected, f"Primes up to {lim} don't match"

    # Test known primes
    primes_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    primes, _ = eratosthenes_sieve(100)
    assert primes == primes_100, "Known primes up to 100 don't match"

    # Edge cases
    primes, _ = eratosthenes_sieve(0)
    assert primes == []

    primes, _ = eratosthenes_sieve(1)
    assert primes == []

    primes, _ = eratosthenes_sieve(2)
    assert primes == []

    primes, _ = eratosthenes_sieve(3)
    assert primes == [2]

    print("Tests passed!")

if __name__ == "__main__":
    test_eratosthenes()
