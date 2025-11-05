"""
 * Author: Simon Lindholm
 * Date: 2015-05-13
 * Source: Wikipedia
 * Description: After running max-flow, the left side of a min-cut from s to t is given
 * by all vertices reachable from s, only traversing edges with positive residual capacity.
 * Status: works

"""

# This is a note/documentation file, not actual code.
# After running any max-flow algorithm (Dinic, EdmondsKarp, PushRelabel),
# use the left_of_min_cut method to determine which side of the cut each vertex is on.
