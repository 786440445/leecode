'''
300. 最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''

class Solution:
    def lengthOfLIS(self, nums) -> int:
        l = len(nums)
        if l == 0:
            return 0
        dp = [1] * l
        for i in range(1, l):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
        return max(dp)


class Solution1:
    def lengthOfLIS(self, nums) -> int:
        stack = []
        ret = 0
        for item in nums:
            if stack:
                if item > stack[-1]:
                    stack.append(item)
                elif item == stack[-1]:
                    continue
                else:
                    i = binary_search(stack, item)
                    stack[i] = item
            else:
                stack.append(item)
            ret = max(ret, len(stack))
        return ret


def binary_search(stack, target):
    index = -1
    begin = 0
    end = len(stack)-1
    while index == -1:
        mid = (end + begin) // 2
        if target == stack[mid]:
            index = mid
        elif target > stack[mid]:
            if mid == len(stack)-1 or target < stack[mid+1]:
                index = mid + 1
            begin = mid + 1
        else:
            if mid == 0 or target > stack[mid-1]:
                index = mid
            end = mid - 1
    return index

# print(Solution1().lengthOfLIS([11, 12, 13, 14, 15, 6, 7, 8, 101, 18]))
print(binary_search([11, 12, 13, 14, 15, 101], 16))