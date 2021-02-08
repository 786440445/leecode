#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 941
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/11/3 9:34 PM
@Desc   ：
=================================================='''

class Solution:
    def validMountainArray(self, A) -> bool:
        left = 0
        l = len(A)
        right = l-1
        while left + 1 < l and A[left] < A[left + 1]:
            left += 1
        while right > 0 and A[right] < A[right - 1]:
            right -= 1
        return left > 0 and right < l - 1 and left == right


print(Solution().validMountainArray([3, 5, 5]))