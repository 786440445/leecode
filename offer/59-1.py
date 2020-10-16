'''
剑指 Offer 59 - I. 滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


提示：

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/
'''

from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        d = deque()
        for i in range(k):  # 未形成窗口
            while d and d[-1] < nums[i]:
                d.pop()
            d.append(nums[i])
        res = [d[0]]

        for i in range(k, len(nums)):  # 形成窗口后
            if d[0] == nums[i - k]:
                d.popleft()
            while d and d[-1] < nums[i]:
                d.pop()
            d.append(nums[i])
            res.append(d[0])
        return res


ret = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k=3)
print(ret)