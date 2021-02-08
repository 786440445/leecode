#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import copy


# 回溯算法
class Solution:
    def solveNQueens(self, n: int):
        mask = [[0] * n for _ in range(n)]
        location = [["." for _ in range(n)] for _ in range(n)]
        result = []
        self.generate(0, n, location, result, mask)
        for res in result:
            self.print_matrix(res)
            input()

    # 矩阵打印输出
    def print_matrix(self, result):
        res = ''
        for item in result:
            res += ' '.join(item) + '\n'
        print(res)

    # 生成八皇后
    def generate(self, k, n, location, result, mask):
        if k == n:
            ret = ''
            ret = [ret + ''.join(x) for x in location]
            result.append(ret)
            return

        for i in range(n):
            if mask[k][i] == 0:
                tmp_mark = copy.deepcopy(mask)
                location[k][i] = "Q"
                # 落字
                self.putdown(mask, k, i, n)
                self.generate(k+1, n, location, result, mask)
                mask = tmp_mark
                location[k][i] = "."

    # 尝试下棋
    def putdown(self, mask, x, y, n):
        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, -1, 1, -1, 1, -1, 1]
        mask[x][y] = 1
        for i in range(1, n):
            for j in range(8):
                newx = x + i * dx[j]
                newy = y + i * dy[j]
                if newx >= 0 and newx < n and newy >= 0 and newy < n:
                    mask[newx][newy] = 1


n = int(input('输入皇后个数：'))
ret = Solution().solveNQueens(n)
