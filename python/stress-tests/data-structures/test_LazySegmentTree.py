import sys
import random
from LazySegmentTree import Node, INF

class RandomGen:
    def __init__(self):
        self.R = 0

    def ra(self):
        self.R = (self.R * 791231 + 1231) & 0xFFFFFFFF
        return self.R >> 1

def test_lazy_segment_tree():
    rg = RandomGen()

    N = 10
    v = list(range(N))
    random.shuffle(v)

    tr = Node(0, N, v)

    # Test initial queries
    for i in range(N):
        for j in range(N):
            if i <= j:
                ma = -INF
                for k in range(i, j):
                    ma = max(ma, v[k])
                assert ma == tr.query(i, j), f"Initial query failed at [{i}, {j})"

    # Test operations
    for _ in range(1000000):
        i = rg.ra() % (N + 1)
        j = rg.ra() % (N + 1)
        if i > j:
            i, j = j, i
        x = (rg.ra() % 10) - 5

        r = rg.ra() % 100
        if r < 30:
            # Query
            result = tr.query(i, j)
            ma = -INF
            for k in range(i, j):
                ma = max(ma, v[k])
            assert ma == result, f"Query failed: expected {ma}, got {result} for range [{i}, {j})"
        elif r < 70:
            # Add
            tr.add(i, j, x)
            for k in range(i, j):
                v[k] += x
        else:
            # Set
            tr.set(i, j, x)
            for k in range(i, j):
                v[k] = x

    print("Tests passed!")

if __name__ == "__main__":
    test_lazy_segment_tree()
