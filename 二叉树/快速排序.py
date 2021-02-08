# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = quick_index(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def quick_index(arr, left, right):
    low = left
    high = right
    mid = arr[left]
    while low < high:
        while low < high and arr[high] <= mid:
            high -= 1
        if low < high:
            arr[low] = arr[high]

        while low < high and arr[low] > mid:
            low += 1
        if low < high:
            arr[high] = arr[low]
    arr[low] = mid
    return low


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


arr = [5, 2, 1, 3, 8, 7, 6, 4]
res = min_num(arr, 2)
res1 = quickSort(arr, 0, len(arr)-1)
print(arr)
print(res)



















