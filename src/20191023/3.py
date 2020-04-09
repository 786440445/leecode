'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        if l & 1 == 1:
            print(l)
            return nums[int(l // 2)] + nums[int((l + 1) / 2)]
        else:
            print('l:', l)
            print(nums)
            return nums[int(l/2)]

print(Solution().findMedianSortedArrays([1, 2, 3], [5]))
# print(Solution().findMedianSortedArrays('pwwkew'))
# print(Solution().findMedianSortedArrays('bbbbbb'))