#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/6 10:10 AM
@Desc   ：
=================================================='''
class Solution():
    def func(self, s):
        nums_1 = 0
        nums_2 = 0
        for item in s:
            if 'a' <= item <= 'z':
                nums_1 += 1
            if 'A' <= item <= 'Z':
                nums_2 += 1

        print(abs(nums_1 - nums_2) // 2)


s = input()
Solution().func(s)