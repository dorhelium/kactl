"""
Author: Simon Lindholm
Date: 2021-01-09
License: CC0
Source: https://en.wikipedia.org/wiki/Stoer-Wagner_algorithm
Description: Find a global minimum cut in an undirected graph, as represented by an adjacency matrix.
Time: O(V^3)
Status: Stress-tested together with GomoryHu
"""

def global_min_cut(mat):
    """
    Find global minimum cut using Stoer-Wagner algorithm.
    mat: adjacency matrix where mat[i][j] = weight of edge between i and j
    Returns: (cut_weight, nodes_on_one_side)
    """
    n = len(mat)
    best = (float('inf'), [])
    co = [[i] for i in range(n)]

    for ph in range(1, n):
        w = mat[0][:]
        s = 0
        t = 0

        # Find most tightly connected pair
        for _ in range(n - ph):
            w[t] = float('-inf')
            s = t
            t = max(range(n), key=lambda i: w[i])
            for i in range(n):
                w[i] += mat[t][i]

        # Update best cut
        if w[t] - mat[t][t] < best[0]:
            best = (w[t] - mat[t][t], co[t][:])

        # Merge s and t
        co[s].extend(co[t])
        for i in range(n):
            mat[s][i] += mat[t][i]
            mat[i][s] = mat[s][i]

        mat[0][t] = float('-inf')

    return best
