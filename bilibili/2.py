#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/13 7:49 PM
@Desc   ：
=================================================='''
import math
def func():
    n = int(input())
    sushu = [0] * (n+1)
    for i in range(2, n+1):
        if is_sh(i):
            sushu[i] = 1
    count = 0
    for i in range(2, n+1):
        sum = 0
        j = i
        if sushu[j] == 1:
            while(1):
                if j > n:
                    break
                if sushu[j] == 1:
                    sum += j
                    if sum == n:
                        count += 1
                        break
                j += 1
                if sum > n:
                    break

    print(count)


def is_sh(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# print(is_sh(8))
# print(is_sh(7))
# print(is_sh(6))
# print(is_sh(5))
# print(is_sh(4))
# print(is_sh(3))
# print(is_sh(2))

func()