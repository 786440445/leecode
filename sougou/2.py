#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/5 7:04 PM
@Desc   ：
=================================================='''
class Solution:
    def getHouses(self, t, xa):
        # write code here
        if t <= 0:
            return
        if not xa:
            return
        l = len(xa)
        count = 0
        left = xa[0] + xa[1]//2
        for index in range(l//2):
            if xa[2*index] - xa[2*index+1]//2 - left == t:
                count += 1
            if xa[2*index] - xa[2*index+1]//2 - left > t:
                count += 2
            left = xa[2*index] + xa[2*index+1]//2
        count += 2
        return count


t = int(input())
xa = list(map(int, input().split(',')))
ret = Solution().getHouses(t, xa)
print(ret)