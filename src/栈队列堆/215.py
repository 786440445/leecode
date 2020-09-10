'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
'''

from heapq import *

class Solution:
    def findKthLargest(self, nums, k) -> int:
        heap = []
        heapify(heap)
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]


import random

class Solution1:
    def findKthLargest(self, A, k) -> int:
        def partition(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if A[i] > pivot_value:
                    A[i], A[new] = A[new], A[i]
                    new += 1
            A[new], A[right] = A[right], A[new]
            return new

        left, right = 0, len(A) - 1
        while left <= right:
            pivot_idx = left
            new = partition(left, right, pivot_idx)
            if new == k - 1:
                return A[new]
            elif new > k - 1:
                right = new - 1
            else:
                left = new + 1


print(Solution1().findKthLargest([9,3,2,4,5,6,1,7,8], 3))
