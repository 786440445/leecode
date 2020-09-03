#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/22 6:55 PM
@Desc   ：
=================================================='''


def solution():
    n = int(input())
    count = 0
    while n > 0:
        n -= 1
        s = input()
        if len(s) > 10 or len(s) == 0:
            continue
        if judge(s):
            count += 1
    print(count)


def judge(s):
    for c in s:
        if 'A' <= c <= 'Z' or 'a' <=c <= 'z':
            pass
        else:
            return False
    return True

solution()