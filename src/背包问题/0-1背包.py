'''
0-1   背包问题
'''

class Solution():
    def func(self, lis, V, N):
        dp = [0]*(V+1)
        for i in range(V+1):
            dp[i] = 0

        for i in range(1, N+1):
            for j in range(V, -1, -1):
                if lis[i-1][0] <= j:
                    dp[j] = max(dp[j], dp[j-lis[i-1][0]] + lis[i-1][1])
                else:
                    continue
        return dp[V]


res = Solution().func([[71, 100], [69, 1], [1, 2]], 70, 3)
print(res)