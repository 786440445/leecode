#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 3
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/13 7:55 PM
@Desc   ：
=================================================='''
def func():
    inp = [int(x) for x in input().split(' ')]
    n = inp[0]
    m = inp[1]
    if n > 100 or n <= 0:
        return 0
    if m < 1 or m > 120:
        return 0
    matrix = [[0, 0] for _ in range(n)]
    dict = {}
    for i in range(n):
        inp = [int(x) for x in input().split(' ')]
        matrix[i][0] = inp[0]
        matrix[i][1] = inp[1]
        # if inp[0] < 1 or inp[0] > 10:
        #     return 0
        # if inp[1] < 1 or inp[1] > 100:
        #     return 0
        if inp[0] <= m:
            dict[i] = inp[1] / inp[0]
    if not dict:
        return 0
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    sum = 0
    ret = 0
    for (k, v) in dict:
        sum += matrix[k][0]
        if sum <= m:
            ret += matrix[k][1]
        else:
            break
    return ret

print(func())