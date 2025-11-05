"""
Author: Håkan Terelius
Date: 2009-09-25
License: CC0
Source: http://en.wikipedia.org/wiki/Euler's_totient_function
Description: Euler's φ function is defined as φ(n):=# of positive integers ≤ n that are coprime with n.
φ(1)=1, p prime => φ(p^k)=(p-1)p^(k-1), m,n coprime => φ(mn)=φ(m)φ(n).
If n=p_1^{k_1}p_2^{k_2} ... p_r^{k_r} then φ(n) = (p_1-1)p_1^{k_1-1}...(p_r-1)p_r^{k_r-1}.
φ(n)=n · ∏_{p|n}(1-1/p).

∑_{d|n} φ(d) = n, ∑_{1≤k≤n, gcd(k,n)=1} k = n φ(n)/2, n>1

Euler's thm: a,n coprime => a^{φ(n)} ≡ 1 (mod n).

Fermat's little thm: p prime => a^{p-1} ≡ 1 (mod p) ∀a.
Status: Tested
"""

def calculate_phi(lim):
    """
    Calculate Euler's totient function for all numbers from 0 to lim-1
    Returns a list where phi[i] is the Euler's totient of i
    """
    phi = list(range(lim))

    # Initialize with i for odd numbers, i/2 for even numbers
    for i in range(0, lim):
        if i & 1:
            phi[i] = i
        else:
            phi[i] = i // 2

    # Apply Euler's formula
    for i in range(3, lim, 2):
        if phi[i] == i:  # i is prime
            for j in range(i, lim, i):
                phi[j] -= phi[j] // i

    return phi
