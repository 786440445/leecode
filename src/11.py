class Solution:
    def maxArea(self, height):
        l = len(height)
        ret = 0
        left = 0
        right = l - 1
        while left < right:
            ret = max(ret, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ret


solu = Solution()
ret = solu.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(ret)