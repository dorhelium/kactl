"""
 * Author: Johan Sannemo, Simon Lindholm
 * Date: 2016-12-15
 * License: CC0
 * Description: Finds a minimum vertex cover in a bipartite graph.
 * The size is the same as the size of a maximum matching, and
 * the complement is a maximum independent set.
 * Status: stress-tested

"""

# Note: This requires DFSMatching.py
from DFSMatching import dfs_matching

def cover(g, n, m):
    """
    Find minimum vertex cover in bipartite graph.
    g: adjacency list for left partition
    n: size of left partition
    m: size of right partition
    Returns: list of vertices in the cover (left vertices as 0..n-1, right as n..n+m-1)
    """
    match = [-1] * m
    res = dfs_matching(g, match)

    lfound = [True] * n
    seen = [False] * m

    # Mark matched vertices on left
    for it in match:
        if it != -1:
            lfound[it] = False

    # BFS from unmatched left vertices
    q = []
    for i in range(n):
        if lfound[i]:
            q.append(i)

    while q:
        i = q.pop()
        lfound[i] = True
        for e in g[i]:
            if not seen[e] and match[e] != -1:
                seen[e] = True
                q.append(match[e])

    # Build cover
    cover_set = []
    for i in range(n):
        if not lfound[i]:
            cover_set.append(i)
    for i in range(m):
        if seen[i]:
            cover_set.append(n + i)

    assert len(cover_set) == res
    return cover_set
