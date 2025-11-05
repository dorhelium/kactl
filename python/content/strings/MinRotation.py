"""
 * Author: Stjepan Glavina
 * License: Unlicense
 * Source: https://github.com/stjepang/snippets/blob/master/min_rotation.cpp
 * Description: Finds the lexicographically smallest rotation of a string.
 * Time: O(N)
 * Usage:
 *  s = s[min_rotation(s):] + s[:min_rotation(s)]
 * Status: Stress-tested

"""


def min_rotation(s):
    a = 0
    N = len(s)
    s = s + s

    for b in range(N):
        for k in range(N):
            if a + k == b or s[a + k] < s[b + k]:
                b += max(0, k - 1)
                break
            if s[a + k] > s[b + k]:
                a = b
                break

    return a
