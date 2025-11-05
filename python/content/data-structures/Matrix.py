"""
Author: Ulf Lundstrom
Date: 2009-08-03
License: CC0
Source: My head
Description: Basic operations on square matrices.
Usage: A = Matrix(3)
 A.d = [[1,2,3], [4,5,6], [7,8,9]]
 vec = [1,2,3]
 vec = (A ** N) * vec
Status: tested
"""

class Matrix:
    def __init__(self, n):
        self.n = n
        self.d = [[0] * n for _ in range(n)]

    def __mul__(self, other):
        if isinstance(other, Matrix):
            # Matrix multiplication
            result = Matrix(self.n)
            for i in range(self.n):
                for j in range(self.n):
                    for k in range(self.n):
                        result.d[i][j] += self.d[i][k] * other.d[k][j]
            return result
        elif isinstance(other, (list, tuple)):
            # Matrix-vector multiplication
            result = [0] * self.n
            for i in range(self.n):
                for j in range(self.n):
                    result[i] += self.d[i][j] * other[j]
            return result
        else:
            raise TypeError("Unsupported operand type")

    def __pow__(self, p):
        assert p >= 0
        # Identity matrix
        result = Matrix(self.n)
        for i in range(self.n):
            result.d[i][i] = 1

        base = Matrix(self.n)
        base.d = [row[:] for row in self.d]  # Deep copy

        while p:
            if p & 1:
                result = result * base
            base = base * base
            p >>= 1
        return result
