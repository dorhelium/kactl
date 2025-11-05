"""
 * Author: chilli, Takanori MAEHARA
 * Date: 2020-04-03
 * License: CC0
 * Source: https://github.com/spaghetti-source/algorithm/blob/master/graph/gomory_hu_tree.cc//L102
 * Description: Given a list of edges representing an undirected flow graph,
 * returns edges of the Gomory-Hu tree. The max flow between any pair of
 * vertices is given by minimum edge weight along the Gomory-Hu tree path.
 * Time: O(V) Flow Computations
 * Status: Tested on CERC 2015 J, stress-tested

 * Details: The implementation used here is not actually the original
 * Gomory-Hu, but Gusfield's simplified version: "Very simple methods for all
 * pairs network flow analysis". PushRelabel is used here, but any flow
 * implementation that supports left_of_min_cut also works.

"""

# Note: This requires PushRelabel.py (or Dinic.py)
from PushRelabel import PushRelabel

def gomory_hu(N, edges):
    """
    Build Gomory-Hu tree.
    N: number of vertices
    edges: list of [a, b, capacity] edges
    Returns: list of tree edges [i, parent[i], flow_value]
    """
    tree = []
    par = [0] * N

    for i in range(1, N):
        D = PushRelabel(N)
        for edge in edges:
            D.add_edge(edge[0], edge[1], edge[2], edge[2])

        flow = D.calc(i, par[i])
        tree.append([i, par[i], flow])

        for j in range(i + 1, N):
            if par[j] == par[i] and D.left_of_min_cut(j):
                par[j] = i

    return tree
