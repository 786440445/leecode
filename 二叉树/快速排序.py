def partition(arr, left, right):
    low = left
    high = right - 1
    pivot = arr[right]
    while low < high:
        while low < high and arr[low] <= pivot:
            low += 1
        while high > low and arr[high] > pivot:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

    if arr[high] > pivot:
        arr[high], arr[right] = arr[right], arr[high]
        return high
    else:
        arr[high + 1], arr[right] = arr[right], arr[high + 1]
        return high + 1


# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# arr = [10, 15, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print(arr)


# 快排求topk
def min_num(arr, m):
    start, end = 0, len(arr) - 1
    index = quick_index(arr, start, end)
    while index != m:
        if index < m:
            index = quick_index(arr, index + 1, end)
        else:
            index = quick_index(arr, start, index)
    return arr[:m]


def quick_index(arr, left, right):
    low = left
    high = right
    mid = arr[left]
    while low < high:
        while low < high and arr[high] <= mid:
            high -= 1
        if low < high:
            arr[low] = arr[high]
            low += 1
        while low < high and arr[low] >= mid:
            low += 1
        if low < high:
            arr[high] = arr[low]
            high -= 1
    arr[low] = mid
    return low


arr = [5, 2, 1, 3, 8, 7, 6, 4]
res = min_num(arr, 2)
print(res)



















