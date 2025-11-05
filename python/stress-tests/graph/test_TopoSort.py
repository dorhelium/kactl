import sys
import random
from graph.TopoSort import topo_sort

def test_topo_sort():
    for _ in range(50000):
        n = random.randint(0, 19)
        m = random.randint(0, 29) if n else 0
        acyclic = random.choice([True, False])

        order = list(range(n))
        random.shuffle(order)
        ed = [[] for _ in range(n)]

        for _ in range(m):
            a = random.randint(0, n - 1) if n else 0
            b = random.randint(0, n - 1) if n else 0
            if acyclic and a >= b:
                continue
            ed[order[a]].append(order[b])

        ret = topo_sort(ed)

        if acyclic:
            assert len(ret) == n, f"Acyclic graph should have all {n} nodes, got {len(ret)}"
        else:
            assert len(ret) <= n, f"Cyclic graph should have at most {n} nodes, got {len(ret)}"

        seen = [False] * n
        for i in ret:
            assert not seen[i], f"Node {i} visited twice"
            seen[i] = True
            for j in ed[i]:
                assert not seen[j], f"Edge {i}->{j} violates topological order"

    print("Tests passed!")

if __name__ == "__main__":
    test_topo_sort()
