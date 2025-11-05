"""
Author: chilli, SJTU, Janez Konc
Date: 2019-05-10
License: GPL3+
Source: https://en.wikipedia.org/wiki/MaxCliqueDyn_maximum_clique_algorithm, https://gitlab.com/janezkonc/mcqd/blob/master/mcqd.h
Description: Quickly finds a maximum clique of a graph (given as symmetric bitset
matrix; self-edges not allowed). Can be used to find a maximum independent
set by finding a clique of the complement graph.
Time: Runs in about 1s for n=155 and worst case random graphs (p=.90). Runs
faster for sparse graphs.
Status: stress-tested
"""

class Maxclique:
    def __init__(self, conn):
        """
        conn: adjacency list where conn[i] = set of neighbors of vertex i
        """
        self.limit = 0.025
        self.pk = 0
        self.e = conn
        n = len(conn)
        self.V = [(i, 0) for i in range(n)]
        self.C = [[] for _ in range(n + 1)]
        self.S = [0] * n
        self.old = [0] * n
        self.qmax = []
        self.q = []

    def init(self, r):
        """Initialize vertex degrees"""
        # Calculate degrees
        for v_idx in range(len(r)):
            r[v_idx] = (r[v_idx][0], 0)

        for i in range(len(r)):
            for j in range(len(r)):
                if r[j][0] in self.e[r[i][0]]:
                    r[i] = (r[i][0], r[i][1] + 1)

        # Sort by degree
        r.sort(key=lambda v: v[1], reverse=True)

        # Update degrees
        mxD = r[0][1]
        for i in range(len(r)):
            r[i] = (r[i][0], min(i, mxD) + 1)

    def expand(self, R, lev=1):
        """Expand clique"""
        self.S[lev] += self.S[lev - 1] - self.old[lev]
        self.old[lev] = self.S[lev - 1]

        while R:
            if len(self.q) + R[-1][1] <= len(self.qmax):
                return

            self.q.append(R[-1][0])
            T = []

            for v in R:
                if v[0] in self.e[R[-1][0]]:
                    T.append((v[0], 0))

            if T:
                self.S[lev] += 1
                self.pk += 1
                if self.S[lev] / self.pk < self.limit:
                    self.init(T)

                j = 0
                mxk = 1
                mnk = max(len(self.qmax) - len(self.q) + 1, 1)

                self.C[1] = []
                self.C[2] = []

                for v in T:
                    k = 1
                    while any(i in self.e[v[0]] for i in self.C[k]):
                        k += 1

                    if k > mxk:
                        mxk = k
                        self.C[mxk + 1] = []

                    if k < mnk:
                        T[j] = (v[0], 0)
                        j += 1

                    self.C[k].append(v[0])

                if j > 0:
                    T[j - 1] = (T[j - 1][0], 0)

                j_idx = j
                for k in range(mnk, mxk + 1):
                    for i in self.C[k]:
                        T[j_idx] = (i, k)
                        j_idx += 1

                T = T[:j_idx]
                self.expand(T, lev + 1)
            elif len(self.q) > len(self.qmax):
                self.qmax = self.q[:]

            self.q.pop()
            R.pop()

    def max_clique(self):
        """Find maximum clique"""
        self.init(self.V)
        self.expand(self.V)
        return self.qmax
