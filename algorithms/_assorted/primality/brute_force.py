

def numb(n: int):
    for i in range(2, n):
        if n % i == 0: return False
    return True

def linear(n: int):
    if n == 2 or n == 3: return True
    sz = n // 2
    for i in range(5, sz, 2):
        if n % i == 0: return False
    return True

def log(n: int):
    if n == 2: return True
    sz = n ** 0.5 # sqrt
    for i in range(3, int(sz) + 1, 1):
        if n % i == 0: return False
    return True

def eliminatory(n: int):
    if n == 2 or n == 3: return True # covers 2, 3
    if n % 2 == 0 or n < 2: return False # covers 1, 0, -1... and x * 2
    if n < 9: return True # covers 5, 7
    if n % 3 == 0: return False # covers x * 3

    r = n ** 0.5 // 1

    f = 11

    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True


if __name__ == "__main__":
    for t in [2, 3, 5, 221, 1235, 124, 612, 1451251, 1117111]:
        print(t, numb(t), linear(t), log(t), eliminatory(t))
