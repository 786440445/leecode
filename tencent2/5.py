#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 5
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/6 9:27 PM
@Desc   ：
=================================================='''

class Solution():
    def func(self, t, graph):



        pass


inp = list(map(int, input().split(' ')))
m, n, t = inp[0], inp[1], inp[2]
graph = [[float('inf')] * n for i in range(n)]
for i in range(m):
    inp = list(map(int, input().split(' ')))
    x, y, d = inp[0], inp[1], inp[2]
    graph[x][y] = d

Solution().func(t, graph)