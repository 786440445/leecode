#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/10/16 9:03 AM
@Desc   ：
=================================================='''

class Solution:
    def __init__(self):
        self.res = ''
        self.count = 0

    def func(self, op, v=None):
        if op == 1:
            if self.count == 0:
                self.res = str(v)
            else:
                self.res = str(v) + ' ' + self.res
            self.count += 1
        elif op == 2:
            if self.count == 0:
                self.res += str(v)
            else:
                self.res = self.res + ' ' + str(v)
            self.count += 1
        elif op == 3:
            if self.count == 1:
                self.res = ''
            else:
                self.res = self.res[2:]
            self.count -= 1
        elif op == 4:
            if self.count == 1:
                self.res = ''
            else:
                self.res = self.res[:-2]
            self.count -= 1
        else:
            pass

n = int(input())
cli = Solution()
while n > 0:
    inp = list(map(int, input().split(' ')))
    if len(inp) == 2:
        op = inp[0]
        v = inp[1]
        cli.func(op, v)
    else:
        op = inp[0]
        cli.func(op)
    n -= 1
print(cli.res)