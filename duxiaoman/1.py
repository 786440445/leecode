#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/20 8:03 PM
@Desc   ：
=================================================='''

class Solution():
    def func(self, mat, n, m):
        dp = [[float('inf')] * m for _ in range(n)]
        flag = [[False] * m for _ in range(n)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def is_all(flag):
            for i in range(n):
                for j in range(m):
                    if not flag[i][j]:
                        return False
            return True

        def dps(x, y):
            if is_all(flag):
                return
            for k in range(4):
                newx = x + dx[k]
                newy = y + dy[k]
                if 0 <= newx < n and 0 <= y < m:
                    if mat[newx][newy] == '.':
                        flag[newx][newy] = True
                        dp[newx][newy] = dp[x][y]
                    elif mat[newx][newy] == '*':
                        flag[newx][newy] = True
                        if newx == 0 and newy == 0:
                            dp[newx][newy] = min(dp[newx][newy+1], dp[newx+1][newy])
                        elif newx == n and newy == m:
                            dp[newx][newy] = min(dp[newx][newy-1], dp[newx-1][newy])
                        elif newx == 0 and newy == m:
                            dp[newx][newy] = min(dp[newx][newy-1], dp[newx+1][newy])
                        elif newx == n and newy == 0:
                            dp[newx][newy] = min(dp[newx-1][newy], dp[newx][newy+1])
                        elif newx == 0:
                            dp[newx][newy] = min(dp[newx][newy+1], dp[newx][newy-1], dp[newx+1][newy])
                        elif newy == 0:
                            dp[newx][newy] = min(dp[newx][newy+1], dp[newx+1][newy], dp[newx-1][newy])
                        else:
                            dp[newx][newy] = min(dp[newx][newy+1], dp[newx+1][newy], dp[newx-1][newy], dp[newx][newy-1])

                    elif mat[newx][newy] == '#':
                        flag[newx][newy] = True
                        dp[newx][newy] = float('inf')

        for i in range(n):
            for j in range(m):
                if mat[i][j] == '@':
                    dps(i, j)


k = int(input())
cli = Solution()
while k > 0:
    inp = list(map(int, input().split()))
    n = inp[0]
    m = inp[1]
    mat = []
    for _ in range(n):
        inp = input().split(' ')
        mat.append(inp)
    ret = cli.func(mat, n, m)
    print(ret)
    k -= 1