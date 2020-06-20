#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 650
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/6/11 11:39 PM
@Desc   ：
=================================================='''

import math


class Solution:
    def minSteps(self, n):
        ret = []
        k = 1
        m = n
        while 1 <= k <= math.ceil(math.sqrt(n)):
            if m % k == 0:
                ret.append(k)
                m = m / k
            else:
                if m <= k:
                    ret.append(m)
            k += 1
        print(ret)



solu = Solution()
solu.minSteps(36)

