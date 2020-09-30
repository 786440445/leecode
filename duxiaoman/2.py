#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/20 9:11 PM
@Desc   ：
=================================================='''
class Solution():
    def __init__(self, n, ret):
        self.res = [[0] * n for _ in range(n)]
        for j in range(n):
            self.res[0][j] = 0
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    self.res[i][j] = i
                elif j < i:
                    old = self.res[i][j-1]
                    self.res[i][j] = ret[old]

    def func(self, x, k):
        print(self.res[x-1][k-1])


inp = list(map(int, (input().split(' '))))
n = inp[0]
q = inp[1]
an = list(map(int, (input().split(' '))))
ret = [0] * (n + 1)
for index, item in enumerate(an):
    ret[index + 2] = item

cli = Solution(n, ret)
for _ in range(q):
    inp = list(map(int, (input().split(' '))))
    x = inp[0]
    k = inp[1]
    cli.func(x, k)