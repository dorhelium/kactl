"""
 * Author: Simon Lindholm
 * Date: 2017-05-11
 * License: CC0
 * Source: folklore
 * Description: Computes sums a[i,j] for all i<I, j<J, and increases single elements a[i,j].
 * Requires that the elements to be updated are known in advance (call fakeUpdate() before init()).
 * Time: O(log^2 N). (Use persistent segment trees for O(log N).)
 * Status: stress-tested

"""

from FenwickTree import FT
import bisect

class FT2:
    def __init__(self, limx):
        self.ys = [[] for _ in range(limx)]
        self.ft = []

    def fake_update(self, x, y):
        while x < len(self.ys):
            self.ys[x].append(y)
            x |= x + 1

    def init(self):
        for v in self.ys:
            v.sort()
            self.ft.append(FT(len(v)))

    def ind(self, x, y):
        return bisect.bisect_left(self.ys[x], y)

    def update(self, x, y, dif):
        while x < len(self.ys):
            self.ft[x].update(self.ind(x, y), dif)
            x |= x + 1

    def query(self, x, y):
        sum_val = 0
        while x:
            sum_val += self.ft[x - 1].query(self.ind(x - 1, y))
            x &= x - 1
        return sum_val
