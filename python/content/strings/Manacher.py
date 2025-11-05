"""
Author: User adamant on CodeForces
Source: http://codeforces.com/blog/entry/12143
Description: For each position in a string, computes p[0][i] = half length of
 longest even palindrome around pos i, p[1][i] = longest odd (half rounded down).
Time: O(N)
Status: Stress-tested
"""


def manacher(s):
    n = len(s)
    p = [[0] * (n + 1), [0] * n]

    for z in range(2):
        l = 0
        r = 0
        for i in range(n):
            t = r - i + (1 if z == 0 else 0)
            if i < r:
                p[z][i] = min(t, p[z][l + t])

            L = i - p[z][i]
            R = i + p[z][i] - (1 if z == 0 else 0)

            while L >= 1 and R + 1 < n and s[L - 1] == s[R + 1]:
                p[z][i] += 1
                L -= 1
                R += 1

            if R > r:
                l = L
                r = R

    return p
