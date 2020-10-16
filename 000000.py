#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 000000
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/10/9 7:10 PM
@Desc   ：
=================================================='''
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
        arr[high+1], arr[right] = arr[right], arr[high+1]
        return high + 1


def quick_sort(arr, low, high):
    if low < high:
        mid = partition(arr, low, high)
        quick_sort(arr, low, mid - 1)
        quick_sort(arr, mid + 1, high)


arr = [10, 1, 2, 6, 3, 7, 8, 4]
quick_sort(arr, 0, len(arr)-1)
print(arr)