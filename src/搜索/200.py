'''
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。



示例 1:

输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1
示例 2:

输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
'''

class Solution:
    def numIslands(self, grid) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        isiland = 0
        mark = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mark[i][j] == 0 and grid[i][j] == '1':
                    self.dfs(i, j, mark, grid)
                    isiland += 1
        return isiland

    def dfs(self, x, y, mark, grid):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        mark[x][y] = 1
        for i in range(4):
            newx = dx[i] + x
            newy = dy[i] + y
            if newx < 0 or newx >= len(mark) or newy < 0 or newy >= len(mark[0]):
                continue
            if mark[newx][newy] == 0 and grid[newx][newy] == '1':
                self.dfs(newx, newy, mark, grid)

print(Solution().numIslands(
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
))