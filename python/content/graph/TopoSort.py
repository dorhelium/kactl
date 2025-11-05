"""
Author: Unknown
Date: 2002-09-13
Source: predates tinyKACTL
Description: Topological sorting. Given is an oriented graph.
Output is an ordering of vertices, such that there are edges only from left to right.
If there are cycles, the returned list will have size smaller than n -- nodes reachable
from cycles will not be returned.
Time: O(|V|+|E|)
Status: stress-tested
"""

def topo_sort(gr):
    """
    gr: adjacency list (list of lists)
    Returns: topologically sorted list of vertices
    """
    indeg = [0] * len(gr)
    for li in gr:
        for x in li:
            indeg[x] += 1

    q = []
    for i in range(len(gr)):
        if indeg[i] == 0:
            q.append(i)

    j = 0
    while j < len(q):
        for x in gr[q[j]]:
            indeg[x] -= 1
            if indeg[x] == 0:
                q.append(x)
        j += 1

    return q
