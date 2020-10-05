'''
91. 解码方法
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        dp = [0]*l
        for index in range(l):
            if index == 0:
                if '1' <= s[index] <= '9':
                    dp[index] = 1
            else:
                if s[index] != '0' and s[index-1] != '0' and 1 <= int(s[index-1]) * 10 + int(s[index]) <= 26:
                    dp[index] = dp[index-1] + 1
                else:
                    dp[index] = dp[index-1]
        return dp[l-1]

res = Solution().numDecodings('10')
print(res)