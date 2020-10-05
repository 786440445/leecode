'''
多重背包问题
容积为V的背包，给定一些物品，每个物品包含体积w，价值v，和数量k，求用该背包装下的最大价值总量

资金n元
m种大米
p，h，c代表每种大幕的价格，重量，及袋数
问：用有限的资金最多能采购多少公斤粮食
输入：
1
8 2
2 100 4
4 100 2

输出：
400
'''

class Solution:
    def func(self, n, m, lis):
        dp = [0]*(n+1)
        str1 = [[0, 0] for _ in range(1000)]
        cnt = 0
        for i in range(m):
            p = lis[i][0]
            w = lis[i][1]
            k = lis[i][2]
            c = 1
            while k > c:
                k -= c
                str1[cnt][0] = c * p
                str1[cnt][1] = c * w
                c = c * 2
                cnt += 1
            str1[cnt][0] = k * p
            str1[cnt][1] = k * w
            cnt += 1
        for i in range(cnt):
            for j in range(n, str1[i][0]-1, -1):
                dp[j] = max(dp[j], dp[j-str1[i][0]] + str1[i][1])
        print(dp[n])


cli = Solution()
cli.func(8, 2, [[2, 100, 4], [4, 100, 2]])

