"""
Author: Simon Lindholm
Date: 2016-07-25
Source: https://github.com/ngthanhtrung23/ACM_Notebook_new/blob/master/DataStructure/LinkCutTree.h
Description: Represents a forest of unrooted trees. You can add and remove
edges (as long as the result is still a forest), and check whether
two nodes are in the same tree.
Time: All operations take amortized O(log N).
Status: Stress-tested a bit for N <= 20
"""

class Node:
    """Splay tree node. Root's pp contains tree's parent."""
    def __init__(self):
        self.p = None  # parent in splay tree
        self.pp = None  # path parent
        self.c = [None, None]  # children
        self.flip = False
        self.fix()

    def fix(self):
        """Update node after modifications"""
        if self.c[0]:
            self.c[0].p = self
        if self.c[1]:
            self.c[1].p = self
        # Can add sum of subtree elements etc. if wanted

    def push_flip(self):
        """Push down flip lazy tag"""
        if not self.flip:
            return
        self.flip = False
        self.c[0], self.c[1] = self.c[1], self.c[0]
        if self.c[0]:
            self.c[0].flip ^= True
        if self.c[1]:
            self.c[1].flip ^= True

    def up(self):
        """Return which child this is (0 or 1), or -1 if root"""
        if not self.p:
            return -1
        return 1 if self.p.c[1] == self else 0

    def rot(self, i, b):
        """Rotate operation"""
        h = i ^ b
        x = self.c[i]
        y = x if b == 2 else x.c[h]
        z = y if b else x

        if self.p:
            self.p.c[self.up()] = y
        y.p = self.p

        self.c[i] = z.c[i ^ 1]

        if b < 2:
            x.c[h] = y.c[h ^ 1]
            y.c[h ^ 1] = x

        z.c[i ^ 1] = self

        self.fix()
        x.fix()
        y.fix()
        if self.p:
            self.p.fix()

        # Swap path parents
        self.pp, y.pp = y.pp, self.pp

    def splay(self):
        """Splay this up to the root. Always finishes without flip set."""
        self.push_flip()
        while self.p:
            if self.p.p:
                self.p.p.push_flip()
            self.p.push_flip()
            self.push_flip()

            c1 = self.up()
            c2 = self.p.up()

            if c2 == -1:
                self.p.rot(c1, 2)
            else:
                self.p.p.rot(c2, c1 != c2)

    def first(self):
        """Return the min element of the subtree rooted at this, splayed to the top."""
        self.push_flip()
        if self.c[0]:
            return self.c[0].first()
        self.splay()
        return self


class LinkCutTree:
    def __init__(self, N):
        self.node = [Node() for _ in range(N)]

    def link(self, u, v):
        """Add an edge (u, v)"""
        assert not self.connected(u, v)
        self.make_root(self.node[u])
        self.node[u].pp = self.node[v]

    def cut(self, u, v):
        """Remove an edge (u, v)"""
        x = self.node[u]
        top = self.node[v]
        self.make_root(top)
        x.splay()

        assert top == (x.pp if x.pp else x.c[0])

        if x.pp:
            x.pp = None
        else:
            x.c[0] = None
            top.p = None
            x.fix()

    def connected(self, u, v):
        """Check if u and v are in the same tree"""
        nu = self.access(self.node[u]).first()
        return nu == self.access(self.node[v]).first()

    def make_root(self, u):
        """Move u to root of represented tree"""
        self.access(u)
        u.splay()
        if u.c[0]:
            u.c[0].p = None
            u.c[0].flip ^= True
            u.c[0].pp = u
            u.c[0] = None
            u.fix()

    def access(self, u):
        """Move u to root aux tree. Return the root of the root aux tree."""
        u.splay()
        while u.pp:
            pp = u.pp
            pp.splay()
            u.pp = None
            if pp.c[1]:
                pp.c[1].p = None
                pp.c[1].pp = pp
            pp.c[1] = u
            pp.fix()
            u = pp
        return u
