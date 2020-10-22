#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/10/16 9:38 AM
@Desc   ：
=================================================='''
import functools


def cmp(x, y):
    if x[0] > y[0]:
        return 1
    if x[0] < y[0]:
        return -1
    if x[1] > y[1]:
        return -1
    if x[1] < y[1]:
        return 1
    return 0


if __name__ == '__main__':
    n = int(input())
    mat = []
    while n > 0:
        inp = list(map(int, input().split(' ')))
        mat.append(inp)
        n -= 1

    mat = sorted(mat, key=functools.cmp_to_key(cmp))
    print(mat)
    nums = 1
    old_l = mat[0][0]
    old_r = mat[0][1]
    max_v = float('-inf')
    for l, r in mat[1:]:
        if r <= old_r:
            nums += 1
            old_r = r
        else:
            nums = 1
            old_l = l
            old_r = r

    if nums > max_v:
        max_v = nums
    print(max_v)
    #
    # dp = [[0]* n for _ in range(n)]
    # for i in range(n):
    #     for j in range(i+1, n):
