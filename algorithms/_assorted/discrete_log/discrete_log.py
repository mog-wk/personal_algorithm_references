import numpy as np
import sys

'''
euler's theorem
a^phi(n) = 1 (mod n)
where 
a is a positive integer > 0 | unsigned int
n is > 0 and < a
n and a are coprime | gcd(a, n) == 1
phi = euler's totient function | number of positive integers that are coprime with n

m = phi(n)
'''



# powers of integer mod n

def get_power_matrix(n: int):
    ''' returns a np.array with the values '''

    if n <= 1: raise ValueError
    return np.array([[(i**j) % n for j in range(1, n)] for i in range(1, n)], dtype=np.int32)


def get_primitive_roots(m: np.array):
    pr = []
    for i in m[1:]:
        if not 1 in i[:-1]:
            pr.append(i[0])
    return pr
    #return np.array(m[m[1:] 

def is_primitive_root(a: int, p: int):
    return a in get_primitive_roots(get_power_matrix(p))

def get_discrete_log(a, b, p) -> int:
    #if b >= p or a >= p: raise ValueError(f"invalid bounderies {a} {b}")
    #if not is_primitive_root(a, p): raise ValueError(f"{a} is not a primitive root of {p}")
    for i in range(1, p):
        if pow(a, i, p) == b % p:
            return i
    raise ValueError(f"{a} is not a primitive root of {p}")

if __name__ == "__main__":
    arg = int(sys.argv[1])
    m = get_power_matrix(arg)
    p = get_primitive_roots(m)

    for row in m:
        print(row)

    print("====================================================")
    for row in p:
        print(row)
    print(is_primitive_root(10, arg))
    print(get_discrete_log(10, 12, arg))
