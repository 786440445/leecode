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
    for i in range(n)[1:]:
        sum = matrix[i][0] ^ matrix[i][1] ^ matrix[i][2] ^ matrix[i][3] ^ matrix[i][4] ^ matrix[i][5]
        a =



t = int(input())
while t > 0:
    n = int(input())
    matrix = []
    for i in range(n):
        inp = list(map(int, input().split(' ')))
        matrix.append(inp)
    ret = func(n, matrix)
    print(ret)