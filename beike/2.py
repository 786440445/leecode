#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/11 7:22 PM
@Desc   ：
=================================================='''

def countDivisors(num, k):
    cnt = 0
    error_cnt = 0
    sqrt = int(num ** 0.5)
    for x in range(1, sqrt +1):
        if num % x == 0:
            if x <= k:
                error_cnt += 1
            cnt += 1
    return cnt * 2 - (sqrt ** 2 == num) - error_cnt


def func():
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    if a < 0 or b < 0:
        return 0
    if a > (10**9) or b > (10**9):
        return 0
    if a == b:
        return 'inf'
    count = countDivisors(a-b, b)
    return count


if __name__ == '__main__':
    # print(countDivisors(1, 1))
    print(str(func()))
