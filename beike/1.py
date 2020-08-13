#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/11 7:02 PM
@Desc   ：
=================================================='''
from itertools import combinations


def gys(x, y):
    x = int(x)
    y = int(y)
    k = min(x, y)
    for i in range(2, k+1):
        if x % k == 0 and y % k == 0:
            return i
    return 1


def func():
    k = int(input())
    res = []
    for _ in range(k):
        n = int(input())
        n_str = input().split(' ')
        if '1' in n_str:
            res.append(-1)
            continue
        flag = True
        for x, y in combinations(n_str, 2):
            if gys(x, y) == 1:
                flag = False
        if flag:
            res.append(0)
        else:
            res.append(-1)
    return res
print(func())