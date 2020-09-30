#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/21 8:35 PM
@Desc   ：
=================================================='''


#
#
# @param num int整型 非负整数 num
# @return int整型一维数组
#
class Solution:
    def countBits(self, num):
        # write code here
        dp = [0] * (num + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for index in range(3, len(dp)):
            if index & 1 == 0:
                dp[index] = dp[index // 2]
            else:
                dp[index] = dp[index - 1] + 1
        return dp
print(Solution().countBits(10))
