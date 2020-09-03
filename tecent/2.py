#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/23 8:27 PM
@Desc   ：
=================================================='''
import sys

def Solution():
    n = int(sys.stdin.readline().strip())
    # n = int(input())
    if n < 0 or n > 1000:
        return
    while n > 0:
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        inp = list(map(int, line.split()))
        # inp = [int(x) for x in input().split(' ')]
        a = inp[0]
        b = inp[1]
        c = inp[2]
        d = inp[3]
        if a < 1 or a > 100:
            continue
        if b < 1 or b > 100:
            continue
        if c < -100 or c > 100:
            continue
        if d < -100 or d > 100:
            continue
        if c > d:
            continue
        sum = a/3*(d**3-c**3) + 1/2*(d**2-c**2) + b*(d-c)
        print('%.6f' % sum)
        print(round(sum, 6))

        n -= 1

if __name__ == '__main__':
    Solution()