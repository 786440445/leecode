class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0] * l2 for _ in range(l1)]
        max_l = 0
        for i in range(l1):
            for j in range(l2):
                if text1[i] != text2[j]:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_l:
                    max_l = dp[i][j]
        return max_l


ret = Solution().longestCommonSubsequence("abcde", "ace")
print(ret)