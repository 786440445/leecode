#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> mm
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/10/17 6:25 PM
@Desc   ：
=================================================='''
import math


class Solution:
    def fun(self, start, stop):
        # write code here
        res = []
        for num in range(start, stop):
            if self.is_sushu(num):
                res.append(num)
        return res

    def is_sushu(self, num):
        for i in range(2, math.ceil(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

res = Solution().fun(2, 5)
print(res)