'''
51. N皇后
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。


提示：

皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自 百度百科 - 皇后 ）
'''

import copy

# 回溯算法
class Solution:
    def solveNQueens(self, n: int):
        mask = [[0] * n for _ in range(n)]
        location = [["." for _ in range(n)] for _ in range(n)]
        result = []
        self.generate(0, n, location, result, mask)
        self.print_matrix(result)

    def print_matrix(self, result):
        m = len(result)
        for i in range(m):
            res = ''
            l = len(result[i])
            for j in range(l):
                res += ' '.join(result[i][j]) + '\n'
            print(res)

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
                self.putdown(mask, k, i, n)
                self.generate(k+1, n, location, result, mask)
                mask = tmp_mark
                location[k][i] = "."

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
#
# # 递归算法
# class Solution1:
#     def solveNQueens(self, n: int):
#         def check(nums, new):
#             for i in range(len(nums)):
#                 if abs(new - nums[i]) in (0, len(nums) - i):
#                     return False
#             return True
#
#         # 构建初始map
#         mapping, ans = ['.' * i + 'Q' + '.' * (n - i - 1) for i in range(n)], []
#
#         def backtrack(nums):
#             if len(nums) == n:
#                 ans.append([mapping[c] for c in nums])
#                 return
#
#             for i in range(n):
#                 if check(nums, i):
#                     backtrack(nums + [i])
#
#         backtrack([])
#         return ans
#
# def print_matrix(ans):
#     pass
#
# n = int(input('输入皇后个数：'))
# ret = Solution1().solveNQueens(n)
# print_matrix(ret)
