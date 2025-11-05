import sys
import random
from FenwickTree2d import FT2

def test_fenwick_tree_2d():
    for _ in range(1000000):
        ft = FT2(12)
        upd = []

        c = random.randint(0, 19)
        for _ in range(c):
            upd.append((random.randint(0, 11), random.randint(0, 11), random.randint(-5, 4)))

        grid = [[0] * 12 for _ in range(12)]
        sumto = [[0] * 13 for _ in range(13)]

        # Fake updates to register coordinates
        for x, y, _ in upd:
            ft.fake_update(x, y)

        ft.init()

        # Apply updates
        for x, y, val in upd:
            grid[x][y] += val
            ft.update(x, y, val)

        # Verify queries
        for i in range(13):
            for j in range(13):
                v = ft.query(i, j)
                if i == 0 or j == 0:
                    assert v == 0, f"Query at ({i}, {j}) should be 0, got {v}"
                else:
                    sumto[i][j] = (grid[i-1][j-1] + sumto[i-1][j] +
                                   sumto[i][j-1] - sumto[i-1][j-1])
                    assert v == sumto[i][j], f"Query at ({i}, {j}): expected {sumto[i][j]}, got {v}"

    print("Tests passed!")

if __name__ == "__main__":
    test_fenwick_tree_2d()
