import numpy as np
import random

def miller_rabin(n, a=None, verbose=False):
    '''miller rabin returns true if probabbly prime returns false if certanly compose'''
    if n in set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 49]): return 1
    if n <= 1 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0: return -1

    # n - 1 = 2**k * q

    q = n - 1
    k = 0
    while q % 2 == 0:
        q /= 2
        k += 1

    assert(n - 1 == 2**k * q)

    if not a: a = random.randrange(2, n - 1)
    if verbose: print(a, n, q, k, end=' ')
    if pow(a, q, n) == 1: return 1
    for j in range(k):
        if pow(a, 2**j*q, n) == n - 1: return 1

    return -1


def is_prime(n, test_all=False, trys=12, verbose=False):
    odds = 0
    if test_all:
        test_table = [0, 0]
        for i in range(3, n-1):
            r = miller_rabin(n, a=i, verbose=True)
            test_table[r > 0] += 1
            odds += r
            print(f"{r} {odds}")

        print(test_table)
    else:
        for i in range(trys):
            odds +=  miller_rabin(n, verbose=verbose)
            print(odds)

    return odds > 0


def extended_euclid(a, b):
    ''' ax + by = mdc(a, b)'''






def rsa() -> tuple:
    # 1. define two large prime numbers
    p = 17
    q = 11

    # 2. multply then
    n = p * q

    # 3. calculate phi(euler's totient) of n, (p-1)(q-1)

    phi_n = (p-1) * (q-1)

    # 4. define e, a relative prime of phi_n and lower then phi_n

    e = 7

    # 5. define d, a multiplicative inverse of e mod (phi_n), (e * d) % phi_n = 1

    d = 23 # use the extended euclided algorithm

    return ((d, n), (e, n)) # returns private key and public key


if __name__ == "__main__":
    plain_text = "this is a sample text to be RSA incrypted pog"
    plain_bytes = plain_text.encode()
    print([int(i) for i in plain_bytes])
    print(is_prime(221, test_all=True))



