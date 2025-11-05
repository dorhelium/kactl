import sys
import random
from FenwickTree import FT

def test_fenwick_tree():
    for it in range(100000):
        N = random.randint(0, 9)
        fw = FT(N)
        t = [0] * N

        for i in range(N):
            v = random.randint(0, 2)
            fw.update(i, v)
            t[i] += v

        q = random.randint(0, 19)
        ind = fw.lower_bound(q)

        res = -1
        sum_val = 0
        for i in range(N + 1):
            if sum_val < q:
                res = i
            if i != N:
                sum_val += t[i]

        assert res == ind, f"Failed: expected {res}, got {ind}"

    print("Tests passed!")

if __name__ == "__main__":
    test_fenwick_tree()
