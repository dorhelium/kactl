import sys
import random
from SegmentTree import Tree

def test_segment_tree():
    # Test empty tree
    t = Tree(0)
    assert t.query(0, 0) == t.unit

    # Test with maximum operation
    for n in range(1, 10):
        tr = Tree(n)
        v = [float('-inf')] * n

        for _ in range(100000):
            i = random.randint(0, n)
            j = random.randint(0, n)
            x = random.randint(0, n + 1)

            r = random.randint(0, 99)
            if r < 30:
                # Query
                ma = float('-inf')
                for k in range(i, j):
                    ma = max(ma, v[k])
                assert ma == tr.query(i, j), f"Query failed: expected {ma}, got {tr.query(i, j)}"
            else:
                # Update
                i = min(i, n - 1)
                tr.update(i, x)
                v[i] = x

    print("Tests passed!")

if __name__ == "__main__":
    test_segment_tree()
