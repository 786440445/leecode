#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 3
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/5 7:29 PM
@Desc   ：
=================================================='''
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param arr float浮点型一维数组
# @return int整型
#
class Solution:
    def find_best_cut(self, arr):
        # write code here
        if not arr:
            return
        best_index = 0
        min_v = float('inf')
        l = len(arr)
        if l > 100000:
            return
        ret1 = [0] * (l+1)
        ret2 = [0] * (l+1)
        v_1 = 0
        v_2 = 0
        for i in range(l):
            v_1 += arr[i]
            v_2 += arr[i] ** 2
            ret1[i+1] = v_1
            ret2[i+1] = v_2
        for k in range(l)[1:]:
            v = ret2[k] - (ret1[k] ** 2) / k
            u = ret2[l] - ret2[k] - ((ret1[l] - ret1[k]) ** 2) / (l-k)
            if v + u < min_v:
                best_index = k
                min_v = v + u
        return best_index


arr = list(map(int, input().split(',')))
ret = Solution().find_best_cut(arr)


print(ret)