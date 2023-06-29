import math

def is_prime(n: int) -> bool:
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    if n < 9: return True # covers 7 and 9 
    if n % 3  == 0: return False

    r = math.sqrt(n) // 1
    f = 11
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True


def fermat(a, p):
    ''' a^p-1 = 1 mod p
    conditions:
    'p' is prime
    'a' is positive integer(unsigned int)
    'a' is not divisible by 'p' not a|p

    should always equal 1 if condictions are met
    else returns -1'''

    if not is_prime(p):
        print(f"p ({p}) is not a prime number")
        return -1
    if a < 0:
        print(f"a is negative or zero")
        return -1
    if a % p == 0: 
        print(f"a ({a}) is divisible by p ({p})")
        return -1
    return (a ** (p-1)) % p 

if __name__ == "__main__":
    tests = [
            (12, 2),
            (16, 1231),
            (8, 11),
            (883, 21),
            (883, 23),
            ]
    for test in tests:
        a, b = test
        print(test, fermat(a, b))

