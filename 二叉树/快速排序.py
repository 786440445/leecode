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

#

# l = left + 1
#             r = right
#             while l <= r:
#                 if nums[l] < pivot and nums[r] > pivot:
#                     nums[l], nums[r] = nums[r], nums[l]
#                 if nums[l] >= pivot:
#                     l += 1
#                 if nums[r] <= pivot:
#                     r -= 1


arr = [10, 15, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print(arr)






#
# def quick_sort(arr):
#     """快速排序"""
#     if len(arr) < 2:
#         return arr
#     mid = arr[0]
#     # 定义基准值左右两个数列
#     left, right = [], []
#     # 从原始数组中移除基准值
#     arr.remove(mid)
#     for item in arr:
#         # 大于基准值放右边
#         if item >= mid:
#             # k -= 1
#             right.append(item)
#         else:
#             # 小于基准值放左边
#             left.append(item)
#     # 使用迭代进行比较
#     return quick_sort(left) + [mid] + quick_sort(right)
#
#
# arr = quick_sort([10, 7, 8, 9, 1, 5])
# print(arr)
