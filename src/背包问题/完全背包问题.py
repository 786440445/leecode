'''
一个储物罐，w为空时重量，cur为当前重量，给定一些钱币的价值和相应重量，求储蓄罐中最少有多少现金
完全背包
1.放置 的物品可以无限多
2.背包恰好装满
input：
n=3
w=10，cur=110
2
1 1
30 50

w=10，cur=110
2
1 1
50 30

w=1，cur=6
2
10 3
20 4

输出
60
100
impossible
'''

class Solution:
    def func(self, w, cur, n, lis):
        s = cur - w
        dp = [float('inf')] * (s+1)
        dp[0] = 0
        for i in range(n):
            for j in range(lis[i][1], s+1):
                if dp[j-lis[i][1]] != float('inf'):
                    dp[j] = min(dp[j], dp[j-lis[i][1]] + lis[i][0])
        if dp[s] != float('inf'):
            print(dp[s])
        else:
            print('No')


cli = Solution()
cli.func(10, 110, 2, [[1, 1], [30, 50]])
cli.func(10, 110, 2, [[1, 1], [50, 30]])
cli.func(1, 6, 2, [[10, 3], [20, 4]])
