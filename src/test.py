#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> test
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/6/6 12:04 AM
@Desc   ：
=================================================='''


# class UndergroundSystem:
#
#     def __init__(self):
#         self.inmap = dict()
#         self.outmap = dict()
#
#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         user_time = self.inmap.get(stationName, dict())
#         user_time[id] = t
#         self.inmap[stationName] = user_time
#
#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         user_time = self.outmap.get(stationName, dict())
#         user_time[id] = t
#         self.outmap[stationName] = user_time
#
#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         in_time_dict = self.inmap.get(startStation, dict())
#         out_time_dict = self.outmap.get(endStation, dict())
#         count = 0
#         sum_time = 0
#         for id, in_time in in_time_dict.items():
#             out_time = out_time_dict.get(id)
#             sum_time += (out_time - in_time)
#             count += 1
#         return sum_time / count


class UndergroundSystem:

    def __init__(self):
        self.inmap = dict()
        self.ret_table = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.inmap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        starttime = self.inmap[id][1]
        index = (self.inmap[id][0], stationName)
        rec = self.ret_table.get(index, (0, 0))
        self.ret_table[index] = (rec[0] + t - starttime, rec[1] + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        index = (startStation, endStation)
        sum, amount = self.ret_table[index]
        return sum / amount


# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
# [45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],
#
# [45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],
#
# ["Paradise","Cambridge"],["Leyton","Waterloo"],
obj.checkIn(45,"Leyton",3)
obj.checkIn(32,"Paradise",8)
obj.checkIn(27,"Leyton",10)

obj.checkOut(45,"Waterloo",15)
obj.checkOut(27,"Waterloo",20)
obj.checkOut(32,"Cambridge",22)


param_3 = obj.getAverageTime("Paradise","Cambridge")
print(param_3)