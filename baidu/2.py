#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 2
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/9/3 8:51 PM
@Desc   ：
=================================================='''

def func():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split(' '))))

    v = n * n
    cost = [[float('inf')]*v for _ in range(v)]
    for i in range(n):
        for j in range(n-1):
            s = 3*i + j
            e = 3*i + j+1
            cost[s][s] = 0
            cost[s][e] = abs(matrix[i][j+1] - matrix[i][j])
    print(cost)


func()
#
#
# def dijkstra(s):
#     distance[s] = 0
#     while True:
#         v = -1
#         for u in range(V):
#             if not used[u] and (v == -1 or distance[u] < distance[v]):
#                 v = u
#
#         if v == -1:
#             break
#
#         used[v] =True
#         for u in range(V):
#             distance[u] = min(distance[u], distance[v] + cost[v][u])
#
# func()
#
# #
# # V = 7
# # used = [False for _ in range(V)]
# # distance = [float('inf') for _ in range(V)]
# # cost = [[float('inf') for _ in range(V)] for _ in range(V)]
#
#
# def dijkstra(s):
#     distance[s] = 0
#     while True:
#         v = -1
#         for u in range(V):
#             if not used[u] and (v == -1 or distance[u] < distance[v]):
#                 v = u
#         if v == -1:
#             break
#         used[v] =True
#         for u in range(V):
#             distance[u] = min(distance[u], distance[v] + cost[v][u])
#
#
# if __name__ == '__main__':
#     for _ in range(12):
#         v, u, w = list(map(int, input().split()))
#         cost[v][u] = w
#     s = int(input('请输入一个起始点：'))
#     dijkstra(s)
#     print(distance)
