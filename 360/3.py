#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 3
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/24 11:04 AM
@Desc   ：
=================================================='''


strs = input()
ret = ''
for index, c in enumerate(strs):
    if index == 0:
        ret += c.upper()
    else:
        if c == 'n':
            ret += '\n' + 'N'
        else:
            ret += c
print(ret)
