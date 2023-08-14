
def merge(arr, l, m, h):
    
    n1 = m - l + 1
    n2 = h - m
    L = [arr[l + i] for i in range(n1)]
    R = [arr[m + i + 1] for i in range(n2)]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return arr

def merge_sort(arr, l, h):
    if not l < h:
        return 
    m = (l+h) // 2
    merge_sort(arr, l, m)
    merge_sort(arr, m+1, h)
    merge(arr, l, m, h)


l1 = [7, 3, 5, 1, 9, 0]

l2 = [2, 4, 6, 8]
l3 = [1, 3, 5, 7]
t2 = merge_sort(l1, 0, len(l1)-1)
print(l1)
