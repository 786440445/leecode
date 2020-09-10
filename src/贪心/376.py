class Solution:
    def __init__(self):
        self.BEGIN = 0
        self.UP = 1
        self.DOWN = 2

    def wiggleMaxLength(self, nums) -> int:
        if len(nums) < 2:
            return len(nums)
        state = self.BEGIN

        count = 0
        for index, item in enumerate(nums[1:]):
            if state == self.BEGIN:
                if item > nums[index]:
                    state = self.UP
                    count += 1
                elif item < nums[index]:
                    state = self.DOWN
                    count += 1
                continue

            if state == self.UP:
                if item < nums[index]:
                    state = self.DOWN
                    count += 1
                continue
            if state == self.DOWN:
                if item > nums[index]:
                    state = self.UP
                    count += 1
                continue
        return count + 1

print(Solution().wiggleMaxLength([1,7,4,9,2,5]))