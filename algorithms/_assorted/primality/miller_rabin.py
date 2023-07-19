import random
import os
import time


def is_prime(n: int, a=None, trys=1) -> bool:
    ''' 
    miller-rabin
    returns false if n is composite number(definetly not a prime),
    returns true if n is inconclusive(almost certenly is a prime{get ratio})''' # TODO <<---

    # n must be an even unsigned integer >= 3
    if n in set([2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 41, 43, 47, 51, 53, 57, 61, 67, 71]): return True
    if n == 1 or n % 2 == 0: return False

    # satisfy n - 1 = 2^k * q
    # k is "exalstive", the maximum possible amount of times n - 1 can be divided by two

    q = n - 1
    k = 0
    while q % 2 == 0:
        q>>=1
        k += 1

    assert(2**k * q == n - 1)

    for i in range(trys):
        if not a: a = random.randrange(2, n-1) # a: 1 < a < n-1
        if pow(a, q, n) == 1: return True
        for j in range(k):
            if pow(a, 2**j*q, n) == n - 1: return True
    
    return False


def test():
    #for i in range(3, 101, 2):
        #print( miller_rabin(i))
    #tests = [2, 3, 5, 7, 9, 11, 13, 17, 21, 22, 23, 29, 31, 35, 79, 221, 1223, 12325, 100329, 1002429,] 
    #tests = [1117111]
    tests = [221]
    for test in tests:
        st = time.perf_counter_ns()
        stats = [0, 0]
        for i in range(3, test-1, 1):
            res = is_prime(test, a=i, trys=1)
            stats[int(res)] += 1
        end = time.perf_counter_ns()
        print(f"input: {test} | compost: {stats[0]} | inconclusive: {stats[1]} time: {end - st}ns")


if __name__ == "__main__":
    test()
