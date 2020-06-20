class Solution:
    def sumNums(self, n):
        res = n
        flag = res == 1 & (res += self.sumNums(n-1))
        return res

solu = Solution()
res = solu.sumNums(10)
print(res)