#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 542
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/6/11 12:00 AM
@Desc   ：
=================================================='''
class Solution:
    def updateMatrix(self, matrix):
        h = len(matrix)
        w = len(matrix[0])
        ret = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]  # 设定结果集
        from collections import deque
        q = deque()
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    ret[i][j] = 0
                    q.append([i, j])
        while q:
            x, y = q.popleft()
            for x_bias, y_bias in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_x = x + x_bias
                new_y = y + y_bias
                if 0 <= new_x < h and 0 <= new_y < w and ret[new_x][new_y] == None:
                    ret[new_x][new_y] = ret[x][y] + 1
                    q.append([new_x, new_y])

        return ret



cli = Solution()
# ret1 = cli.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
# ret2 = cli.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1], [1, 1, 1]])

ret3 = cli.updateMatrix([[0,0,1,0,1,1,1,0,1,1],
                         [1,1,1,1,0,1,1,1,1,1],
                         [1,1,1,1,1,0,0,0,1,1],
                         [1,0,1,0,1,1,1,0,1,1],
                         [0,0,1,1,1,0,1,1,1,1],
                         [1,0,1,1,1,1,1,1,1,1],
                         [1,1,1,1,0,1,0,1,0,1],
                         [0,1,0,0,0,1,0,0,1,1],
                         [1,1,1,0,1,1,0,1,0,1],
                         [1,0,1,1,1,0,1,1,1,0]])


# print(ret1)
# print(ret2)
print(ret3)
