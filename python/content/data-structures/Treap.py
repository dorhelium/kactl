"""
Author: someone on Codeforces
Date: 2017-03-14
Source: folklore
Description: A short self-balancing tree. It acts as a
sequential container with log-time splits/joins, and
is easy to augment with additional data.
Time: O(log N)
Status: stress-tested
"""

import random

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.val = val
        self.y = random.randint(0, 2**31 - 1)
        self.c = 1

    def recalc(self):
        self.c = cnt(self.l) + cnt(self.r) + 1

def cnt(n):
    return n.c if n else 0

def each(n, f):
    """Apply function f to each value in-order"""
    if n:
        each(n.l, f)
        f(n.val)
        each(n.r, f)

def split(n, k):
    """Split tree into two: first k elements and the rest"""
    if not n:
        return None, None
    if cnt(n.l) >= k:
        L, R = split(n.l, k)
        n.l = R
        n.recalc()
        return L, n
    else:
        L, R = split(n.r, k - cnt(n.l) - 1)
        n.r = L
        n.recalc()
        return n, R

def merge(l, r):
    """Merge two trees"""
    if not l:
        return r
    if not r:
        return l
    if l.y > r.y:
        l.r = merge(l.r, r)
        l.recalc()
        return l
    else:
        r.l = merge(l, r.l)
        r.recalc()
        return r

def ins(t, n, pos):
    """Insert node n at position pos"""
    l, r = split(t, pos)
    return merge(merge(l, n), r)

def move(t, l, r, k):
    """Move the range [l, r) to index k"""
    a, b = split(t, l)
    b, c = split(b, r - l)
    if k <= l:
        return merge(ins(a, b, k), c)
    else:
        return merge(a, ins(c, b, k - r))
