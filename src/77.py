'''
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(n, count, begin, end, k, res, path):
            if count == k:
                res.append(path)
                return
            for j in range(begin, end):
                helper(n, count+1, j+1, end, k, res, path + [j+1])

        res = []
        path = []
        helper(n, 0, 0, n, k, res, path)
        return res


Solution().combine(4, 2)


