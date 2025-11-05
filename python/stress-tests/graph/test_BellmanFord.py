import sys
import random
from graph.BellmanFord import bellman_ford, Node, Ed, INF

def dijkstra(adj, s):
    """Simple Dijkstra for reference (only works with non-negative weights)"""
    n = len(adj)
    dist = [INF] * n
    dist[s] = 0
    visited = [False] * n

    for _ in range(n):
        u = -1
        for v in range(n):
            if not visited[v] and (u == -1 or dist[v] < dist[u]):
                u = v
        if dist[u] == INF:
            break
        visited[u] = True
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist

def test_bellman_ford():
    random.seed(42)

    # Test 1: Simple paths with non-negative weights
    for _ in range(1000):
        n = random.randint(2, 15)
        m = random.randint(0, min(30, n * (n - 1) // 2))

        # Create adjacency list for Dijkstra
        adj = [[] for _ in range(n)]

        # Create nodes and edges for BellmanFord
        nodes = [Node() for _ in range(n)]
        edges = []

        for _ in range(m):
            a = random.randint(0, n - 1)
            b = random.randint(0, n - 1)
            if a != b:
                w = random.randint(1, 10)
                adj[a].append((b, w))
                edges.append(Ed(a, b, w))

        s = random.randint(0, n - 1)

        # Run both algorithms
        bellman_ford(nodes, edges, s)
        dijkstra_dist = dijkstra(adj, s)

        # Compare results
        for i in range(n):
            assert nodes[i].dist == dijkstra_dist[i], \
                f"Distance mismatch for node {i}: BellmanFord={nodes[i].dist}, Dijkstra={dijkstra_dist[i]}"

    # Test 2: Graph with negative weights (but no negative cycles)
    for _ in range(500):
        n = random.randint(2, 10)
        m = random.randint(0, min(20, n * (n - 1) // 2))

        nodes = [Node() for _ in range(n)]
        edges = []

        for _ in range(m):
            a = random.randint(0, n - 1)
            b = random.randint(0, n - 1)
            if a != b:
                w = random.randint(-5, 10)
                edges.append(Ed(a, b, w))

        s = random.randint(0, n - 1)
        bellman_ford(nodes, edges, s)

        # Verify triangle inequality (no negative cycles should be present)
        for ed in edges:
            if nodes[ed.a].dist != INF and nodes[ed.a].dist != -INF:
                if nodes[ed.b].dist != -INF:
                    assert nodes[ed.b].dist <= nodes[ed.a].dist + ed.w + 1e-9, \
                        f"Triangle inequality violated"

    # Test 3: Unreachable nodes
    nodes = [Node() for _ in range(5)]
    edges = [Ed(0, 1, 1), Ed(1, 2, 2)]
    bellman_ford(nodes, edges, 0)
    assert nodes[0].dist == 0
    assert nodes[1].dist == 1
    assert nodes[2].dist == 3
    assert nodes[3].dist == INF
    assert nodes[4].dist == INF

    print("Tests passed!")

if __name__ == "__main__":
    test_bellman_ford()
