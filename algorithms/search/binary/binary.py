import numpy as np
import math, time


def binary_search(arr: list, value: int) -> int:
    '''returns index of element in array
    arr => sorted list
    value => value to be found
    returns -1 if value is not in list
    not an accurate search
    '''
    if value not in arr: return -1

    pivot = (len(arr)-1) // 2

    while pivot > -1 and pivot < len(arr):
        print(pivot, arr[pivot], value)
        elt = arr[pivot]
        if elt == value:
            return pivot
        elif elt < value:
            pivot += pivot // 2
        elif elt > value:
            pivot -= pivot // 2
        #time.sleep(0.5)


if __name__ == "__main__":
    n = np.random.RandomState(42)
    tests = n.randint(0, 12, (10, 5))

    st = time.perf_counter()

    for test in tests:
        # position of 2nd element
        #print(binary_search(np.sort(test), test[1]))
        # has 7
        print(f"input: {test} res:{binary_search(np.sort(test), 7)}")

    mid = time.perf_counter()
    print(mid - st)

    big_arr = np.sort(n.randint(0, 100, 1000))
    print(f"input: {big_arr}")
    res = binary_search(big_arr, 22)
    print(f"res: {res} {big_arr[res-4:res+4]}")

    print(time.perf_counter() - mid)
