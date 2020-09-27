'''
647. 回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。



示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[False] * l for _ in range(l)]
        ans = 0
        for j in range(l):
            for i in range(j+1):
                if s[i] == s[j] and (j-i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans += 1
        return ans


res = Solution().countSubstrings("aaa")
print(res)