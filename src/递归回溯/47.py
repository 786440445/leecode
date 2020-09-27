'''
47. 全排列 II
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dps(nums, res, path):
            if not nums:
                res.append(path)
                return
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] in nums[:i]:
                        continue
                    else:
                        dps(nums[:i] + nums[i+1:], res, path + [nums[i]])

        res = []
        path = []
        dps(nums, res, path)
        return res


Solution().permuteUnique([1, 1, 2])

