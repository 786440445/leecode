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
        ret = []
        count1 = 0
        count2 = 0
        min = float('inf')
        state = True
        for item in strs:
            if item < min:
                min = item
                count1 += 1
            elif item == min:
                state = False
                continue
            else:
                pass
        return min(count1, count2)




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
