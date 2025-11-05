"""
Author: Unknown
Date: 2017-05-15
Source: https://e-maxx.ru/algo/ukkonen
Description: Ukkonen's algorithm for online suffix tree construction.
 Each node contains indices [l, r) into the string, and a list of child nodes.
 Suffixes are given by traversals of this tree, joining [l, r) substrings.
 The root is 0 (has l = -1, r = 0), non-existent children are -1.
 To get a complete tree, append a dummy symbol -- otherwise it may contain
 an incomplete path (still useful for substring matching, though).
Time: O(26N)
Status: stress-tested a bit
"""


class SuffixTree:
    N = 200010
    ALPHA = 26  # N ~ 2*maxlen+10

    def __init__(self, a):
        self.a = a
        self.t = [[-1] * self.ALPHA for _ in range(self.N)]
        self.l = [0] * self.N
        self.r = [len(a)] * self.N
        self.p = [0] * self.N
        self.s = [0] * self.N
        self.v = 0
        self.q = 0
        self.m = 2

        # Initialize
        self.t[1] = [0] * self.ALPHA
        self.s[0] = 1
        self.l[0] = self.l[1] = -1
        self.r[0] = self.r[1] = 0
        self.p[0] = self.p[1] = 0

        for i in range(len(a)):
            self._ukkadd(i, self._toi(a[i]))

    def _toi(self, c):
        return ord(c) - ord('a')

    def _ukkadd(self, i, c):
        while True:
            if self.r[self.v] <= self.q:
                if self.t[self.v][c] == -1:
                    self.t[self.v][c] = self.m
                    self.l[self.m] = i
                    self.p[self.m] = self.v
                    self.m += 1
                    self.v = self.s[self.v]
                    self.q = self.r[self.v]
                    continue
                self.v = self.t[self.v][c]
                self.q = self.l[self.v]

            if self.q == -1 or c == self._toi(self.a[self.q]):
                self.q += 1
                break
            else:
                self.l[self.m + 1] = i
                self.p[self.m + 1] = self.m
                self.l[self.m] = self.l[self.v]
                self.r[self.m] = self.q
                self.p[self.m] = self.p[self.v]
                self.t[self.m][c] = self.m + 1
                self.t[self.m][self._toi(self.a[self.q])] = self.v
                self.l[self.v] = self.q
                self.p[self.v] = self.m
                self.t[self.p[self.m]][self._toi(self.a[self.l[self.m]])] = self.m
                self.v = self.s[self.p[self.m]]
                self.q = self.l[self.m]

                while self.q < self.r[self.m]:
                    self.v = self.t[self.v][self._toi(self.a[self.q])]
                    self.q += self.r[self.v] - self.l[self.v]

                if self.q == self.r[self.m]:
                    self.s[self.m] = self.v
                else:
                    self.s[self.m] = self.m + 2

                self.q = self.r[self.v] - (self.q - self.r[self.m])
                self.m += 2
                continue

    # example: find longest common substring (uses ALPHA = 28)
    def lcs(self, node, i1, i2, olen):
        if self.l[node] <= i1 < self.r[node]:
            return 1
        if self.l[node] <= i2 < self.r[node]:
            return 2

        mask = 0
        length = olen + (self.r[node] - self.l[node]) if node else 0

        for c in range(self.ALPHA):
            if self.t[node][c] != -1:
                mask |= self.lcs(self.t[node][c], i1, i2, length)

        if mask == 3:
            if (length, self.r[node] - length) > self.best:
                self.best = (length, self.r[node] - length)

        return mask

    @staticmethod
    def LCS(s, t):
        """Find longest common substring"""
        combined = s + chr(ord('z') + 1) + t + chr(ord('z') + 2)
        st = SuffixTree(combined)
        st.best = (0, 0)
        st.lcs(0, len(s), len(s) + 1 + len(t), 0)
        return st.best
