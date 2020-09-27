'''
剑指 Offer 61. 扑克牌中的顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。



示例 1:

输入: [1,2,3,4,5]
输出: True


示例 2:

输入: [0,0,1,2,5]
输出: True
'''

from typing import List

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        d = {}
        min_num = float('inf')
        max_num = float('-inf')
        for i in nums:
            if i != 0:
                d[i] = d.get(i, 0) + 1
                if d[i] == 2:
                    return False
                if i > max_num:
                    max_num = i
                if i < min_num:
                    min_num = i
            else:
                pass
        return max_num - min_num < 5


print(Solution().isStraight([1, 2, 12, 0, 3]))
print(Solution().isStraight([11, 10, 0, 0, 12]))

