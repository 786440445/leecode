'''
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''

class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 0 and n == 0:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    pass
                else:
                    if i == 0:
                        dp[i][j] = dp[i][j-1] + grid[i][j]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j] + grid[i][j]
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]


print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))