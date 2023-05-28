
def euclid(a: int , b: int, verbose: bool = False) -> int:
    if b > a: a, b = b, a
    if b == 0: return -1

    n = abs(a)
    d = abs(b)

    while d != 0:
        mod = n % d
        n = d
        d = mod
        if verbose == True: print(n, d)

    return n


if __name__ == "__main__":
    tests = [
        ((12, 2), 2),
        ((11, 2), 1),
        ((-11, 2), 1),
        ((270, 192), 6),
        ((16_156, 32), 4),
        ((523, 0), -1),
        ((42, 5), 1),
        ((25, 125), 25),
        ((0, 5), -1),
        ]

    for inp, res in tests:
        a, b = inp
        euclid(a, b)
        print("{} => {}" .format(euclid(a, b, ), res))

