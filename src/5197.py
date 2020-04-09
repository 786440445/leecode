'''
最小绝对差
给你个整数数组 arr，其中每个元素都 不相同。

请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。



示例 1：

输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]
示例 2：

输入：arr = [1,3,6,10,15]
输出：[[1,3]]
示例 3：

输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]


提示：

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6
'''

class Solution:
    def minimumAbsDifference(self, arr):
        arr = sorted(arr)
        tmp = 1000000
        ma = dict()
        for i in range(len(arr)-1):
            a = arr[i+1] - arr[i]
            if a <= tmp:
                tmp = a
                if ma.get(a) is None:
                    value = [i]
                    ma.setdefault(a, value)
                else:
                    old = ma.get(a)
                    old.append(i)
                    ma[a] = old
        keys = ma.keys()
        sort_keys = sorted(keys)
        value_list = ma.get(sort_keys[0])
        res = []
        for i in value_list:
            res.append([arr[i], arr[i+1]])
        return res



arr = [3,8,-10,23,19,-4,-14,27]
solution = Solution()
res = solution.minimumAbsDifference(arr)
print('res :', res)