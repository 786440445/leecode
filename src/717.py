# #!/usr/bin/env python
# # -*- coding: UTF-8 -*-
# '''=================================================
# @Project -> File   ：leecode -> 717
# @IDE    ：PyCharm
# @Author ：chengli
# @Date   ：2020/6/7 9:59 AM
# @Desc   ：
# =================================================='''
# class Solution:
#     def isOneBitCharacter(self, bits) -> bool:
#         flag = False
#         if bits == []:
#             return True and flag
#         else:
#             if bits[-2:] == [1,0] or bits[-2:] == [1,1]:
#                 return self.isOneBitCharacter(bits[:-2]) and flag
#             elif bits[-1:] == [0]:
#                 flag = True
#                 return self.isOneBitCharacter(bits[:-1]) and flag
#             else:
#                 return False and flag
#
#
# b = [1, 1, 1]
# print(b[-1:])
# print(b[-2:])
# a = Solution()
# b = a.isOneBitCharacter([1,1,1,0])
# print(b)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        i = 0
        flag = False
        while (i < len(bits)):
            if bits[i] == 1:
                i = i + 2
                if i == len(bits):
                    flag = True
            else:
                i += 1

        if bits[i - 1] == 0 and not flag:
            return True
        else:
            return False

cli = Solution()
ret = cli.isOneBitCharacter([1,1,1,0])
print(ret)