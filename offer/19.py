#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 19
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/10/24 1:36 PM
@Desc   ：
=================================================='''
'''
剑指 Offer 19. 正则表达式匹配
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = '#' + s, '#' + p
        m, n = len(s), len(p)
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True

        for i in range(m):
            for j in range(1, n):
                if i == 0:
                    dp[i][j] = j > 1 and p[j] == '*' and dp[i][j-2]
                elif p[j] in [s[i], '.']:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    dp[i][j] = j > 1 and dp[i][j - 2] or p[j - 1] in [s[i], '.'] and dp[i - 1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]


res = Solution().isMatch('aab', 'c*a*b')
print(res)
# Solution().isMatch('aa', 'a.')
# Solution().isMatch('aa', 'a*')
# Solution().isMatch('ab', 'a*')
# Solution().isMatch('ab', 'a.')
# Solution().isMatch('ab', 'a')

