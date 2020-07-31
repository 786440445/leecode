# 快速排序
class Solution():
    def quicksort(self, nums, k):
        n = len(nums)
        return self.sort(nums, 0, n-1, k)

    def sort(self, nums, left, right, k):
        if left >= right:
            return -1
        pivot = left
        i = left
        j = right
        while(i < j):
            while i < j and nums[j] > nums[pivot]:
                j -= 1
            while i < j and nums[i] <= nums[pivot]:
                i += 1
            nums[i],  nums[j] = nums[j], nums[i]

        if j == k:
            return nums[j]
        nums[pivot], nums[j] = nums[j], nums[pivot]
        self.sort(nums, left, j-1, k)
        self.sort(nums, j+1, right, k)


cli = Solution()
ret = cli.quicksort([6, 3, 10, 5, 4, 9, 7, 2], 2)
print(ret)