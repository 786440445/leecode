#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 1
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/21 7:57 PM
@Desc   ：
=================================================='''
import numpy as np
def func(userids, itemids):
    ret = ''
    for uid, id1 in userids:
        scores = []
        for index, (iid, id2) in enumerate(itemids):
            a = cosine(np.array(id1), np.array(id2))
            scores.append((index, iid, a))
        scores = sorted(scores, key=lambda x: x[2], reverse=True)
        scores = scores[:10]
        out = uid + ':'
        for socre in scores:
            out += socre[1] + ','
        ret += out[:-1] + '\n'
    print(ret[:-1])


def cosine(id1, id2):
    aa = np.dot(id1, id2.T)
    id1_norm = np.sum(id1 ** 2) ** 0.5
    id2_norm = np.sum(id2 ** 2) ** 0.5
    bb = np.dot(id1_norm, id2_norm.T)
    return np.divide(aa, bb)
    # return np.multiply(id1, id2) / (np.did1 ** id1 + id2 ** id2)


k = int(input())
userid = []
itemid = []
while k > 0:
    inp = input().split('#')
    if inp[0][0] == 'u':
        userid.append((inp[0], list(map(float, inp[1].split(',')))))
    else:
        itemid.append((inp[0], list(map(float, inp[1].split(',')))))
    k -= 1
func(userid, itemid)
