"""
 * Author: Stanford
 * Date: Unknown
 * Source: Stanford Notebook
 * Description: Min-cost max-flow.
 * If costs can be negative, call setpi before maxflow, but note that negative cost cycles are not supported.
 * To obtain the actual flow, look at positive values only.
 * Status: Tested on kattis:mincostmaxflow, stress-tested against another implementation
 * Time: O(F E log(V)) where F is max flow. O(VE) for setpi.

"""

import heapq

INF = 10**18

class MCMF:
    class Edge:
        def __init__(self, from_node, to, rev, cap, cost):
            self.from_node = from_node
            self.to = to
            self.rev = rev
            self.cap = cap
            self.cost = cost
            self.flow = 0

    def __init__(self, n):
        self.N = n
        self.ed = [[] for _ in range(n)]
        self.seen = [0] * n
        self.dist = [0] * n
        self.pi = [0] * n
        self.par = [None] * n

    def add_edge(self, from_node, to, cap, cost):
        """Add edge from from_node to with capacity cap and cost"""
        if from_node == to:
            return
        self.ed[from_node].append(MCMF.Edge(from_node, to, len(self.ed[to]), cap, cost))
        self.ed[to].append(MCMF.Edge(to, from_node, len(self.ed[from_node]) - 1, 0, -cost))

    def path(self, s):
        """Find shortest path using Dijkstra with potentials"""
        self.seen = [0] * self.N
        self.dist = [INF] * self.N
        self.dist[s] = 0

        # Priority queue: (distance, node)
        pq = [(0, s)]

        while pq:
            d, v = heapq.heappop(pq)
            if self.seen[v]:
                continue
            self.seen[v] = 1
            di = self.dist[v] + self.pi[v]

            for e in self.ed[v]:
                if not self.seen[e.to]:
                    val = di - self.pi[e.to] + e.cost
                    if e.cap - e.flow > 0 and val < self.dist[e.to]:
                        self.dist[e.to] = val
                        self.par[e.to] = e
                        heapq.heappush(pq, (val, e.to))

        for i in range(self.N):
            self.pi[i] = min(self.pi[i] + self.dist[i], INF)

    def maxflow(self, s, t):
        """Compute min-cost max-flow from s to t. Returns (flow, cost)"""
        totflow = 0
        totcost = 0

        while True:
            self.path(s)
            if not self.seen[t]:
                break

            # Find minimum capacity along path
            fl = INF
            x = self.par[t]
            while x:
                fl = min(fl, x.cap - x.flow)
                x = self.par[x.from_node]

            totflow += fl

            # Update flow along path
            x = self.par[t]
            while x:
                x.flow += fl
                self.ed[x.to][x.rev].flow -= fl
                x = self.par[x.from_node]

        # Calculate total cost
        for i in range(self.N):
            for e in self.ed[i]:
                totcost += e.cost * e.flow

        return (totflow, totcost // 2)

    def setpi(self, s):
        """
        If some costs can be negative, call this before maxflow.
        Uses Bellman-Ford to set initial potentials.
        """
        self.pi = [INF] * self.N
        self.pi[s] = 0
        it = self.N
        ch = 1

        while ch and it:
            it -= 1
            ch = 0
            for i in range(self.N):
                if self.pi[i] != INF:
                    for e in self.ed[i]:
                        if e.cap:
                            v = self.pi[i] + e.cost
                            if v < self.pi[e.to]:
                                self.pi[e.to] = v
                                ch = 1

        assert it >= 0, "Negative cost cycle detected"
