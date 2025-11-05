"""
 * Author: Simon Lindholm
 * Date: 2018-07-06
 * License: CC0
 * Description: Permutation -> integer conversion. (Not order preserving.)
 * Integer -> permutation can use a lookup table.
 * Time: O(n)

"""

def perm_to_int(v):
    """
    Convert a permutation to an integer representation.

    Args:
        v: List representing a permutation (0-indexed)

    Returns:
        Integer representation of the permutation

    Note: This is not order-preserving. To convert back, use a lookup table.
    """
    use = 0
    i = 0
    r = 0

    for x in v:
        i += 1
        # Count number of bits set in (use & -(1 << x))
        # This counts how many smaller elements have been used
        count = bin(use & -(1 << x)).count('1')
        r = r * i + count
        use |= 1 << x

    return r

def int_to_perm(n, val):
    """
    Convert an integer back to a permutation using lookup/generation.

    Args:
        n: Size of permutation
        val: Integer representation

    Returns:
        Permutation as a list

    Note: This is a general method. For specific use cases,
    pre-computing a lookup table may be more efficient.
    """
    perm = []
    available = list(range(n))

    for i in range(n, 0, -1):
        idx = val % i
        val //= i
        perm.append(available[idx])
        available.pop(idx)

    return perm
