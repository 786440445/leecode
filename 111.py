#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 111
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/6 11:25 AM
@Desc   ：
=================================================='''

class Solution:
    def modifyString(self, s: str) -> str:
        s = list('0' + s + '0')
        l = len(s)
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        i = 1
        while i < l-1:
            if s[i] == '?':
                k = 0
                while k < len(alpha):
                    if alpha[k] not in [s[i - 1], s[i + 1]]:
                        s[i] = alpha[k]
                        break
                    k += 1
            i += 1
        return ''.join(s[1:-1])


ret = Solution().modifyString("?ob?b???")
print(ret)


