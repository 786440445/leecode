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
            l1 = len(ret1)
            l2 = len(ret2)
            if l1 == 2 and l2 == 1 and ret1[0] + ret1[1] + 1 == ret2[0]:
                ret1.pop()
                ret1.pop()
                ret2.pop()
                continue

            top = ret2.pop()
            for i in range(l1)[:-1]:
                if ret1[i] + ret1[i+1] + 1 == top:
                    ret1[i] = top
                    for k in range(i+1, l1-1):
                        ret1[k] = ret1[k+1]
                    ret1 = ret1[:-1]
                    break
            else:
                return 'NO'
        if not ret1 and not ret2:
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':
    while True:
        n = int(input())
        an = list(map(int, input().split(' ')))
        ret = Solution().func(n, an)
        print(ret)