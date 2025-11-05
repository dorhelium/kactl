import sys
import random
from various.LIS import lis

def naive_lis(v):
    """Naive LIS for verification - tries all subsequences"""
    n = len(v)
    best_len = 0
    best_indices = []

    # Try all possible subsequences
    for mask in range(1 << n):
        indices = [i for i in range(n) if mask & (1 << i)]
        if not indices:
            continue

        # Check if strictly increasing
        is_valid = True
        for j in range(len(indices) - 1):
            if v[indices[j]] >= v[indices[j + 1]]:
                is_valid = False
                break

        if is_valid and len(indices) > best_len:
            best_len = len(indices)
            best_indices = indices

    return best_indices

def test_lis():
    random.seed(42)

    # Test empty sequence
    assert lis([]) == []

    # Test single element
    assert lis([5]) == [0]

    # Test strictly increasing sequence
    result = lis([1, 2, 3, 4, 5])
    assert len(result) == 5
    for i in range(len(result) - 1):
        assert result[i] < result[i + 1]

    # Test strictly decreasing sequence
    result = lis([5, 4, 3, 2, 1])
    assert len(result) == 1

    # Test known examples
    result = lis([3, 1, 4, 1, 5, 9, 2, 6])
    values = [v for i, v in enumerate([3, 1, 4, 1, 5, 9, 2, 6]) if i in result]
    # Check that result is strictly increasing
    for i in range(len(values) - 1):
        assert values[i] < values[i + 1]

    # Stress test with random small sequences
    for _ in range(10000):
        n = random.randint(0, 7)
        v = [random.randint(0, 3) for _ in range(n)]

        inds = lis(v)

        # Verify that result is strictly increasing
        for i in range(len(inds) - 1):
            assert v[inds[i]] < v[inds[i + 1]], \
                f"Result not strictly increasing at position {i}"

        # Verify that this is actually the longest
        expected = naive_lis(v)
        assert len(inds) == len(expected), \
            f"LIS length mismatch: got {len(inds)}, expected {len(expected)} for sequence {v}"

    # Test with larger sequences
    for _ in range(1000):
        n = random.randint(10, 50)
        v = [random.randint(0, 20) for _ in range(n)]

        inds = lis(v)

        # Verify that result is strictly increasing
        for i in range(len(inds) - 1):
            assert v[inds[i]] < v[inds[i + 1]]

        # Verify indices are in increasing order
        for i in range(len(inds) - 1):
            assert inds[i] < inds[i + 1]

    # Test with duplicates
    result = lis([1, 2, 2, 3, 4])
    values = [v for i, v in enumerate([1, 2, 2, 3, 4]) if i in result]
    for i in range(len(values) - 1):
        assert values[i] < values[i + 1], "Should be strictly increasing"

    print("Tests passed!")

if __name__ == "__main__":
    test_lis()
