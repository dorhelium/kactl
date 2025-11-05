"""
Author: Simon Lindholm
Date: 2015-02-23
License: CC0
Source: http://en.wikipedia.org/wiki/Bellman-Ford_algorithm
Description: Calculates shortest paths from s in a graph that might have negative edge weights.
Unreachable nodes get dist = inf; nodes reachable through negative-weight cycles get dist = -inf.
Time: O(VE)
Status: Tested on kattis:shortestpath3
"""

INF = float('inf')

class Ed:
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

    def s(self):
        return self.a if self.a < self.b else -self.a

class Node:
    def __init__(self):
        self.dist = INF
        self.prev = -1

def bellman_ford(nodes, eds, s):
    """
    nodes: list of Node objects
    eds: list of Ed objects (edges)
    s: source node index
    """
    nodes[s].dist = 0
    eds.sort(key=lambda ed: ed.s())

    lim = len(nodes) // 2 + 2

    for i in range(lim):
        for ed in eds:
            cur = nodes[ed.a]
            dest = nodes[ed.b]
            if abs(cur.dist) == INF:
                continue
            d = cur.dist + ed.w
            if d < dest.dist:
                dest.prev = ed.a
                dest.dist = d if i < lim - 1 else -INF

    for i in range(lim):
        for e in eds:
            if nodes[e.a].dist == -INF:
                nodes[e.b].dist = -INF
