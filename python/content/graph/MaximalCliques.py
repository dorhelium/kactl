"""
 * Author: Simon Lindholm
 * Date: 2018-07-18
 * License: CC0
 * Source: https://en.wikipedia.org/wiki/Bron-Kerbosch_algorithm
 * Description: Runs a callback for all maximal cliques in a graph (given as a
 * symmetric bitset matrix; self-edges not allowed). Callback is given a bitset
 * representing the maximal clique.
 * Time: O(3^(n/3)), much faster for sparse graphs
 * Status: stress-tested

 * Possible optimization: on the top-most
 * recursion level, ignore 'cands', and go through nodes in order of increasing
 * degree, where degrees go down as nodes are removed.
 * (mostly irrelevant given MaximumClique)

"""

def cliques(eds, f, P=None, X=None, R=None):
    """
    Find all maximal cliques using Bron-Kerbosch algorithm.
    eds: adjacency list where eds[i] = set of neighbors of vertex i
    f: callback function to call with each maximal clique (as a set)
    P: candidate set (defaults to all vertices)
    X: excluded set (defaults to empty)
    R: current clique (defaults to empty)
    """
    n = len(eds)

    if P is None:
        P = set(range(n))
    if X is None:
        X = set()
    if R is None:
        R = set()

    if not P and not X:
        f(R)
        return

    # Choose pivot
    pivot_candidates = P | X
    if pivot_candidates:
        q = next(iter(pivot_candidates))
        cands = P - eds[q]
    else:
        cands = P.copy()

    for i in list(cands):
        R_new = R | {i}
        P_new = P & eds[i]
        X_new = X & eds[i]
        cliques(eds, f, P_new, X_new, R_new)
        P.remove(i)
        X.add(i)
