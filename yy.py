#
# 根据给定的参数n（10>n>=0），得到0-n之间的整数组成的不含有重复数字的偶数的个数（0为偶数）
# @param n int整型 10>n>=0
# @return int整型
#
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> yy
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/8/31 7:31 PM
@Desc   ：
=================================================='''

#
# 根据给定的参数n（10>n>=0），得到0-n之间的整数组成的不含有重复数字的偶数的个数（0为偶数）
# @param n int整型 10>n>=0
# @return int整型
#
class Solution:
    def get_even_num(self, n):
        # write code here
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 2
        dict = {1: 1, 2: 1}
        for i in range(2, n+1):
            if i & 1 == 0: #
                sum = 0
                for k, v in dict.items():
                    sum += (k+1)*v
                dp[i] = dp[i-1] + 1 + sum

                max_key = max(dict.keys())
                max_value = 0
                for k, v in dict.items():
                    if k == 1:
                        dict[k] = v + 1
                    else:
                        if k == max_key:
                            max_value = v
                        dict[k] = v + v * k
                dict[max_key+1] = max_value * (max_key + 1)
            else:
                sum = 0
                for k, v in dict.items():
                    sum += k * v
                dp[i] = dp[i - 1] + sum

                max_key = max(dict.keys())
                max_value = 0
                for k, v in dict.items():
                    if k == 1:
                        pass
                    else:
                        if k == max_key:
                            max_value = v
                        dict[k] = v + v * (k-1)
                dict[max_key + 1] = max_value * (max_key)

        return dp


if __name__ == '__main__':
    n = int(input())
    if n < 0 or n >= 10:
        print(0)
    elif n == 0:
        print(1)
    else:
        ret = Solution().get_even_num(n)
        print(ret[n])