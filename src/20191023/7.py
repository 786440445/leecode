'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    @classmethod
    def reverse(self, x):
        total = 0
        if x < 0:
            x = abs(x)
            sum = []
            while (x != 0):
                sum.append(x % 10)
                x = x // 10
            l = len(sum)
            for i, v in enumerate(sum):
                total += v * pow(10, l - i - 1)
            total = 0-total

        else:
            sum = []
            while(x != 0):
                sum.append(x % 10)
                x = x // 10
            l = len(sum)
            for i, v in enumerate(sum):
                total += v * pow(10, l-i-1)

        if total.bit_length() < 32:
            return total
        else:
            return 0


print(Solution().reverse(pow(2, 31)-1))
print(Solution().reverse(-pow(2, 31)))
print(Solution().reverse(1463847412))
a = pow(2, 31)-1
b = -pow(2, 31)
c = 7463847412
d = 2147483647
print(c.bit_length())
print(d.bit_length())