"""
 * Author: Chen Xing
 * Date: 2009-10-13
 * License: CC0
 * Source: N/A
 * Description: Flow algorithm with guaranteed complexity O(VE^2). To get edge flow values, compare
 * capacities before and after, and take the positive values only.
 * Status: stress-tested

"""

def edmonds_karp(graph, source, sink):
    """
    Compute max flow from source to sink.
    graph: list of dicts where graph[i][j] = capacity from i to j
    Returns: max flow value
    """
    assert source != sink

    n = len(graph)
    flow = 0
    par = [-1] * n
    q = [0] * n

    while True:
        # BFS to find augmenting path
        par = [-1] * n
        par[source] = source
        ptr = 1
        q[0] = source

        for i in range(ptr):
            x = q[i]
            for dest, cap in graph[x].items():
                if par[dest] == -1 and cap > 0:
                    par[dest] = x
                    q[ptr] = dest
                    ptr += 1
                    if dest == sink:
                        break

        # No more augmenting paths
        if par[sink] == -1:
            return flow

        # Find minimum capacity along path
        inc = float('inf')
        y = sink
        while y != source:
            inc = min(inc, graph[par[y]][y])
            y = par[y]

        # Update capacities
        flow += inc
        y = sink
        while y != source:
            p = par[y]
            graph[p][y] -= inc
            if graph[p][y] <= 0:
                del graph[p][y]
            if y not in graph[y]:
                graph[y][p] = 0
            graph[y][p] += inc
            y = p
