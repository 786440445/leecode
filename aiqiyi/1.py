#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/23 2:58 PM
@Desc   ：
=================================================='''
def Solution():
    strs1 = input()
    strs2 = input().split(' ')
    l1 = len(strs1)
    l2 = len(strs2)
    i = 0
    ret = ''
    while i < l1:
        j = i+1
        c = strs1[i]
        k = cunzai(c, strs2)
        if k:
            while j < i+2*len(k):
                item = strs1[i:j]
                item = item.replace(' ', '')
                if item == k:
                    if strs1[i-1] != ' ':
                        ret += ' ' + item
                    else:
                        ret += item
                    if j + 1 < l1 and strs1[j+1] != ' ':
                        ret += ' '
                    break
                j += 1
        else:
            ret += c
        i += 1
    return ret.strip()

def cunzai(c, strs):
    for item in strs:
        if c in item:
            return item
    return None

print(Solution())