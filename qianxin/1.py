#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/25 3:54 PM
@Desc   ：
=================================================='''


def func():
    n = int(input())

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        for k in range(i):
            dp[i] += dp[k]
        dp[i] += 1
    print(dp[n])


if __name__ == '__main__':
    func()