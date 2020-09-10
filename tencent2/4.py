#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 4
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/6 8:32 PM
@Desc   ：
=================================================='''


def func(n, matrix):
    flag = False
    for i in range(n):
        f = True
        for j in range(6):
            if matrix[i][j] != matrix[i+1][j]:
                f = False
                break
        if f:
            flag = True
            break
    if flag:
        return 'YES'
    else:
        return 'NO'


t = int(input())
while t > 0:
    n = int(input())
    matrix = []
    for i in range(n):
        inp = list(map(int, input().split(' ')))
        inp.sort()
        matrix.append(inp)
    ret = func(n, matrix)
    print(ret)