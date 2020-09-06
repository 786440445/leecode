#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/6 8:12 PM
@Desc   ：
=================================================='''
def func(l, d):
    if l <= 0 or d <= 0:
        return
    if l <= d:
        print('%.4f' % 0)

    count = 0
    while l > d:
        p = d/l
        count += 1
        l = d



if __name__ == '__main__':
    an = list(map(int, input().split(' ')))
    l = an[0]
    d = an[1]
    ret = func(l, d)
    print(ret)
