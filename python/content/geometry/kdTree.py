"""
Author: Stanford
Date: Unknown
Source: Stanford Notebook
Description: KD-tree (2d, can be extended to 3d)
Status: Tested on excellentengineers
"""

import sys


class Node:
    """Node in a KD-tree."""

    def __init__(self, vp):
        """
        Initialize a KD-tree node.
        vp: list of points
        """
        self.pt = vp[0]  # if leaf, the single point
        self.x0 = sys.maxsize
        self.x1 = -sys.maxsize
        self.y0 = sys.maxsize
        self.y1 = -sys.maxsize
        self.first = None
        self.second = None

        # Calculate bounds
        for p in vp:
            self.x0 = min(self.x0, p.x)
            self.x1 = max(self.x1, p.x)
            self.y0 = min(self.y0, p.y)
            self.y1 = max(self.y1, p.y)

        if len(vp) > 1:
            # Split on x if width >= height (not ideal...)
            if self.x1 - self.x0 >= self.y1 - self.y0:
                vp.sort(key=lambda p: p.x)
            else:
                vp.sort(key=lambda p: p.y)

            # Divide by taking half the array for each child
            half = len(vp) // 2
            self.first = Node(vp[:half])
            self.second = Node(vp[half:])

    def distance(self, p):
        """
        Minimum squared distance from point p to this bounding box.
        """
        x = p.x if p.x < self.x0 else (self.x1 if p.x > self.x1 else p.x)
        y = p.y if p.y < self.y0 else (self.y1 if p.y > self.y1 else p.y)

        from Point import Point
        return (Point(x, y) - p).dist2()


class KDTree:
    """KD-tree for nearest neighbor queries."""

    def __init__(self, vp):
        """Initialize KD-tree with list of points."""
        self.root = Node(vp[:])  # Make a copy

    def search(self, node, p):
        """
        Search for nearest point to p in subtree rooted at node.
        Returns (distance^2, point).
        """
        if not node.first:
            # Leaf node
            # Uncomment if we should not find the point itself:
            # if p == node.pt: return (sys.maxsize, None)
            return ((p - node.pt).dist2(), node.pt)

        f = node.first
        s = node.second
        bfirst = f.distance(p)
        bsec = s.distance(p)

        if bfirst > bsec:
            bfirst, bsec = bsec, bfirst
            f, s = s, f

        # Search closest side first, other side if needed
        best = self.search(f, p)
        if bsec < best[0]:
            best = min(best, self.search(s, p))

        return best

    def nearest(self, p):
        """
        Find nearest point to p and its squared distance.
        Returns (distance^2, point).
        """
        return self.search(self.root, p)
