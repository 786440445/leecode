#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/15 7:33 PM
@Desc   ：
=================================================='''

class Solution():
    def func(self, mat, m, n):
        if mat == []:
            return 0
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = mat[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1] + mat[i][j]
                if j == 0:
                    dp[i][j] = dp[i-1][j] + mat[i][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + mat[i][j]
        return dp[m-1][n-1]


inp = list(map(int, input().split(' ')))
m = inp[0]
n = inp[1]
mat = []
for i in range(m):
    inp = list(map(int, input().split(' ')))
    mat.append(inp)
print(Solution().func(mat, m, n))