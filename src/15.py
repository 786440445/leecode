#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 15
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/6/7 8:31 PM
@Desc   ：
=================================================='''


class Solution:
    def threeSum(self, nums):
        nums.sort()
        l = len(nums)
        ret = []
        for k in range(l):
            if nums[k] > 0:
                return ret
            else:
                for i in range(k+1, l):
                    for j in range(i+1, l):
                        if nums[k] + nums[i] + nums[j] == 0:
                            value = [nums[k],nums[i],nums[j]]
                            if value not in ret:
                                ret.append([nums[k],nums[i],nums[j]])
        return ret

solu = Solution()
ret = solu.threeSum([-1, 0, 1, 2, -1, -4])
print(ret)
