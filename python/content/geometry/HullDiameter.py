"""
 * Author: Oleksandr Bacherikov, chilli
 * Date: 2019-05-05
 * License: Boost Software License
 * Source: https://codeforces.com/blog/entry/48868
 * Description: Returns the two points with max distance on a convex hull (ccw,
 * no duplicate/collinear points).
 * Status: stress-tested, tested on kattis:roberthood
 * Time: O(n)

"""


def hull_diameter(S):
    """
    Find the diameter of a convex hull.
    Returns the two points with maximum distance.
    Hull must be in counter-clockwise order with no duplicates or collinear points.
    """
    n = len(S)
    j = 1 if n >= 2 else 0

    res_dist2 = 0
    res_pts = [S[0], S[0]]

    for i in range(j):
        while True:
            d2 = (S[i] - S[j]).dist2()
            if d2 > res_dist2:
                res_dist2 = d2
                res_pts = [S[i], S[j]]

            if (S[(j + 1) % n] - S[j]).cross(S[i + 1] - S[i]) >= 0:
                break

            j = (j + 1) % n

    return res_pts
