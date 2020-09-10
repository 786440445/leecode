#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/6 7:54 PM
@Desc   ：
=================================================='''

class Solution():
    def func(self, n, strs):
        dp1 = [1]*n
        dp2 = [1]*n
        for i in range(n, 1, -1):  ## 递增序列
            for j in range(i, n):
                if strs[i] < strs[j]:
                    dp1[i] = max(dp1[i], dp1[j] + 1)

        for i in range(0, n):   ## 递减序列
            for j in range(0, i):
                if strs[i] > strs[j]:
                    dp2[i] = max(dp2[i], dp2[j] + 1)

        max_l = 0
        for i in range(n):
            for j in range(i, n):
                if strs[i] == strs[j]:
                    max_l = max(max_l, 2*min(dp2[i], dp1[j]))
        return max_l


n = int(input())
cli = Solution()
while n > 0:
    l = int(input())
    strs = list(map(int, input().split(' ')))
    ret = cli.func(l, strs)
    print(ret)
    n -= 1

# 5 4 3 2 3 2 4 5 6
# 5 4 3 2 1 2 3 4 5
