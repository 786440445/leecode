'''
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0
        dp = [0] * l
        max_l = 0
        dp[0] = 0
        for i in range(1, l):
            if s[i] == ')' and s[i-1] == '(':
                dp[i] = dp[i-2] + 2
            elif s[i] == ')' and s[i-1] == ')':
                if s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
            max_l = max(max_l, dp[i])
        return max_l

ret = Solution().longestValidParentheses("()())")
print(ret)