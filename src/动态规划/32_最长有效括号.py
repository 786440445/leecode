'''
32. 最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ret = []
        num = 0
        max_l = 0
        for c in s:
            if not ret:
                ret.append(c)
            else:
                top = ret[-1]
                if c == ')' and top == '(':
                    ret.pop()
                    num += 2
                else:
                    if c == '(' and top == ')':
                        num = 0
                        ret.append(c)
                    else:
                        ret.append(c)
            if num > max_l:
                max_l = num
        return max_l

# "()(()"
ret = Solution().longestValidParentheses("()(()")
print(ret)