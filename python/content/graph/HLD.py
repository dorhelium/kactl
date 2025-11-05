"""
 * Author: Benjamin Qi, Oleksandr Kulkov, chilli
 * Date: 2020-01-12
 * License: CC0
 * Source: https://codeforces.com/blog/entry/53170, https://github.com/bqi343/USACO/blob/master/Implementations/content/graphs%20(12)/Trees%20(10)/HLD%20(10.3).h
 * Description: Decomposes a tree into vertex disjoint heavy paths and light
 * edges such that the path from any leaf to the root contains at most log(n)
 * light edges. Code does additive modifications and max queries, but can
 * support commutative segtree modifications/queries on paths and subtrees.
 * Takes as input the full adjacency list. vals_edges being True means that
 * values are stored in the edges, as opposed to the nodes. All values
 * initialized to the segtree default. Root must be 0.
 * Time: O((log N)^2)
 * Status: stress-tested against old HLD

"""

# Note: This requires LazySegmentTree.py from data-structures

class HLD:
    def __init__(self, adj, vals_edges=False):
        """
        adj: adjacency list of the tree
        vals_edges: True if values are on edges, False if on vertices
        """
        self.N = len(adj)
        self.vals_edges = vals_edges
        self.tim = 0
        self.adj = [list(neighbors) for neighbors in adj]
        self.par = [-1] * self.N
        self.siz = [1] * self.N
        self.rt = [0] * self.N
        self.pos = [0] * self.N
        # self.tree = LazySegmentTree(0, self.N)  # Requires LazySegmentTree

        self.dfs_sz(0)
        self.dfs_hld(0)

    def dfs_sz(self, v):
        for i in range(len(self.adj[v])):
            u = self.adj[v][i]
            # Remove parent edge from child's adjacency list
            if v in self.adj[u]:
                self.adj[u].remove(v)
            self.par[u] = v
            self.dfs_sz(u)
            self.siz[v] += self.siz[u]
            # Put heaviest child first
            if self.siz[u] > self.siz[self.adj[v][0]]:
                self.adj[v][i], self.adj[v][0] = self.adj[v][0], self.adj[v][i]

    def dfs_hld(self, v):
        self.pos[v] = self.tim
        self.tim += 1
        for i, u in enumerate(self.adj[v]):
            # Heavy child gets same root, light child becomes new root
            self.rt[u] = self.rt[v] if i == 0 else u
            self.dfs_hld(u)

    def process(self, u, v, op):
        """Process path from u to v with operation op"""
        while True:
            if self.pos[u] > self.pos[v]:
                u, v = v, u
            if self.rt[u] == self.rt[v]:
                break
            op(self.pos[self.rt[v]], self.pos[v] + 1)
            v = self.par[self.rt[v]]
        op(self.pos[u] + self.vals_edges, self.pos[v] + 1)

    def modify_path(self, u, v, val):
        """Add val to all nodes/edges on path from u to v"""
        # self.process(u, v, lambda l, r: self.tree.add(l, r, val))
        pass  # Requires LazySegmentTree implementation

    def query_path(self, u, v):
        """Query max on path from u to v (modify depending on problem)"""
        res = -10**9
        # def op(l, r):
        #     nonlocal res
        #     res = max(res, self.tree.query(l, r))
        # self.process(u, v, op)
        # return res
        pass  # Requires LazySegmentTree implementation

    def query_subtree(self, v):
        """Query subtree rooted at v"""
        # return self.tree.query(self.pos[v] + self.vals_edges,
        #                        self.pos[v] + self.siz[v])
        pass  # Requires LazySegmentTree implementation
