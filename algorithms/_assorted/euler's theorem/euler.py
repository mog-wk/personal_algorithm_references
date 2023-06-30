import math

def euler(a, n):
    '''n**euler_totient(p) = 1 mod n'''
    if not are_coprime(a, n):
        return -1
    return (a**euler_totient(n)) % n
    pass


def are_coprime(x, y) -> bool:
    return math.gcd(x, y) == 1


def euler_totient(n: int) -> int:
    ''' returns how many numbers are coprime with 'n';
    coprime implies gcd(n, i) == 1
    prime numbers return n-1; unefficient prime checker thought'''
    c = 0
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            c += 1
    return c


if __name__ == "__main__":
    tests = [2, 5, 6, 14, 16, 18, 35, 37, 65, 123, 712, 129742, 126281]

    for test in tests:
        print(test, euler_totient(test))

