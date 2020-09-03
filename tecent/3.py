#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 3
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/23 8:27 PM
@Desc   ：
=================================================='''


class Solution():
    def __init__(self):
        self.n = int(input())
        if self.n < 1 or self.n > 10**9:
            return
        self.shuzu = [0 for _ in range(self.n+1)]
        self.shuzu[0] = 1

        sum = 1
        for i in range(1, self.n+1):
            sum = sum*i
            self.shuzu[i] = sum

    def func(self):
        ret = 0
        for i in range(1, self.n+1):
            ret += self.calc(i)

        return int(ret % (10**9+7))

    def calc(self, k): #计算k*Cnk
        return k * self.shuzu[self.n]/(self.shuzu[self.n-k] * self.shuzu[k])


if __name__ == '__main__':
    sun = Solution()
    ret = sun.func()
    print(ret)