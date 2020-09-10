'''
120. 三角形最小路径和
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。



例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。



说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
'''

class Solution:
    def minimumTotal(self, triangle):
        m = len(triangle)
        n = len(triangle[-1])
        dp = [[0] * x for x in range(1, n+1)]
        for j in range(n):
            dp[m-1][j] = triangle[m-1][j]
        for i in range(m-2, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]


print(Solution().minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
