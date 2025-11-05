import sys
import random
from graph.Dinic import Dinic

def edmonds_karp(graph, s, t):
    """Simple EdmondsKarp for reference"""
    n = len(graph)

    def bfs():
        parent = [-1] * n
        visited = [False] * n
        visited[s] = True
        queue = [s]
        idx = 0

        while idx < len(queue):
            u = queue[idx]
            idx += 1

            for v in range(n):
                if not visited[v] and graph[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == t:
                        return parent
        return None

    flow = 0
    while True:
        parent = bfs()
        if parent is None:
            break

        # Find minimum capacity along path
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u

        # Update capacities
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

        flow += path_flow

    return flow

def test_dinic():
    random.seed(123)

    for _ in range(50000):
        n = 2 + random.randint(0, 9)
        s = random.randint(0, n - 1)
        t = random.randint(0, n - 2)
        if t >= s:
            t += 1

        dinic = Dinic(n)
        graph = [[0] * n for _ in range(n)]

        m = random.randint(0, 39)
        for _ in range(m):
            a = random.randint(0, n - 1)
            b = random.randint(0, n - 1)
            c = random.randint(0, 3)
            d = random.randint(0, 2) if random.randint(0, 3) == 0 else 0

            dinic.add_edge(a, b, c, d)
            graph[a][b] += c
            graph[b][a] += d

        # Copy graph for EdmondsKarp
        graph_copy = [row[:] for row in graph]

        dinic_flow = dinic.calc(s, t)
        ek_flow = edmonds_karp(graph_copy, s, t)

        assert dinic_flow == ek_flow, f"Flow mismatch: Dinic={dinic_flow}, EK={ek_flow}"

        # Verify conservation of flow
        flows = [0] * n
        for i in range(n):
            for e in dinic.adj[i]:
                if e.flow() > 0:
                    assert e.c >= 0, "Negative capacity"
                    flows[i] += e.flow()
                    flows[e.to] -= e.flow()

        assert flows[s] == dinic_flow, f"Source flow mismatch"
        assert flows[t] == -dinic_flow, f"Sink flow mismatch"

        for i in range(n):
            if i != s and i != t:
                assert flows[i] == 0, f"Flow conservation violated at node {i}"

        # Verify min cut
        assert dinic.left_of_min_cut(s), "Source not on left of cut"
        assert not dinic.left_of_min_cut(t), "Sink on left of cut"

        across_cut = 0
        for i in range(n):
            for e in dinic.adj[i]:
                if dinic.left_of_min_cut(i) and not dinic.left_of_min_cut(e.to):
                    assert e.c == 0, "Unsaturated edge across cut"
                    across_cut += e.flow()

        assert across_cut == dinic_flow, "Min cut != max flow"

    print("Tests passed!")

if __name__ == "__main__":
    test_dinic()
