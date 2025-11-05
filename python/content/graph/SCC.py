"""
 * Author: Lukas Polacek
 * Date: 2009-10-28
 * License: CC0
 * Source: Czech graph algorithms book, by Demel. (Tarjan's algorithm)
 * Description: Finds strongly connected components in a
 * directed graph. If vertices u, v belong to the same component,
 * we can reach u from v and vice versa.
 * Usage: scc(graph, lambda v: ...) visits all components
 * in reverse topological order. comp[i] holds the component
 * index of a node (a component only has edges to components with
 * lower index). ncomps will contain the number of components.
 * Time: O(E + V)
 * Status: Bruteforce-tested for N <= 5

"""

# Global variables (can be encapsulated in a class if preferred)
val = []
comp = []
z = []
cont = []
Time = 0
ncomps = 0

def dfs(j, g, f):
    global Time, ncomps, val, comp, z, cont
    low = val[j] = Time
    Time += 1
    z.append(j)

    for e in g[j]:
        if comp[e] < 0:
            if val[e] == 0:
                low = min(low, dfs(e, g, f))
            else:
                low = min(low, val[e])

    if low == val[j]:
        while True:
            x = z.pop()
            comp[x] = ncomps
            cont.append(x)
            if x == j:
                break
        f(cont)
        cont = []
        ncomps += 1

    val[j] = low
    return low

def scc(g, f):
    """
    g: adjacency list
    f: callback function to process each SCC
    """
    global Time, ncomps, val, comp, z, cont
    n = len(g)
    val = [0] * n
    comp = [-1] * n
    z = []
    cont = []
    Time = 0
    ncomps = 0

    for i in range(n):
        if comp[i] < 0:
            dfs(i, g, f)
