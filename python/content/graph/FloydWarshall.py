"""
 * Author: Simon Lindholm
 * Date: 2016-12-15
 * License: CC0
 * Source: http://en.wikipedia.org/wiki/Floyd-Warshall_algorithm
 * Description: Calculates all-pairs shortest path in a directed graph that might have negative edge weights.
 * Input is a distance matrix m, where m[i][j] = inf if i and j are not adjacent.
 * As output, m[i][j] is set to the shortest distance between i and j, inf if no path,
 * or -inf if the path goes through a negative-weight cycle.
 * Time: O(N^3)
 * Status: slightly tested

"""

INF = 1 << 62

def floyd_warshall(m):
    """
    m: 2D list (distance matrix)
    Modifies m in-place
    """
    n = len(m)
    for i in range(n):
        m[i][i] = min(m[i][i], 0)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if m[i][k] != INF and m[k][j] != INF:
                    new_dist = max(m[i][k] + m[k][j], -INF)
                    m[i][j] = min(m[i][j], new_dist)

    for k in range(n):
        if m[k][k] < 0:
            for i in range(n):
                for j in range(n):
                    if m[i][k] != INF and m[k][j] != INF:
                        m[i][j] = -INF
