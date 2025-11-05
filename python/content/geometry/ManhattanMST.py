"""
Author: chilli, Takanori MAEHARA
Date: 2019-11-02
License: CC0
Source: https://github.com/spaghetti-source/algorithm/blob/master/geometry/rectilinear_mst.cc
Description: Given N points, returns up to 4*N edges, which are guaranteed
to contain a minimum spanning tree for the graph with edge weights w(p, q) =
|p.x - q.x| + |p.y - q.y|. Edges are in the form (distance, src, dst). Use a
standard MST algorithm on the result to find the final MST.
Time: O(N log N)
Status: Stress-tested
"""


def manhattan_mst(ps):
    """
    Generate candidate edges for Manhattan MST.
    ps: list of points (should have integer coordinates)
    Returns list of [distance, i, j] where i, j are point indices.
    """
    n = len(ps)
    id_list = list(range(n))
    edges = []

    for k in range(4):
        # Sort by x + y
        id_list.sort(key=lambda i: (ps[i].x - ps[i].y, ps[i].x + ps[i].y))

        sweep = {}  # maps -y to point index

        for i in id_list:
            # Find all points in sweep with -y >= -ps[i].y
            to_remove = []
            for neg_y in sorted(sweep.keys()):
                if neg_y < -ps[i].y:
                    break

                j = sweep[neg_y]
                d = ps[i] - ps[j]
                if d.y > d.x:
                    break

                edges.append([d.y + d.x, i, j])
                to_remove.append(neg_y)

            for neg_y in to_remove:
                del sweep[neg_y]

            sweep[-ps[i].y] = i

        # Transform coordinates for next iteration
        for p in ps:
            if k & 1:
                p.x = -p.x
            else:
                p.x, p.y = p.y, p.x

    return edges
