"""
 * Author: Simon Lindholm
 * Date: 2017-04-17
 * License: CC0
 * Source: folklore
 * Description: Finds all biconnected components in an undirected graph, and
 * runs a callback for the edges in each. In a biconnected component there
 * are at least two distinct paths between any two nodes. Note that a node can
 * be in several components. An edge which is not in a component is a bridge,
 * i.e., not part of any cycle.
 * Usage:
 * eid = 0; ed = [[] for _ in range(N)]
 * for each edge (a,b):
 *     ed[a].append((b, eid))
 *     ed[b].append((a, eid))
 *     eid += 1
 * bicomps(lambda edgelist: ...)
 * Time: O(E + V)
 * Status: tested during MIPT ICPC Workshop 2017

"""

num = []
st = []
ed = []
Time = 0

def dfs(at, par, f):
    """DFS to find biconnected components"""
    global Time, num, st

    me = Time
    num[at] = Time
    Time += 1
    top = me

    for y, e in ed[at]:
        if e != par:
            if num[y] is not None:
                top = min(top, num[y])
                if num[y] < me:
                    st.append(e)
            else:
                si = len(st)
                up = dfs(y, e, f)
                top = min(top, up)
                if up == me:
                    st.append(e)
                    f(st[si:])
                    del st[si:]
                elif up < me:
                    st.append(e)
                # else: e is a bridge

    return top

def bicomps(f):
    """
    Find all biconnected components and call f for each component.
    f: callback function that takes a list of edge indices
    ed: global edge list where ed[i] = [(neighbor, edge_id), ...]
    """
    global Time, num, st

    n = len(ed)
    num = [None] * n
    st = []
    Time = 0

    for i in range(n):
        if num[i] is None:
            dfs(i, -1, f)
