'''
224. 基本计算器
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1"
输出: 2
示例 2:

输入: " 2-1 + 2 "
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
'''

dict = {
    ('+', '-'): 1,
    ('-', '+'): 1,
    ('(', '-'): 0,
    ('(', '+'): 0,
    ('+', ')'): 1,
    ('-', ')'): 1,
}

#定义操作符的优先级
rank = {'+': 1,
        '-': 1,
        '(': 100,
        ')': -100
        }

class Solution:
    def calculate(self, s: str) -> int:
        nums_stack = []
        op_stack = []
        calc_flag = 1
        nums = 0
        # calc_state = False
        s = s.replace(' ', '')
        for i, c in enumerate(s):
            # 处理数字
            if '0' <= c <= '9':
                # 可能是多位数的情况
                if i != 0 and s[i - 1] >= '0' and s[i - 1] <= '9':
                    nums_stack[-1] = nums_stack[-1] * 10 + ord(c) - ord('0')
                else:
                    nums_stack.append(int(c))

            elif c == '(':
                op_stack.append(c)
            elif c == ')':
                while op_stack[-1] != '(':
                    do_op(op_stack, nums_stack)
                op_stack.pop()
            elif c == '+' or c == '-':
                while op_stack and (rank[c] >= rank[op_stack[-1]]):
                    do_op(op_stack, nums_stack)

                op_stack.append(c)
        while op_stack:
            do_op(op_stack, nums_stack)
        return nums_stack.pop()


def do_op(op_stack, nums_stack):
    if op_stack and len(nums_stack) >= 2:
        if op_stack[-1] == '+' or op_stack[-1] == '-':
            nums1 = nums_stack.pop()
            nums2 = nums_stack.pop()
            op = op_stack.pop()
            ret = calc(nums2, nums1, op)
            nums_stack.append(ret)


def calc(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b


# print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
# print(Solution().calculate('1-11'))
# print(Solution().calculate(" 2-1 + 2 "))
# print(Solution().calculate("0-2147483647"))
print(Solution().calculate("2-4-(8+2-6+(8+4-(1)+8-10))"))
