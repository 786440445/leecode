#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/23 7:59 PM
@Desc   ：
=================================================='''
def Solution():
    strs = input()
    l = len(strs)
    if l > 200 or l < 0:
        return 0
    count = 0
    ret = []
    for index, item in enumerate(strs):
        if not ret:
            ret.append(item)
        else:
            if (item == ')' and ret[-1] == '(') or (item == ']' and ret[-1] == '['):
                ret.pop()
            elif item == ']':
                count += 1
            else:
                ret.append(item)
    lis = []
    count2 = 0
    for k in ret:
        if not lis:
            lis.append(k)
        else:
            if (k == ')' and lis[-1] == '(') or (k == ']' and lis[-1] == '['):
                lis.pop()
            elif k == ')':
                count2 += 1
            else:
                lis.append(k)
    print(count)
    print(count2)
    print(len(lis))
Solution()
