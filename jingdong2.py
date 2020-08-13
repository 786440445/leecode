

import math

class Solution():
    def func(self):
        inpu = input()
        n = int(inpu.split(' ')[0])
        m = int(inpu.split(' ')[1])
        if n < 1 or n > 1000000:
            return 0
        if m < 1 or m > 1000000:
            return 0
        if n >= m:
            return 0
        count = 0
        for i in range(n, m+1):
            if self.huiwen_and_sushu(i):
                count += 1
        return count

    def huiwen_and_sushu(self, n):
        n = str(n)
        l = len(n)
        for index in range(l):
            if index == 0:
                a = n[1:]
            elif index == len(n)-1:
                a = n[:-1]
            else:
                a = n[:index] + n[index+1:]
            int_a = int(a)
            if self.ishuiwen(a) and self.sushu(int_a):
                return True
        return False

    def ishuiwen(self, n):
        return n == n[::-1]

    def sushu(self, n):
        for i in range(2, math.ceil(math.sqrt(n))):
            if n % i == 0:
                return False
        return True


print(Solution().func())