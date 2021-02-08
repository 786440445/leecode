'''
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums):
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return

            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


# ret = Solution().permute([1, 2, 3])
# print(ret)
#coding=utf-8
import sys
#str = input()
#print(str)


def func(strs):
    res = []
    def recurr(path, tmp):
        if not path:
            res.append(tmp)
        for i in range(len(path)):
            recurr(path[:i] + path[i+1:], tmp + path[i])
    recurr(strs, '')
    print(res)

func('abc')