def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[low]
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

#
# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print(arr)


def quick_sort(arr, k):
    """快速排序"""
    if len(arr) < 2:
        return arr
    mid = arr[0]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    arr.remove(mid)
    for item in arr:
        # 大于基准值放右边
        if item >= mid:
            k -= 1
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
        if k == 0:
            print(item)
    # 使用迭代进行比较
    return quick_sort(left, k) + [mid] + quick_sort(right, k)


arr = quick_sort([10, 7, 8, 9, 1, 5], 4)
print(arr)
