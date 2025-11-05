"""
Author: Johan Sannemo
Date: 2015-02-06
License: CC0
Source: Folklore
Description: Calculate power of two jumps in a tree,
to support fast upward jumps and LCAs.
Assumes the root node points to itself.
Time: construction O(N log N), queries O(log N)
Status: Tested at Petrozavodsk, also stress-tested via LCA.cpp
"""

def tree_jump(P):
    """
    Build jump table for binary lifting.
    P[i] = parent of node i
    Returns jump table where jmp[k][i] = 2^k-th ancestor of i
    """
    n = len(P)
    on = 1
    d = 1
    while on < n:
        on *= 2
        d += 1

    jmp = [list(P) for _ in range(d)]
    for i in range(1, d):
        for j in range(n):
            jmp[i][j] = jmp[i-1][jmp[i-1][j]]

    return jmp

def jump(tbl, node, steps):
    """
    Jump 'steps' steps up from 'node' using jump table.
    """
    for i in range(len(tbl)):
        if steps & (1 << i):
            node = tbl[i][node]
    return node

def lca(tbl, depth, a, b):
    """
    Find lowest common ancestor of nodes a and b.
    tbl: jump table from tree_jump
    depth: depth[i] = depth of node i
    """
    if depth[a] < depth[b]:
        a, b = b, a

    # Bring a to same level as b
    a = jump(tbl, a, depth[a] - depth[b])

    if a == b:
        return a

    # Binary search for LCA
    for i in range(len(tbl) - 1, -1, -1):
        c = tbl[i][a]
        d = tbl[i][b]
        if c != d:
            a = c
            b = d

    return tbl[0][a]
