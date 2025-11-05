"""
Author: chilli, pajenegod
Date: 2020-02-20
License: CC0
Source: Folklore
Description: Data structure for computing lowest common ancestors in a tree
(with 0 as root). C should be an adjacency list of the tree, either directed
or undirected.
Time: O(N log N + Q)
Status: stress-tested
"""

# Note: This requires RMQ.py from data-structures

class LCA:
    def __init__(self, adj):
        """
        adj: adjacency list of the tree
        """
        self.n = len(adj)
        self.T = 0
        self.time = [0] * self.n
        self.path = []
        self.ret = []
        self.dfs(adj, 0, -1)
        # RMQ would be initialized here: self.rmq = RMQ(self.ret)

    def dfs(self, adj, v, par):
        self.time[v] = self.T
        self.T += 1
        for y in adj[v]:
            if y != par:
                self.path.append(v)
                self.ret.append(self.time[v])
                self.dfs(adj, y, v)

    def lca(self, a, b):
        """
        Find the lowest common ancestor of nodes a and b
        Note: requires RMQ to be implemented
        """
        if a == b:
            return a
        ta, tb = self.time[a], self.time[b]
        if ta > tb:
            ta, tb = tb, ta
        # return self.path[self.rmq.query(ta, tb)]
        # Without RMQ implementation, this is incomplete
        pass

    # def dist(self, a, b, depth):
    #     """Compute distance between nodes a and b given depth array"""
    #     return depth[a] + depth[b] - 2 * depth[self.lca(a, b)]
