#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 456
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/6/7 9:35 PM
@Desc   ：
=================================================='''
class Solution:
    def find132pattern(self, nums) -> bool:
        ak = float("-inf")
        max = []
        if len(nums) < 3:
            return False
        for num in nums:
            if ak > num:
                return True
            while max and max[-1] < num:
                ak = max.pop()
            max.append(num)
        return False



cli = Solution()
ret1 = cli.find132pattern([-2, 1, 2, -2, 1, 2])
# ret2 = cli.find132pattern([1, 2, 3, 4])
# ret3 = cli.find132pattern([3, 1, 4, 2])
print(ret1)
# print(ret2)
# print(ret3)