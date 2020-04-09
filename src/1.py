'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        res = []
        for i, v in enumerate(nums):
            if dict.get(v) == None:
                dict[v] = [i]
            else:
                value = dict.get(v)
                dict[v] = value + [i]

        for i, (k, v) in enumerate(dict.items()):
            p = dict.get(target - k, [])
            if target == k * 2:
                if len(p) == 2:
                    res.append(v[0])
                    for index in p:
                        if i != index:
                            res.append(index)
                            return res
                else:
                    continue
            elif p != []:
                res.append(v[0])
                res.append(p[0])
                return res
        return res


result = Solution().twoSum([3, 2, 4], 6)
print(result)