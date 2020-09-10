'''
523. 连续的子数组和
给定一个包含 非负数 的数组和一个目标 整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，且总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。



示例 1：

输入：[23,2,4,6,7], k = 6
输出：True
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6。
示例 2：

输入：[23,2,6,4,7], k = 6
输出：True
解释：[23,2,6,4,7]是大小为 5 的子数组，并且和为 42。


说明：

数组的长度不会超过 10,000 。
你可以认为所有数字总和在 32 位有符号整数范围内。
'''

class Solution:
    def checkSubarraySum(self, nums, k) -> bool:
        stack = []
        for item in nums:
            if not stack:
                stack.append(item)
            else:
                tmp_list = calc_sum(stack)
                for le, tmp in enumerate(tmp_list):
                    if k == 0:
                        if item + tmp == 0:
                            return True
                    elif le+1 >= 1 and (item + tmp) % k == 0:
                        return True
                stack.append(item)
        return False


def calc_sum(stack):
    ret = []
    cum = 0
    for item in stack[::-1]:
        cum += item
        ret.append(cum)
    return ret


print(Solution().checkSubarraySum([23,2,4,6,7], 6))