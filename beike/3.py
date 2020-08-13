#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 3
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/11 8:40 PM
@Desc   ：
=================================================='''

def func():
    m, n = input().split(' ')
    m = int(m)
    n = int(n)
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        str1 = input().split(' ')
        for j, v in enumerate(str1):
            matrix[i][j] = v
    print(matrix)

    for i in range(m):
        for j in range(n):

def dps(i, j, m, n):
    if i < m and j < n and i >= 0 and j >= 0:



func()