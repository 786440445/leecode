#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/22 8:16 PM
@Desc   ：
=================================================='''


class Solution(object):
    def func(self):
        inp = [int(x) for x in input().split(' ')]
        n = inp[0]
        m = inp[1]
        if n < 2:
            return
        if n & 1 == 1:
            return
        if m > 100000:
            return
        op_list = input().split(' ')
        lis1 = list(range(1, n+1, 2))
        lis2 = list(range(2, n+1, 2))
        if len(op_list) != m:
            return
        for op in op_list:
            if op == '1':
                x = lis1[0]
                for i in range(n//2-1):
                    lis1[i], lis2[i] = lis2[i], lis1[i+1]
                lis1[n//2-1] = lis2[n//2-1]
                lis2[n//2-1] = x
            if op == '2':
                for i in range(n//2):
                    lis1[i], lis2[i] = lis2[i], lis1[i]
        ret = ''
        for i in range(n//2):
            ret += str(lis1[i]) + ' ' + str(lis2[i]) + ' '
        print(ret[:-1])

Solution().func()