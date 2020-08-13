#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 111
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/6 11:25 AM
@Desc   ：
=================================================='''
import math

while(True):
    inpu = input()
    m = int(inpu.split(' ')[0])
    n = int(inpu.split(' ')[1])
    ret = []
    if m < 100:
        print('No')
    elif n > 999:
        print('No')
    else:
        for i in range(m, n+1):
            j = i
            sum = 0
            x = 10
            while(j > 0):
                s = j % x
                j = j // x
                sum += int(math.pow(s, 3))
            if sum == i:
                ret.append(str(i))
        if ret:
            print(' '.join(ret))
        else:
            print('No')