"""
 * Author: Simon Lindholm
 * License: CC0
 * Description: Add and remove intervals from a set of disjoint intervals.
 * Will merge the added interval with any overlapping intervals in the set when adding.
 * Intervals are [inclusive, exclusive).
 * Time: O(log N)
 * Status: stress-tested

"""

from sortedcontainers import SortedList

class IntervalContainer:
    """
    Maintains a set of disjoint intervals with efficient add/remove operations.
    Uses a sorted list to maintain intervals in order.
    """
    def __init__(self):
        self.intervals = SortedList()

    def add_interval(self, L, R):
        """
        Add interval [L, R) to the set, merging with overlapping intervals.

        Args:
            L: Left endpoint (inclusive)
            R: Right endpoint (exclusive)

        Returns:
            Index of the added/merged interval
        """
        if L == R:
            return None

        intervals = self.intervals
        idx = intervals.bisect_left((L, R))

        # Merge with overlapping intervals
        while idx < len(intervals) and intervals[idx][0] <= R:
            R = max(R, intervals[idx][1])
            intervals.pop(idx)

        # Check if we can merge with previous interval
        if idx > 0 and intervals[idx - 1][1] >= L:
            idx -= 1
            L = min(L, intervals[idx][0])
            R = max(R, intervals[idx][1])
            intervals.pop(idx)

        intervals.add((L, R))
        return intervals.bisect_left((L, R))

    def remove_interval(self, L, R):
        """
        Remove interval [L, R) from the set.

        Args:
            L: Left endpoint (inclusive)
            R: Right endpoint (exclusive)
        """
        if L == R:
            return

        intervals = self.intervals
        idx = self.add_interval(L, R)

        if idx is None or idx >= len(intervals):
            return

        interval = intervals[idx]
        r2 = interval[1]

        if interval[0] == L:
            intervals.pop(idx)
        else:
            # Split: keep [interval[0], L)
            intervals.pop(idx)
            intervals.add((interval[0], L))

        if R != r2:
            # Add remaining part [R, r2)
            intervals.add((R, r2))

# Alternative implementation using standard list (simpler but may be less efficient)
def add_interval(intervals, L, R):
    """
    Add interval [L, R) to a sorted list of intervals.

    Args:
        intervals: Sorted list of (left, right) tuples
        L, R: Interval endpoints

    Returns:
        Updated intervals list and index of added interval
    """
    if L == R:
        return intervals, None

    new_intervals = []
    merged = False
    merge_L, merge_R = L, R

    for left, right in intervals:
        if right < L or left > R:
            # No overlap
            new_intervals.append((left, right))
        else:
            # Overlap - merge
            merge_L = min(merge_L, left)
            merge_R = max(merge_R, right)
            merged = True

    new_intervals.append((merge_L, merge_R))
    new_intervals.sort()

    return new_intervals, new_intervals.index((merge_L, merge_R))

def remove_interval(intervals, L, R):
    """Remove interval [L, R) from list of intervals"""
    if L == R:
        return intervals

    new_intervals = []
    for left, right in intervals:
        if right <= L or left >= R:
            # No overlap
            new_intervals.append((left, right))
        else:
            # Overlap - split
            if left < L:
                new_intervals.append((left, L))
            if R < right:
                new_intervals.append((R, right))

    return new_intervals
