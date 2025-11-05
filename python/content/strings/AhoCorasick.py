"""
 * Author: Simon Lindholm
 * Date: 2015-02-18
 * License: CC0
 * Source: marian's (TC) code
 * Description: Aho-Corasick automaton, used for multiple pattern matching.
 * Initialize with ac = AhoCorasick(patterns); the automaton start node will be at index 0.
 * find(word) returns for each position the index of the longest word that ends there, or -1 if none.
 * find_all(patterns, word) finds all words (up to N sqrt(N) many if no duplicate patterns)
 * that start at each position (shortest first).
 * Duplicate patterns are allowed; empty patterns are not.
 * To find the longest words that start at each position, reverse all input.
 * For large alphabets, split each symbol into chunks, with sentinel bits for symbol boundaries.
 * Time: construction takes O(26N), where N = sum of length of patterns.
 * find(x) is O(N), where N = length of x. find_all is O(NM).
 * Status: stress-tested

"""

from collections import deque


class AhoCorasick:
    ALPHA = 26
    FIRST = ord('A')  # change this!

    class Node:
        def __init__(self, v=-1):
            # (nmatches is optional)
            self.back = 0
            self.next = [v] * AhoCorasick.ALPHA
            self.start = -1
            self.end = -1
            self.nmatches = 0

    def __init__(self, patterns):
        self.N = [self.Node()]
        self.backp = []

        for j, pattern in enumerate(patterns):
            self._insert(pattern, j)

        self.N[0].back = len(self.N)
        self.N.append(self.Node(0))

        q = deque([0])
        while q:
            n = q.popleft()
            prev = self.N[n].back

            for i in range(self.ALPHA):
                ed = self.N[n].next[i]
                y = self.N[prev].next[i]

                if ed == -1:
                    self.N[n].next[i] = y
                else:
                    self.N[ed].back = y
                    if self.N[ed].end == -1:
                        self.N[ed].end = self.N[y].end
                    else:
                        self.backp[self.N[ed].start] = self.N[y].end
                    self.N[ed].nmatches += self.N[y].nmatches
                    q.append(ed)

    def _insert(self, s, j):
        assert len(s) > 0
        n = 0
        for c in s:
            ch_idx = ord(c) - self.FIRST
            if self.N[n].next[ch_idx] == -1:
                self.N[n].next[ch_idx] = len(self.N)
                self.N.append(self.Node(-1))
            n = self.N[n].next[ch_idx]

        if self.N[n].end == -1:
            self.N[n].start = j
        self.backp.append(self.N[n].end)
        self.N[n].end = j
        self.N[n].nmatches += 1

    def find(self, word):
        n = 0
        res = []
        # count = 0
        for c in word:
            n = self.N[n].next[ord(c) - self.FIRST]
            res.append(self.N[n].end)
            # count += self.N[n].nmatches
        return res

    def find_all(self, patterns, word):
        r = self.find(word)
        res = [[] for _ in range(len(word))]
        for i in range(len(word)):
            ind = r[i]
            while ind != -1:
                res[i - len(patterns[ind]) + 1].append(ind)
                ind = self.backp[ind]
        return res
