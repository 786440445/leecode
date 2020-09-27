'''
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def right_index():
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if target == nums[mid]:
                    if mid == len(nums)-1 or target < nums[mid + 1]:
                        return mid
                    start = mid + 1
                elif target > nums[mid]:
                    start = mid + 1
                elif target < nums[mid]:
                    end = mid - 1

        def left_index():
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                if target == nums[mid]:
                    if target > nums[mid-1] or mid == 0:
                        return mid
                    else:
                        end = mid - 1
                elif target > nums[mid]:
                    start = mid + 1
                elif target < nums[mid]:
                    end = mid - 1

        index1 = left_index()
        index2 = right_index()
        if index1 == None:
            return [-1, -1]
        return [index1, index2]

ret = Solution().searchRange([1], target = 1)
print(ret)