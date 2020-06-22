'''
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''

# 动态规划
# 1.s[i] = s[i+1]
# 2.s[i] = s[j] and ret[i+1][j-1]
# 3.i == j

class Solution:
    def longestPalindrome(self, s: str):
        length = len(s)
        result = [[False for _ in range(length)] for _ in range(length)]
        ans = ""
        for l in range(length):
            for i in range(length):
                j = i + l
                if j >= length:
                    break
                if l == 0:
                    result[i][j] = True
                elif l == 1 and s[i] == s[j]:
                    result[i][j] = True
                else:
                    result[i][j] = (result[i+1][j-1] and s[i] == s[j])
                if result[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans


solu = Solution()
solu.longestPalindrome("abcba")
