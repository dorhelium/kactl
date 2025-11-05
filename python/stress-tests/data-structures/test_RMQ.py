import sys
import random
from RMQ import RMQ

def test_rmq():
    random.seed(2)
    for N in range(100):
        v = list(range(N))
        random.shuffle(v)
        rmq = RMQ(v)

        for i in range(N):
            for j in range(i + 1, N + 1):
                m = rmq.query(i, j)
                n = float('inf')
                for k in range(i, j):
                    n = min(n, v[k])
                assert n == m, f"RMQ test failed: expected {n}, got {m} for range [{i}, {j})"

    print("Tests passed!")

if __name__ == "__main__":
    test_rmq()
