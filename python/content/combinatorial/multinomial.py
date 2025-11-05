"""
 * Author: Mattias de Zalenski, Fredrik Niemelä, Per Austrin, Simon Lindholm
 * Date: 2002-09-26
 * Source: Max Bennedich
 * Description: Computes C(k_1 + ... + k_n; k_1, k_2, ..., k_n) = (sum k_i)! / (k_1! * k_2! * ... * k_n!)
 * This is the multinomial coefficient, which counts the number of ways to arrange
 * sum(k_i) objects where there are k_i objects of type i.
 * Status: Tested on kattis:lexicography

"""

def multinomial(v):
    """
    Compute the multinomial coefficient for the given partition.

    Args:
        v: List of non-negative integers [k_1, k_2, ..., k_n]

    Returns:
        The multinomial coefficient C(sum(v); k_1, k_2, ..., k_n)

    Examples:
        multinomial([2, 3]) = C(5; 2, 3) = 10
        multinomial([1, 2, 1]) = C(4; 1, 2, 1) = 12
    """
    if not v:
        return 1

    c = 1
    m = v[0]

    for i in range(1, len(v)):
        for j in range(v[i]):
            m += 1
            c = c * m // (j + 1)

    return c
