"""
 * Author: Simon Lindholm
 * Date: 2018-07-15
 * License: CC0
 * Source: Wikipedia
 * Description: Given N and a real number x >= 0, finds the closest rational approximation p/q with p, q <= N.
 * It will obey |p/q - x| <= 1/qN.

 * For consecutive convergents, p_{k+1}q_k - q_{k+1}p_k = (-1)^k.
 * (p_k/q_k alternates between >x and <x.)
 * If x is rational, y eventually becomes infinity;
 * if x is the root of a degree 2 polynomial the a's eventually become cyclic.
 * Time: O(log N)
 * Status: stress-tested for n <= 300

"""

def approximate(x, N):
    """
    Find the closest rational approximation p/q to x with p, q <= N
    Returns a tuple (p, q)
    """
    LP = 0
    LQ = 1
    P = 1
    Q = 0
    inf = float('inf')
    y = x

    while True:
        lim = min(
            (N - LP) // P if P else inf,
            (N - LQ) // Q if Q else inf
        )
        a = int(y)
        b = min(a, lim)
        NP = b * P + LP
        NQ = b * Q + LQ

        if a > b:
            # If b > a/2, we have a semi-convergent that gives us a
            # better approximation; if b = a/2, we *may* have one.
            # Return (P, Q) here for a more canonical approximation.
            if abs(x - NP / NQ) < abs(x - P / Q):
                return (NP, NQ)
            else:
                return (P, Q)

        if y != a:
            y = 1 / (y - a)
        else:
            return (NP, NQ)

        if abs(y) > 3 * N:
            return (NP, NQ)

        LP = P
        P = NP
        LQ = Q
        Q = NQ
