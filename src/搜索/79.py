'''
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

'''
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def dps(matrix, board, i, j, m, n, word, count):
            if board[i][j] != word[count]:
                return False
            if count == len(word) - 1:
                return True

            matrix[i][j] = True
            for k in range(4):
                newi = i + dx[k]
                newj = j + dy[k]
                if 0 <= newi < m and 0 <= newj < n:
                    if not matrix[newi][newj] and dps(matrix, board, newi, newj, m, n, word, count + 1):
                        return True
            matrix[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                matrix = [[False] * n for _ in range(m)]
                if dps(matrix, board, i, j, m, n, word, 0):
                    return True
        return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word0 = "ABCESEEEFS"
word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"

ret0 = Solution().exist(board, word0)
ret1 = Solution().exist(board, word1)
ret2 = Solution().exist(board, word2)
ret3 = Solution().exist(board, word3)

print(ret0)
print(ret1)
print(ret2)
print(ret3)