"""
Author: Simon Lindholm
Date: 2019-12-28
License: CC0
Source: https://github.com/hoke-t/tamu-kactl/blob/master/content/data-structures/MoQueries.h
Description: Answer interval or tree path queries by finding an approximate TSP through the queries,
and moving from one query to the next by adding/removing points at the ends.
Time: O(N sqrt Q)
Status: stress-tested
"""

# User must define these functions before calling mo():
# def add(ind, end): pass  # add a[ind] (end = 0 or 1)
# def del_elem(ind, end): pass  # remove a[ind]
# def calc(): pass  # compute current answer

def mo(Q, add_func, del_func, calc_func):
    """
    Q: list of (first, second) tuples representing queries
    Returns: list of answers for each query
    """
    L = 0
    R = 0
    blk = 350  # ~N/sqrt(Q)
    s = list(range(len(Q)))
    res = [0] * len(Q)

    def key(x):
        q = Q[x]
        return (q[0] // blk, q[1] ^ (-(q[0] // blk & 1)))

    s.sort(key=key)

    for qi in s:
        q = Q[qi]
        while L > q[0]:
            L -= 1
            add_func(L, 0)
        while R < q[1]:
            add_func(R, 1)
            R += 1
        while L < q[0]:
            del_func(L, 0)
            L += 1
        while R > q[1]:
            R -= 1
            del_func(R, 1)
        res[qi] = calc_func()

    return res


def mo_tree(Q, ed, add_func, del_func, calc_func, root=0):
    """
    Q: list of [a, b] queries on tree
    ed: adjacency list of tree
    Returns: list of answers for each query
    """
    N = len(ed)
    pos = [0, 0]
    blk = 350  # ~N/sqrt(Q)
    s = list(range(len(Q)))
    res = [0] * len(Q)
    I = [0] * N
    L_arr = [0] * N
    R_arr = [0] * N
    in_arr = [0] * N
    par = [0] * N

    add_func(0, 0)
    in_arr[0] = 1

    # DFS to compute I, L, R, par arrays
    def dfs(x, p, dep):
        nonlocal N
        par[x] = p
        L_arr[x] = N
        if dep:
            I[x] = N
            N += 1
        for y in ed[x]:
            if y != p:
                dfs(y, x, 1 - dep)
        if not dep:
            I[x] = N
            N += 1
        R_arr[x] = N

    N_orig = N
    N = 0
    dfs(root, -1, 0)

    def key(x):
        return (I[Q[x][0]] // blk, I[Q[x][1]] ^ (-(I[Q[x][0]] // blk & 1)))

    s.sort(key=key)

    for qi in s:
        for end in range(2):
            a = pos[end]
            b = Q[qi][end]
            path = []
            while not (L_arr[b] <= L_arr[a] <= R_arr[b]):
                path.append(b)
                b = par[b]
            while a != b:
                if in_arr[a]:
                    del_func(a, end)
                    in_arr[a] = 0
                else:
                    add_func(a, end)
                    in_arr[a] = 1
                a = par[a]
            for i in reversed(path):
                if in_arr[i]:
                    del_func(i, end)
                    in_arr[i] = 0
                else:
                    add_func(i, end)
                    in_arr[i] = 1
                a = i
            pos[end] = a
            if end:
                res[qi] = calc_func()

    return res
