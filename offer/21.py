'''
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。



示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。


提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000
'''


class Solution:
    def exchange(self, nums):
        l = len(nums)
        i = 0
        j = l-1
        while i < j:
            # 偶数
            if nums[i] & 1 == 1:
                i += 1
                continue
            # 奇数
            if nums[j] & 1 == 0:
                j -= 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
        return nums


ret = Solution().exchange([1, 3, 4, 2, 5, 1])
print(ret)
