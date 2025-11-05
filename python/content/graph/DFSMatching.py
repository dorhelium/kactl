"""
 * Author: Lukas Polacek
 * Date: 2009-10-28
 * License: CC0
 * Source:
 * Description: Simple bipartite matching algorithm. Graph g should be a list
 * of neighbors of the left partition, and btoa should be a list full of
 * -1's of the same size as the right partition. Returns the size of
 * the matching. btoa[i] will be the match for vertex i on the right side,
 * or -1 if it's not matched.
 * Time: O(VE)
 * Usage: btoa = [-1] * m; dfs_matching(g, btoa)
 * Status: works

"""

def find(j, g, btoa, vis):
    """Try to find augmenting path starting from right vertex j"""
    if btoa[j] == -1:
        return True

    vis[j] = 1
    di = btoa[j]

    for e in g[di]:
        if not vis[e] and find(e, g, btoa, vis):
            btoa[e] = di
            return True

    return False

def dfs_matching(g, btoa):
    """
    Compute maximum bipartite matching.
    g: adjacency list for left partition
    btoa: list of -1's of size |right partition|
    Returns: size of matching
    """
    for i in range(len(g)):
        vis = [0] * len(btoa)
        for j in g[i]:
            if find(j, g, btoa, vis):
                btoa[j] = i
                break

    return len(btoa) - btoa.count(-1)
