#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 3
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/6 10:21 AM
@Desc   ：
=================================================='''

class Solution():
    def func(self, n, an):
        if len(an) != n:
            return
        ret1 = []
        ret2 = []
        for item in an:
            if item == 1:
                ret1.append(1)
            else:
                ret2.append(item)
        ret2.sort(reverse=True)
        while ret1 and ret2:
            top = ret2.pop()
            item1 = ret1.pop()
            item2 = ret1.pop()
            for k in len(ret1):
                if item[]
            if top == item1 + item2 + 1:
                ret1.insert(, top)
            else:
                return 'NO'

        if not ret2:
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':
    while True:
        n = int(input())
        an = list(map(int, input().split(' ')))
        ret = Solution().func(n, an)
        print(ret)