"""
 * Author: Emil Lenngren, Simon Lindholm
 * Date: 2011-11-29
 * License: CC0
 * Source: folklore
 * Description: Calculates a valid assignment to boolean variables a, b, c,... to a 2-SAT problem,
 * so that an expression of the type (a||b)&&(!a||c)&&(d||!b)&&...
 * becomes true, or reports that it is unsatisfiable.
 * Negated variables are represented by bit-inversions (~x).
 * Usage:
 *  ts = TwoSat(number of boolean variables)
 *  ts.either(0, ~3)  // Var 0 is true or var 3 is false
 *  ts.set_value(2)  // Var 2 is true
 *  ts.at_most_one([0,~1,2])  // <= 1 of vars 0, ~1 and 2 are true
 *  ts.solve()  // Returns True iff it is solvable
 *  ts.values[0..N-1] holds the assigned values to the vars
 * Time: O(N+E), where N is the number of boolean variables, and E is the number of clauses.
 * Status: stress-tested

"""

class TwoSat:
    def __init__(self, n=0):
        self.N = n
        self.gr = [[] for _ in range(2 * n)]
        self.values = []
        self.val = []
        self.comp = []
        self.z = []
        self.time = 0

    def add_var(self):
        """Optional: add a new boolean variable"""
        self.gr.append([])
        self.gr.append([])
        self.N += 1
        return self.N - 1

    def either(self, f, j):
        """Add clause: f OR j must be true"""
        f = max(2 * f, -1 - 2 * f)
        j = max(2 * j, -1 - 2 * j)
        self.gr[f].append(j ^ 1)
        self.gr[j].append(f ^ 1)

    def set_value(self, x):
        """Set variable x to true"""
        self.either(x, x)

    def at_most_one(self, li):
        """At most one of the variables in li can be true"""
        if len(li) <= 1:
            return
        cur = ~li[0]
        for i in range(2, len(li)):
            next_var = self.add_var()
            self.either(cur, ~li[i])
            self.either(cur, next_var)
            self.either(~li[i], next_var)
            cur = ~next_var
        self.either(cur, ~li[1])

    def dfs(self, i):
        low = self.val[i] = self.time
        self.time += 1
        x = i
        self.z.append(i)

        for e in self.gr[i]:
            if not self.comp[e]:
                if self.val[e] == 0:
                    low = min(low, self.dfs(e))
                else:
                    low = min(low, self.val[e])

        if low == self.val[i]:
            while True:
                x = self.z.pop()
                self.comp[x] = low
                if self.values[x >> 1] == -1:
                    self.values[x >> 1] = x & 1
                if x == i:
                    break

        self.val[i] = low
        return low

    def solve(self):
        """
        Solve the 2-SAT problem.
        Returns True if satisfiable, False otherwise.
        After solving, self.values contains the assignment.
        """
        self.values = [-1] * self.N
        self.val = [0] * (2 * self.N)
        self.comp = [0] * (2 * self.N)
        self.time = 0
        self.z = []

        for i in range(2 * self.N):
            if not self.comp[i]:
                self.dfs(i)

        for i in range(self.N):
            if self.comp[2 * i] == self.comp[2 * i + 1]:
                return False
        return True
