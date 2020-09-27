#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/15 7:52 PM
@Desc   ：
=================================================='''
def deal1(item1, item2):
    # 计算交集
    a1, b1, c1, d1 = item1[0], item1[1], item1[2], item1[3]
    a2, b2, c2, d2 = item2[0], item2[1], item2[2], item2[3]
    if a2 > c1 or b2 > d1 or a1 > c2 or b1 > d2:
        return 0
    w = min(c1, c2) - max(a1, a2)
    h = min(d1, d2) - max(b1, b2)
    return abs(w)*abs(h)


def deal2(item1, item2):
    # 计算和积
    a1, b1, c1, d1 = item1[0], item1[1], item1[2], item1[3]
    a2, b2, c2, d2 = item2[0], item2[1], item2[2], item2[3]
    return (b1-a1)*(d1-c1) + (b2-a2)*(d2-c2)


def NMS(boxxes, th):
    s = set()
    l = len(boxxes)
    for i in range(l):
        for j in range(i+1, l):
            item1 = boxxes[i]
            item2 = boxxes[j]
            aaa = deal1(item1, item2) / deal2(item1, item2)
            if aaa > th:
                if item1[4] > item2[4]:
                    s.add(j)
                else:
                    s.add(i)

    s = list(s)
    boxxes = [item for index, item in enumerate(boxxes) if index not in s]
    boxxes = sorted(boxxes, key=lambda x: x[4], reverse=True)
    for item in boxxes:
        ret = ''
        for s in item:
            ret += str(s) + ' '
        print(ret[:-1])


inp = list(map(float, input().split()))
n = int(inp[0])
th = inp[1]
mat = []
for _ in range(n):
    inp = list(map(float, input().split()))
    mat.append(inp)
NMS(mat, th)
