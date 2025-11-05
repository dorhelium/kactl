"""
 * Author: Victor Lecomte, chilli
 * Date: 2019-04-26
 * License: CC0
 * Source: https://vlecomte.github.io/cp-geo.pdf
 * Description: Returns true iff p lies on the line segment from s to e.
 * Use (seg_dist(s,e,p)<=epsilon) instead when using Point with float.
 * Status:

"""


def on_segment(s, e, p):
    """
    Returns True if p lies on the line segment from s to e.
    For float points, consider using seg_dist(s, e, p) <= epsilon instead.
    """
    return p.cross(s, e) == 0 and (s - p).dot(e - p) <= 0
