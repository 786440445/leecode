'''
剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。



示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
'''

class Solution:
    def translateNum(self, num: int) -> int:
        if num == 0:
            return 1
        stack = []
        while num > 0:
            a = num % 10
            stack.append(a)
            num = num // 10
        l = len(stack)
        dp = [0] * l
        dp[0] = 1
        stack.reverse()
        for i in range(1, l):
            if i == 1:
                if stack[i-1] != 0 and 0 <= stack[i-1] * 10 + stack[i] <= 25:
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = dp[i - 1]
            elif stack[i-1] != 0 and 0 <= stack[i-1] * 10 + stack[i] <= 25:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return (dp[l-1])


res = Solution().translateNum(506)
print(res)