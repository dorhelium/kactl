import sys
import random
from Treap import Node, cnt, merge, split, move, each

def split2(n, v):
    """Split by value instead of count"""
    if not n:
        return None, None
    if n.val >= v:
        pa = split2(n.l, v)
        n.l = pa[1]
        n.recalc()
        return pa[0], n
    else:
        pa = split2(n.r, v)
        n.r = pa[0]
        n.recalc()
        return n, pa[1]

class RandomGen:
    def __init__(self):
        self.x = 0

    def ra(self):
        self.x = (self.x * 4176481 + 193861934) & 0xFFFFFFFF
        return self.x >> 1

def test_treap():
    random.seed(3)
    rg = RandomGen()

    # Test split by value
    for _ in range(1000):
        nodes = [Node(i * 2 + 2) for i in range(10)]
        exp = [i * 2 + 2 for i in range(10)]

        n = None
        for node in nodes:
            n = merge(n, node)

        v = random.randint(0, 24)
        left = cnt(split2(n, v)[0])
        rleft = sum(1 for x in exp if x < v)
        assert left == rleft, f"Split test failed: expected {rleft}, got {left}"

    # Test move operation
    for _ in range(10000):
        nodes = [Node(i) for i in range(10)]
        exp = list(range(10))

        n = None
        for node in nodes:
            n = merge(n, node)

        i = rg.ra() % 11
        j = rg.ra() % 11
        if i > j:
            i, j = j, i
        k = rg.ra() % 11
        if i < k < j:
            continue

        n = move(n, i, j, k)

        nk = k - (j - i) if k >= j else k
        iv = exp[i:j]
        exp = exp[:i] + exp[j:]
        exp = exp[:nk] + iv + exp[nk:]

        result = []
        each(n, lambda x: result.append(x))

        assert result == exp, f"Move test failed: expected {exp}, got {result}"

    print("Tests passed!")

if __name__ == "__main__":
    test_treap()
