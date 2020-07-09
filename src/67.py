"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        status = 0
        a = a[::-1]
        b = b[::-1]
        la = len(a)
        lb = len(b)
        l = max(la, lb)
        ret = ''
        for i in range(l):
            if i >= la:
                tmp_a = 0
            else:
                tmp_a = int(a[i])
            if i >= lb:
                tmp_b = 0
            else:
                tmp_b = int(b[i])

            if tmp_a + tmp_b + status < 2:
                ret += str(tmp_a + tmp_b + status)
                status = 0
            elif tmp_a + tmp_b + status == 2:
                ret += '0'
                status = 1
            elif tmp_a + tmp_b + status == 3:
                ret += '1'
                status = 1
        if status == 1:
            ret += str(status)
        return ret[::-1]


soli = Solution()
print(soli.addBinary('11', '1'))
# 10101
# b = '1011'
# c = b[1:][::-1]
# print(repr(c))