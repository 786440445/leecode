#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/25 3:56 PM
@Desc   ：
=================================================='''

class Solution:
    def leastWorkTime(self , tasks , n ):
        # write code here
        d = {}
        for c in tasks:
            d[c] = d.get(c, 0) + 1

