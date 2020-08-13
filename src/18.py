'''
四个数之和
'''

class Solution:
    def fourSum(self, nums, target):
        l = len(nums)
        ret = []
        if l < 4:
            return ret
        nums.sort()
        for k in range(l):
            for j in range(k+1, l):
                right = l - 1
                left = j + 1
                while(left < right):
                    if (nums[k] + nums[j] + nums[left] + nums[right]) == target:
                        value = [nums[k], nums[j], nums[left], nums[right]]
                        if value not in ret:
                            ret.append(value)
                        while(left < right and nums[left] == nums[left + 1]):
                            left = left + 1
                        while(left < right and nums[right] == nums[right - 1]):
                            right = right - 1
                        left += 1
                        right -= 1
                    elif nums[k] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        return ret


ret = Solution().fourSum([1,-2,-5,-4,-3,3,3,5], -11)
print(ret)
