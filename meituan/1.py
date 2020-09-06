#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/6 9:53 AM
@Desc   ：
=================================================='''
class Solution():
    def func(self, n, p, q, list_p, list_q):
        dict = {}
        count = 0
        for item in list_p:
            dict[item] = 1
        for item in list_q:
            if dict.get(item, 0) == 1:
                count += 1
        print(p-count, q-count, count)


inp = list(map(int, input().split(' ')))
n = inp[0]
p = inp[1]
q = inp[2]
list_p = list(map(int, input().split(' ')))
list_q = list(map(int, input().split(' ')))
Solution().func(n, p, q, list_p, list_q)