"""
Author: Simon Lindholm
Date: 2015-02-24
License: CC0
Source: Wikipedia, tinyKACTL
Description: Push-relabel using the highest label selection rule and the gap heuristic. Quite fast in practice.
To obtain the actual flow, look at positive values only.
Time: O(V^2 sqrt(E))
Status: Tested on Kattis and SPOJ, and stress-tested
"""

class PushRelabel:
    class Edge:
        def __init__(self, dest, back, f, c):
            self.dest = dest
            self.back = back
            self.f = f
            self.c = c

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.ec = [0] * n
        self.cur = [None] * n
        self.hs = [[] for _ in range(2 * n)]
        self.H = [0] * n

    def add_edge(self, s, t, cap, rcap=0):
        """Add edge from s to t with capacity cap and reverse capacity rcap"""
        if s == t:
            return
        self.g[s].append(PushRelabel.Edge(t, len(self.g[t]), 0, cap))
        self.g[t].append(PushRelabel.Edge(s, len(self.g[s]) - 1, 0, rcap))

    def add_flow(self, e, f):
        """Add flow f to edge e"""
        back = self.g[e.dest][e.back]
        if not self.ec[e.dest] and f:
            self.hs[self.H[e.dest]].append(e.dest)
        e.f += f
        e.c -= f
        self.ec[e.dest] += f
        back.f -= f
        back.c += f
        self.ec[back.dest] -= f

    def calc(self, s, t):
        """Calculate max flow from s to t"""
        v = self.n
        self.H[s] = v
        self.ec[t] = 1
        co = [0] * (2 * v)
        co[0] = v - 1

        for i in range(v):
            self.cur[i] = 0

        # Initial push from source
        for e in self.g[s]:
            self.add_flow(e, e.c)

        hi = 0
        while True:
            # Find next active node
            while not self.hs[hi]:
                hi -= 1
                if hi < 0:
                    return -self.ec[s]

            u = self.hs[hi].pop()

            # Discharge u
            while self.ec[u] > 0:
                if self.cur[u] == len(self.g[u]):
                    # Relabel
                    self.H[u] = 10**9
                    for e in self.g[u]:
                        if e.c and self.H[u] > self.H[e.dest] + 1:
                            self.H[u] = self.H[e.dest] + 1
                            self.cur[u] = self.g[u].index(e)

                    co[self.H[u]] += 1
                    co[hi] -= 1
                    if co[hi] == 0 and hi < v:
                        # Gap heuristic
                        for i in range(v):
                            if hi < self.H[i] < v:
                                co[self.H[i]] -= 1
                                self.H[i] = v + 1
                    hi = self.H[u]
                else:
                    e = self.g[u][self.cur[u]]
                    if e.c and self.H[u] == self.H[e.dest] + 1:
                        self.add_flow(e, min(self.ec[u], e.c))
                    else:
                        self.cur[u] += 1

    def left_of_min_cut(self, a):
        """Check if node a is on the source side of min cut"""
        return self.H[a] >= self.n
