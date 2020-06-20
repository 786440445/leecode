#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 673
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/6/9 12:04 AM
@Desc   ：
=================================================='''


class Solution:
    def findNumberOfLIS(self, nums):
        stack = []
        length = len(nums)
        if length == 1:
            return 1
        for k in range(length-1, 0, -1):
            if len(stack) == 0:
                stack.append(nums[k])
            else:
                pop = stack.pop()
                if nums[k] < pop:
                    return self.findNumberOfLIS(nums[:k])
                else:
                    return self.findNumberOfLIS(nums[:k]) + 1

solu = Solution()
ret = solu.findNumberOfLIS([1, 3, 5, 4, 7])
print(ret)