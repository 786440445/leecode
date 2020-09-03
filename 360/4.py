#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 4
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/24 11:13 AM
@Desc   ：
=================================================='''
inp = list(map(int, input().split(' ')))
m = inp[0]
n = inp[1]
# dp = [0] * (n+1)
matrix = [[0] * n for _ in range(m)]
for i in range(m):
    inp = list(map(int, input().split(' ')))
    for j in range(n):
        matrix[i][j] = inp[j]

dp = [[0] * n for _ in range(m)]

for i in range(0, n):  # 物品数
    j = 0
    max_count = 0
    while(j < m):
        if i == 0:
            if max_count < matrix[j][i]:
                max_count = matrix[j][i]
                dp[j][i] = max_count
            else:
                pass
        else:
            for k in range(0, i):
                if max_count < matrix[j][n-k-1] + matrix[j][k]:
                    max_count = matrix[j][n-k-1] + matrix[j][k]
            dp[j][i] = max_count
        j += 1
print(dp[m-1][n-1])
