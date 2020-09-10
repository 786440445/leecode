#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/5 6:23 PM
@Desc   ：
=================================================='''
class Solution():
    def func(self):
        inp = list(map(int, input().split(',')))
        a = inp[0]
        b = inp[1]
        c = inp[2]
        if a < 1 or b < 1 or c < 1:
            return 0
        if a > 10e9 or b > 10e9 or c > 10e9:
            return 0
        min_num = min(a, b, c)
        if a + b + c >= 3*min_num + 4:
            return int((a + b + c - 3*min_num) / 4) + min_num
        else:
            return min_num


ret = Solution().func()
print(ret)