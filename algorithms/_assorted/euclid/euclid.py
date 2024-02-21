import math

def euclid(m: int, n: int) -> int:
    if n > m: (m, n) = (n, m)
    if n == 0: return m;
    while m % n != 0:
        (m, n) = (n, m % n)
    return abs(n)

def interactive_euclid(m: int, n: int) -> int:
    while (n > 0 and m > 0):
        if n > m:
            n = n % m
        else:
            m = m % n

    if n == 0:
        return m
    return n


if __name__ == "__main__":
    tests = [
        ((12, 2), 2),
        ((11, 2), 1),
        ((-11, 2), 1),
        ((270, 192), 6),
        ((16_156, 32), 4),
        ((523, 0), -1),
        ((6, 17), -1),
        ((42, 5), 1),
        ((25, 125), 25),
        ((12, 50), 2),
        ((0, 5), 5),
        ((0, 0), 0),
        ]

    for inp, res in tests:
        a, b = inp
        print("input: {} result: {} answer: {}" .format(inp, euclid(a, b), math.gcd(a, b)))

