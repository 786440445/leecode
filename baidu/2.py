#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/3 8:51 PM
@Desc   ：
=================================================='''


import math
def func():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split(' '))))

    dp = [[0] * n for _ in range(n)]
    def dps(dp, matrix, x, y, cur_val, n):
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        if dp[x][y] <= cur_val:
            return
        else:
            dp[x][y] = cur_val

        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if matrix[newx][newy]:
                continue
            if newx < n and newx > 0 and newy > 0 and newy < n:
                val = matrix[x][y]
                matrix[x][y] = -1
                # dp[newx][newy] = dp[x][y] + abs(matrix[newx][newy] - matrix[x][y])
                dps(dp, matrix, newx, newy, cur_val + abs(val-matrix[x][y]), n)
                matrix[x][y] = val

    dps(dp, matrix, 0, 0, 0, n)
    print(dp[n-1][n-1])

func()