"""
Author: Simon Lindholm
Date: 2016-01-14
License: CC0
Description: Given a rooted tree and a subset S of nodes, compute the minimal
subtree that contains all the nodes by adding all (at most |S|-1)
pairwise LCA's and compressing edges.
Returns a list of (par, orig_index) representing a tree rooted at 0.
The root points to itself.
Time: O(|S| log |S|)
Status: Tested at CodeForces
"""

# Note: This requires LCA.py

def compress_tree(lca, subset):
    """
    Compress tree to minimal subtree containing subset.
    lca: LCA object with lca.time array
    subset: list of node indices to include
    Returns: list of (parent_idx, original_node) pairs
    """
    rev = [0] * len(lca.time)
    li = subset[:]
    T = lca.time

    # Sort by DFS time
    li.sort(key=lambda a: T[a])

    m = len(li) - 1

    # Add LCAs of consecutive pairs
    for i in range(m):
        a = li[i]
        b = li[i + 1]
        li.append(lca.lca(a, b))

    # Sort again and remove duplicates
    li.sort(key=lambda a: T[a])
    li = list(dict.fromkeys(li))  # Remove duplicates while preserving order

    # Build reverse mapping
    for i, node in enumerate(li):
        rev[node] = i

    # Build compressed tree
    ret = [(0, li[0])]
    for i in range(len(li) - 1):
        a = li[i]
        b = li[i + 1]
        ret.append((rev[lca.lca(a, b)], b))

    return ret
