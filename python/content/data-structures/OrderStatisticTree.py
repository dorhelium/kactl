"""
 * Author: Simon Lindholm
 * Date: 2016-03-22
 * License: CC0
 * Source: hacKIT, NWERC 2015
 * Description: A set (not multiset!) with support for finding the n'th
 * element, and finding the index of an element.
 * Time: O(log N)

"""

from sortedcontainers import SortedSet

class OrderStatisticTree:
    """
    A set with order statistics support using sortedcontainers.
    Provides O(log N) operations for:
    - insert/remove
    - find k-th element
    - count elements less than x
    """
    def __init__(self):
        self.tree = SortedSet()

    def insert(self, x):
        """Insert element x"""
        self.tree.add(x)
        return self

    def remove(self, x):
        """Remove element x"""
        self.tree.discard(x)

    def find_by_order(self, k):
        """Find k-th element (0-indexed)"""
        if 0 <= k < len(self.tree):
            return self.tree[k]
        return None

    def order_of_key(self, x):
        """Count elements strictly less than x"""
        return self.tree.bisect_left(x)

    def lower_bound(self, x):
        """Find first element >= x"""
        idx = self.tree.bisect_left(x)
        if idx < len(self.tree):
            return self.tree[idx]
        return None

    def __contains__(self, x):
        return x in self.tree

    def __len__(self):
        return len(self.tree)

# Example usage
def example():
    t = OrderStatisticTree()
    t.insert(8)
    it = t.insert(10)
    assert t.lower_bound(9) == 10
    assert t.order_of_key(10) == 1
    assert t.order_of_key(11) == 2
    assert t.find_by_order(0) == 8
