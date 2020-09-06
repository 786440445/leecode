#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 4
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/6 11:15 AM
@Desc   ：
=================================================='''
class Solution():
    def func(self, n, an):
        if n <= 0:
            return
        dp = [0]*n
        bn = [0]*n
        an_ = [0]*n
        for i in range(n):
            bn[i] = an[i] ^ an_[i]
            if i == 0:
                an_[0] = 1
                bn[0] = an[0] ^ an_[0]
                dp[0] = bn[0]
            else:
                if i % 2 == 0:
                    bn[i] = an[i] ^ an_[i] ^ (i+1)
                    dp[i] = dp[i - 1] ^ bn[i]
                else:
                    bn[i] = an[i] ^ an_[i]
                    dp[i] = dp[i - 1] ^ bn[i]
        return dp[n-1]


n = int(input())
an = list(map(int, input().split()))

ret = Solution().func(n, an)
print(ret)