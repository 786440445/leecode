#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 14
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/9 12:41 PM
@Desc   ：
=================================================='''
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        l = min([len(s) for s in strs])
        k = 0
        ret = ''
        while k <= l:
            s0 = strs[0]
            flag = True
            for s in strs:
                if s0[:k] != s[:k]:
                    flag = False
            if flag:
                ret = s0[:k]
            k += 1
        return ret






ret = Solution().longestCommonPrefix(["cbasda", "cbasdac"])
print(ret)


