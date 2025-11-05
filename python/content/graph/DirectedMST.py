"""
Author: chilli, Takanori MAEHARA, Benq, Simon Lindholm
Date: 2019-05-10
License: CC0
Source: https://github.com/spaghetti-source/algorithm/blob/master/graph/arborescence.cc
and https://github.com/bqi343/USACO/blob/42d177dfb9d6ce350389583cfa71484eb8ae614c/Implementations/content/graphs%20(12)/Advanced/DirectedMST.h for the reconstruction
Description: Finds a minimum spanning
tree/arborescence of a directed graph, given a root node. If no MST exists, returns -1.
Time: O(E log V)
Status: Stress-tested, also tested on NWERC 2018 fastestspeedrun
"""

# Note: This requires UnionFindRollback.py from data-structures
# The implementation below shows the structure but requires UnionFind with rollback

from collections import deque

class Edge:
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

class Node:
    """Lazy skew heap node"""
    def __init__(self, key):
        self.key = key
        self.l = None
        self.r = None
        self.delta = 0

    def prop(self):
        """Propagate lazy delta"""
        self.key.w += self.delta
        if self.l:
            self.l.delta += self.delta
        if self.r:
            self.r.delta += self.delta
        self.delta = 0

    def top(self):
        self.prop()
        return self.key

def merge(a, b):
    """Merge two skew heaps"""
    if not a or not b:
        return a if a else b
    a.prop()
    b.prop()
    if a.key.w > b.key.w:
        a, b = b, a
    a.l, a.r = merge(b, a.r), a.l
    return a

def pop(a):
    """Pop from skew heap"""
    a.prop()
    return merge(a.l, a.r)

def dmst(n, r, edges):
    """
    Find directed MST rooted at r.
    n: number of vertices
    r: root vertex
    edges: list of Edge objects
    Returns: (cost, parent_array) or (-1, []) if no MST exists

    Note: Requires UnionFindRollback implementation
    """
    # This is a placeholder showing the algorithm structure
    # Full implementation requires UnionFindRollback

    # uf = RollbackUF(n)
    heap = [None] * n

    for e in edges:
        heap[e.b] = merge(heap[e.b], Node(e))

    res = 0
    seen = [-1] * n
    path = [0] * n
    par = [0] * n
    seen[r] = r

    Q = [None] * n
    in_edge = [Edge(-1, -1, 0) for _ in range(n)]
    comp = []
    cycs = deque()

    for s in range(n):
        u = s
        qi = 0

        while seen[u] < 0:
            if not heap[u]:
                return (-1, [])

            e = heap[u].top()
            heap[u].delta -= e.w
            heap[u] = pop(heap[u])

            Q[qi] = e
            path[qi] = u
            qi += 1
            seen[u] = s
            res += e.w
            # u = uf.find(e.a)  # Requires UnionFind

            # if seen[u] == s:  # found cycle, contract
            #     # Contract cycle logic
            #     pass

        for i in range(qi):
            pass  # in_edge[uf.find(Q[i].b)] = Q[i]

    # Restore solution (optional)
    # for u, t, comp in cycs:
    #     # Restoration logic
    #     pass

    # for i in range(n):
    #     par[i] = in_edge[i].a

    # return (res, par)

    raise NotImplementedError("Requires UnionFindRollback.py implementation")
