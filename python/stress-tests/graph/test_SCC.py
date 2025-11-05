import sys
import random
from graph.SCC import scc, comp, ncomps

def old_scc(g):
    """Old reference implementation for testing"""
    n = len(g)
    orig = [0] * n
    low = [0] * n
    comp_old = [-1] * n
    z_old = []
    no_vertices = 0
    no_components = 0

    def dfs(j):
        nonlocal no_vertices, no_components
        low[j] = orig[j] = no_vertices
        no_vertices += 1
        comp_old[j] = -2
        z_old.append(j)

        for e in g[j]:
            if comp_old[e] == -1:
                dfs(e)
                low[j] = min(low[j], low[e])
            elif comp_old[e] == -2:
                low[j] = min(low[j], orig[e])

        if orig[j] == low[j]:
            while True:
                x = z_old.pop()
                comp_old[x] = no_components
                if x == j:
                    break
            no_components += 1

    for i in range(n):
        if comp_old[i] == -1:
            dfs(i)

    return comp_old

def test_scc():
    global comp, ncomps

    r = 1
    for N in range(5):
        adj = [[] for _ in range(N)]
        seen = [0] * N
        count = 0

        for bits in range(1 << (N * N)):
            # Build adjacency list
            for i in range(N):
                adj[i].clear()
                for j in range(N):
                    if bits & (1 << (i * N + j)):
                        adj[i].append(j)
                        r = (r * 12387123 + 1231) & 0xFFFFFFFF
                        # Sometimes add duplicate edges
                        if ((r >> 6) & 31) == 3:
                            adj[i].append(j)

            # Run both implementations
            comp2 = old_scc(adj)
            compsize = [0] * N

            scc(adj, lambda v: None)

            # Compare results
            for i in range(N):
                assert comp[i] >= 0 and comp[i] < ncomps, f"Component out of bounds"

            # Check that edges only go to same or lower components
            for i in range(N):
                for j in adj[i]:
                    assert comp[j] <= comp[i], f"Edge from {i} to {j} violates topological order"

            # Check reachability
            for i in range(N):
                seen = [0] * N
                seen[i] = 1
                # Compute reachability
                for _ in range(N):
                    for j in range(N):
                        if seen[j]:
                            for k in adj[j]:
                                seen[k] = 1

                for j in range(N):
                    if seen[j]:
                        assert comp[j] <= comp[i], f"Reachable node {j} from {i} has higher component"
                    else:
                        assert comp[j] != comp[i], f"Non-reachable node {j} in same component as {i}"

            count += 1

    print("Tests passed!")

if __name__ == "__main__":
    test_scc()
