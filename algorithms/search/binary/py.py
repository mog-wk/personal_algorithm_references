
def binary_search(arr, n, k):
    l, h = 0, n

    while l <= h:
        m = (h + l) // 2
        print(l, h, m, k, arr[m])
        if arr[m] == k:
            return m
        if arr[m] > k:
            h = m - 1
        else:
            l = m + 1

    return 0

def binary_recursive(arr, l, h, k):
    if h < l: return 0
    m = (l + h) // 2

    if arr[m] == k:
        return m
    if arr[m] > k:
        return binary_recursive(arr, l, m-1, k)
    else:
        return binary_recursive(arr, m+1, h, k)



if __name__ == "__main__":

    data = [1, 6, 7, 12, 16, 19, 21, 30, 36, 47, 50]

    ind = binary_search(data, len(data)-1, 12)
    ind2 = binary_recursive(data, 0, len(data)-1, 12)
    print(data[ind], ind, ind2)
