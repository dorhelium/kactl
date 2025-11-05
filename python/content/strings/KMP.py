"""
 * Author: Johan Sannemo
 * Date: 2016-12-15
 * License: CC0
 * Description: pi[x] computes the length of the longest prefix of s that ends at x,
 * other than s[0...x] itself (abacaba -> 0010123).
 * Can be used to find all occurrences of a string.
 * Time: O(n)
 * Status: Tested on kattis:stringmatching

"""


def pi(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        g = p[i - 1]
        while g and s[i] != s[g]:
            g = p[g - 1]
        p[i] = g + (1 if s[i] == s[g] else 0)
    return p


def match(s, pat):
    p = pi(pat + '\0' + s)
    res = []
    for i in range(len(p) - len(s), len(p)):
        if p[i] == len(pat):
            res.append(i - 2 * len(pat))
    return res
