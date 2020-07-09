'''
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
'''


class Solution:
    def generateParenthesis(self, n: int):
        if n == 1:
            return ['()']
        else:
            ret = self.generateParenthesis(n-1)
            new_ret = []
            for item in ret:
                for i in range(len(item)):
                    new_item = item[:i] + '()' + item[i:]
                    if new_item not in new_ret:
                        new_ret.append(new_item)
            return new_ret


cli = Solution()
ret = cli.generateParenthesis(3)
print(ret)