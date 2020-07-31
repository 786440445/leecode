'''
剑指 Offer 10- I. 斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。



示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5


提示：

0 <= n <= 100
'''
import math


class Solution:
    def fib(self, n: int) -> int:
        tmp_list = [0] * 101
        for index in range(len(tmp_list)):
            if index == 0:
                tmp_list[index] = 0
            elif index == 1:
                tmp_list[index] = 1
            else:
                tmp_list[index] = tmp_list[index-1] + tmp_list[index-2]
        return tmp_list[n] % 1000000007


print(Solution().fib(1))
print(Solution().fib(2))
print(Solution().fib(3))
print(Solution().fib(4))
print(Solution().fib(5))