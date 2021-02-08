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
        if not matrix:
            return []
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []
        while left <= right and up <= down:
            for i in range(left, right + 1):
                res.append(matrix[left][i])
            up += 1
            if up > down:
                break

            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break

            for i in range(right, left-1, -1):  # 右到左
                res.append(matrix[down][i])
            down -= 1
            for i in range(down, up-1, -1):  # 下到上
                res.append(matrix[i][left])
            left += 1
        return res


class Solution1:
    def __init__(self):
        self.move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        d = 0
        visited = [[False] * n for _ in range(m)]
        res = []
        self.dps(res, visited, matrix, 0, 0, m, n, d, 0)
        return res

    def check(self, x, y, m, n, visited):
        if x >= 0 and y >= 0 and x < m and y < n and not visited[x][y]:
            return True
        else:
            return False

    def dps(self, path, visited, matrix, x, y, m, n, d, count):
        visited[x][y] = True
        path.append(matrix[x][y])
        if count == m*n - 1:
            return
        if self.check(x + self.move[d][0], y + self.move[d][1], m, n, visited):
            self.dps(path, visited, matrix, x + self.move[d][0], y + self.move[d][1], m, n, d, count+1)
        else:
            # 换方向，因此不做处理
            visited[x][y] = False
            path.pop()
            d = (d + 1) % 4
            self.dps(path, visited, matrix, x, y, m, n, d, count)


res = Solution1().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(res)