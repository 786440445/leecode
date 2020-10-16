#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 111111
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/10/12 11:00 AM
@Desc   ：
=================================================='''
#
# #coding=utf-8
# import sys
# #str = input()
# #print(str)
#
# def merge(lis1, lis2):
#     p = lis1
#     q = lis2
#     while p!= None or q != None:
#         if p.val < q.val:
#             p.next = q
#             q = q.next
#         else:
#             q.next = p
#             p = p.next
#
#     if not q:
#         return lis2
#     if not p:
#         return lis1
#
# from utils import *
#
# a = create_list_node([1, 3, 5])
# b = create_list_node([2, 6, 10])
# print(a)
# print(b)
# res = merge(a, b)
# print_list(res)


# import random
#
# def func():
#     dict = {1: 2, 2: 4, 3: 4}
#     dic = {}
#     for k, v in dict.items():
#         dic[]
#
#     rand = random.random(1, 10)
#     sum = 0
#     for k, v in dict.items():
#         sum += v
#         if rand <= sum:
#             res = k
#             break
#     print(res)
#
# func()

def func(lis):
    l = len(lis)
    dp = [[0] * l for _ in range(l)]
    left = 0
    right = 0
    max_v = float('-inf')
    for i in range(l):
        for j in range(i, l):
            if i == j:
                dp[i][j] = lis[i]
            else:
                dp[i][j] = dp[i][j-1] + lis[j]

            if dp[i][j] > max_v:
                left = i
                right = j
                max_v = dp[i][j]
    print(lis[left:right+1])


func([4,-3,1,2,3,-5,6,7,-8,-9,1])