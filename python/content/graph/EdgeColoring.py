"""
 * Author: Simon Lindholm
 * Date: 2020-10-12
 * License: CC0
 * Source: https://en.wikipedia.org/wiki/Misra_%26_Gries_edge_coloring_algorithm
 * https://codeforces.com/blog/entry/75431 for the note about bipartite graphs.
 * Description: Given a simple, undirected graph with max degree D, computes a
 * (D + 1)-coloring of the edges such that no neighboring edges share a color.
 * (D-coloring is NP-hard, but can be done for bipartite graphs by repeated matchings of
 * max-degree nodes.)
 * Time: O(NM)
 * Status: stress-tested, tested on kattis:gamescheduling

"""

def edge_coloring(N, edges):
    """
    Compute (D+1)-edge coloring using Misra & Gries algorithm.
    N: number of vertices
    edges: list of (u, v) edges
    Returns: list of colors (one per edge)
    """
    cc = [0] * (N + 1)
    ret = [0] * len(edges)
    fan = [0] * N
    free = [0] * N
    loc = []

    # Count degree
    for u, v in edges:
        cc[u] += 1
        cc[v] += 1

    ncols = max(cc) + 1
    adj = [[{} for _ in range(ncols)] for _ in range(N)]
    # adj[v] will map color -> neighbor

    # Build adjacency structure (simplified version)
    adj_list = [[None] * ncols for _ in range(N)]

    for idx, (u, v) in enumerate(edges):
        fan[0] = v
        loc = [0] * ncols
        at = u
        end = u
        c = free[u]
        ind = 0

        # Find fan
        d = free[v]
        while not loc[d] and adj_list[u][d] is not None:
            v_next = adj_list[u][d]
            if v_next == -1:
                break
            loc[d] = ind + 1
            ind += 1
            cc[ind] = d
            fan[ind] = v_next
            v = v_next
            d = free[v]

        cc[loc[d]] = c

        # Rotate along cd-path
        cd = d
        while at != -1:
            cd_next = cd ^ c ^ d
            next_at = adj_list[at][cd]
            adj_list[at][cd], adj_list[end][cd_next] = adj_list[end][cd_next], adj_list[at][cd]
            end = at
            at = next_at
            cd = cd_next

        # Update fan edges
        i = 0
        while i < ind and adj_list[fan[i]][d] is not None:
            left = fan[i]
            right = fan[i + 1]
            e = cc[i + 1]
            adj_list[u][e] = left
            adj_list[left][e] = u
            adj_list[right][e] = None
            free[right] = e
            i += 1

        adj_list[u][d] = fan[i]
        adj_list[fan[i]][d] = u

        # Update free colors
        for y in [fan[0], u, end]:
            z = 0
            while adj_list[y][z] is not None:
                z += 1
            free[y] = z

    # Reconstruct colors from adjacency
    for i, (u, v) in enumerate(edges):
        color = 0
        while adj_list[u][color] != v:
            color += 1
        ret[i] = color

    return ret
