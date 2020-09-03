#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/3 6:52 PM
@Desc   ：
=================================================='''

from functools import cmp_to_key


def cmp(x1, x2):
    if x1[2] != x2[2]:
        return x2[2] - x1[2]
    if x1[0] != x2[0]:
        return x1[0] - x2[0]
    else:
        return x1[1] - x2[1]

ret = [[1, 2, 3], [4, 3, 2], [4, 3, 3], [3, 3, 3], [3, 4, 3], [2, 5, 4]]
ret = sorted(ret, key=cmp_to_key(cmp))


#
print(ret)
# def func():
#     inp = [int(x) for x in input().split(' ')]
#     n = inp[0]
#     m = inp[1]
#     k = inp[2]
#     if n >= 10e5:
#         return
#     if m >= 100:
#         return
#     if k >= 10000:
#         return
#     things = []
#     for i in range(n):
#         inp = [int(x) for x in input().split(' ')]
#         price = inp[0]
#         weight = inp[1]
#         value = inp[2]
#         things.append([price, weight, value])
#
#     things = sorted(things, key=cmp_to_key(cmp))
#     # print(things)
#     weights = 0
#     prices = 0
#     i = 0
#     while weights + things[i][1] <= m and prices + things[i][0] <= k:
#         weights += things[i][1]
#         prices += things[i][0]
#         i += 1
#     print(i)
#
# func()