'''
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''

class Solution:
    def maxSubArray(self, nums) -> int:
        if nums == []:
            return 0
        l = len(nums)
        dp = [0] * l
        dp[0] = nums[0]
        if l == 1:
            return dp[0]
        for index in range(1, l):
            if dp[index-1] > 0:
                dp[index] = dp[index-1] + nums[index]
            else:
                dp[index] = nums[index]
        return max(dp)

print(Solution().maxSubArray([-2, 1]))

