"""
 * Author: Simon Lindholm
 * Date: 2017-04-20
 * License: CC0
 * Source: own work
 * Description: Container where you can add lines of the form kx+m, and query maximum values at points x.
 * Useful for dynamic programming ("convex hull trick").
 * Time: O(log N)
 * Status: stress-tested

"""

from sortedcontainers import SortedList

class Line:
    def __init__(self, k, m, p=0):
        self.k = k
        self.m = m
        self.p = p

    def __lt__(self, other):
        if isinstance(other, Line):
            return self.k < other.k
        return self.p < other

class LineContainer:
    def __init__(self):
        self.lines = SortedList(key=lambda line: line.k)
        self.INF = float('inf')

    def div(self, a, b):
        """Floored division"""
        return a // b - (1 if (a ^ b) < 0 and a % b else 0)

    def isect(self, x_idx, y_idx):
        """Calculate intersection point of two lines"""
        if y_idx >= len(self.lines):
            self.lines[x_idx].p = self.INF
            return False

        x = self.lines[x_idx]
        y = self.lines[y_idx]

        if x.k == y.k:
            x.p = self.INF if x.m > y.m else -self.INF
        else:
            x.p = self.div(y.m - x.m, x.k - y.k)

        return x.p >= y.p

    def add(self, k, m):
        """Add line y = kx + m"""
        line = Line(k, m, 0)
        idx = self.lines.bisect_left(line)
        self.lines.add(line)

        # idx now points to our newly inserted line
        # Remove lines that are now irrelevant
        y_idx = idx + 1
        while y_idx < len(self.lines) and self.isect(idx, y_idx):
            self.lines.pop(y_idx)

        if idx > 0:
            x_idx = idx - 1
            if self.isect(x_idx, idx):
                self.lines.pop(idx)
                idx = x_idx

        while idx > 0:
            x_idx = idx - 1
            if self.lines[x_idx].p >= self.lines[idx].p:
                self.lines.pop(idx)
                idx = x_idx
                if idx < len(self.lines) - 1:
                    self.isect(idx, idx + 1)
            else:
                break

        # Recalculate intersections
        if idx > 0:
            self.isect(idx - 1, idx)

    def query(self, x):
        """Query maximum value at point x"""
        assert len(self.lines) > 0
        # Binary search for the right line
        idx = 0
        for i, line in enumerate(self.lines):
            if line.p >= x:
                idx = i
                break
        else:
            idx = len(self.lines) - 1

        l = self.lines[idx]
        return l.k * x + l.m
