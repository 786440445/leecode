'''
剑指 Offer 29. 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。



示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
'''


class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        ret = self.board(0, 0, m, n, [], matrix, visited, direction='r')
        return ret

    def board(self, i, j, m, n, ret, matrix, visited, direction):
        if i <= 0 or j <= 0 or i >= m-1 or j >= n-1 and direction =='r' and visited[i][j+1]:

            ret = ret.append(matrix[i, j])
            return self.board(i, j, m, n, ret, matrix, visited, direction='b')
        elif:
            return self.board(i, j, m, n, ret, matrix, visited, direction='b')







