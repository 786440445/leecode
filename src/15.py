#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 15
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/6/7 8:31 PM
@Desc   ：
=================================================='''

'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums):
        l = len(nums)
        ret = []
        if l < 3:
            return ret
        nums.sort()
        for k in range(l):
            if nums[k] > 0:
                return ret
            if(k > 0 and nums[k] == nums[k-1]):
                continue

            right = l - 1
            left = k + 1
            while(left < right):
                if (nums[k] + nums[left] + nums[right]) == 0:
                    value = [nums[k], nums[left], nums[right]]
                    ret.append(value)
                    while(left < right and nums[left] == nums[left + 1]):
                        left = left + 1
                    while(left < right and nums[right] == nums[right - 1]):
                        right = right - 1
                    left += 1
                    right -= 1
                elif nums[k] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return ret


solu = Solution()
ret = solu.threeSum([-1, 0, 1, 2, -1, -4])
print(ret)
