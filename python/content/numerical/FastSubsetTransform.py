"""
 * Author: Lucian Bicsi
 * Date: 2015-06-25
 * License: GNU Free Documentation License 1.2
 * Source: csacademy
 * Description: Transform to a basis with fast convolutions of the form
 * c[z] = sum_{z = x op y} a[x] * b[y],
 * where op is one of AND, OR, XOR. The size of a must be a power of two.
 * Time: O(N log N)
 * Status: stress-tested

"""

def fst(a, inv, op='AND'):
    """
    Fast Subset Transform
    op: 'AND', 'OR', or 'XOR'
    inv: True for inverse transform
    """
    n = len(a)
    step = 1
    while step < n:
        i = 0
        while i < n:
            for j in range(i, i + step):
                u_idx = j
                v_idx = j + step
                u = a[u_idx]
                v = a[v_idx]

                if op == 'AND':
                    if inv:
                        a[u_idx] = v - u
                        a[v_idx] = u
                    else:
                        a[u_idx] = v
                        a[v_idx] = u + v
                elif op == 'OR':
                    if inv:
                        a[u_idx] = v
                        a[v_idx] = u - v
                    else:
                        a[u_idx] = u + v
                        a[v_idx] = u
                elif op == 'XOR':
                    a[u_idx] = u + v
                    a[v_idx] = u - v
            i += 2 * step
        step *= 2

    # XOR requires division by n for inverse
    if op == 'XOR' and inv:
        for i in range(n):
            a[i] //= n

def conv(a, b, op='AND'):
    """Compute subset convolution using FST"""
    a_copy = a[:]
    b_copy = b[:]
    fst(a_copy, False, op)
    fst(b_copy, False, op)
    for i in range(len(a_copy)):
        a_copy[i] *= b_copy[i]
    fst(a_copy, True, op)
    return a_copy
