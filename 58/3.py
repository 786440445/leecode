#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 3
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/21 8:47 PM
@Desc   ：
=================================================='''
#
# 合并数组
# @param arrayA int整型一维数组 数组A
# @param arrayB int整型一维数组 数组B
# @return int整型一维数组
#
class Solution:
    def mergerArrays(self , arrayA , arrayB ):
        # write code here
        i = 0
        j = 0
        l1 = len(arrayA)
        l2 = len(arrayB)
        ret = []
        while i < l1 and j < l2:
            if arrayA[i] > arrayB[j]:
                j += 1
            elif arrayA[i] < arrayB[j]:
                i += 1
            else:
                ret.append(arrayA[i])
                i += 1
                j += 1
        return ret

print(Solution().mergerArrays([-5,0,6,8,9,10],[0,8,9,11,15]))

