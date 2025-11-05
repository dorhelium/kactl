"""
 * Author: Johan Sannemo, pajenegod
 * Date: 2015-02-06
 * License: CC0
 * Source: Folklore
 * Description: Range Minimum Queries on an array. Returns
 * min(V[a], V[a + 1], ... V[b - 1]) in constant time.
 * Usage:
 *  rmq = RMQ(values)
 *  rmq.query(inclusive, exclusive)
 * Time: O(|V| log |V| + Q)
 * Status: stress-tested

"""

class RMQ:
    def __init__(self, V):
        self.jmp = [V[:]]
        pw = 1
        k = 1
        while pw * 2 <= len(V):
            self.jmp.append([0] * (len(V) - pw * 2 + 1))
            for j in range(len(self.jmp[k])):
                self.jmp[k][j] = min(self.jmp[k - 1][j], self.jmp[k - 1][j + pw])
            pw *= 2
            k += 1

    def query(self, a, b):
        assert a < b
        dep = (b - a).bit_length() - 1
        return min(self.jmp[dep][a], self.jmp[dep][b - (1 << dep)])
