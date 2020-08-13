#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> jingdong
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/6 7:51 PM
@Desc   ：
=================================================='''
def func():
    N = int(input())
    list1 = input()
    list2 = input()
    if N > 1000 or N < 0:
        return 0
    list1 = list1.split(' ')
    list2 = list2.split(' ')
    max_len = 0
    for i in range(N):
        start_index = i
        end_index = 0
        l = 0
        while True:
            if start_index >= N:
                break
            if end_index >= N:
                break
            if list1[start_index] == list2[end_index]:
                end_index += 1
                start_index += 1
                l += 1
            else:
                end_index += 1
        if l > max_len:
            max_len = l
    ret = round(max_len/N, 2)
    if ret > 0.50:
        return str(ret) + ' ' + 'No'
    else:
        return str(ret) + ' ' + 'Yes'

print(func())