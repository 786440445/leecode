'''
45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。
'''


class Solution:
    def jump(self, nums) -> int:
        l = len(nums)

        if l < 2:
            return 0
        else:
            current_max_index = nums[0]
            pre_max_index = nums[0]
            jump_min = 1
            for i in range(1, l):
                if i > current_max_index:
                    jump_min += 1
                    current_max_index = pre_max_index
                if pre_max_index < nums[i] + i:
                    pre_max_index = nums[i] + i
            return jump_min


ret = Solution().jump([2, 3, 1, 1, 4])
print(ret)