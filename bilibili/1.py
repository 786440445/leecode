#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/13 7:41 PM
@Desc   ：
=================================================='''
def func():
    str1 = input().strip()
    str2 = input().strip()
    if len(str1) >= 1000:
        return
    if len(str2) >= 1000:
        return
    if str1 == str2:
        return 1
    if len(str1) != len(str2):
        return 0
    str_dict1 = {}
    str_dict2 = {}

    for a, b in zip(str1, str2):
        str_dict1[a] = str_dict1.get(a, 0) + 1
        str_dict2[b] = str_dict2.get(b, 0) + 1
    if str_dict1 == str_dict2:
        return 1
    else:
        return 0
print(func())