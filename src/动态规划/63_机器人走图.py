'''
63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
'''

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid == []:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                elif i == 0:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = 0
                elif j == 0:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = 0
                else:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        if obstacleGrid[i-1][j] != 1:
                            dp[i][j] += dp[i-1][j]
                        if obstacleGrid[i][j-1] != 1:
                            dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]

res = Solution().uniquePathsWithObstacles([[1]])
print(res)
