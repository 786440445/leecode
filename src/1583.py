from typing import List

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        dic = {}
        for index, value in enumerate(preferences):
            v1 = min(index, value[0])
            v2 = index + value[0] - v1
            key = (v1, v2)
            values = dic.get(key, [])
            for item in value[1:]:
                v1 = min(index, item)
                v2 = index + item - v1
                values.append((v1, v2))
            dic[key] = values

        ans = 0
        l = len(pairs)
        for i in range(l):
            for j in range(i+1, l):
                pairs1 = (min(pairs[i]), sum(pairs[i])-min(pairs[i]))
                pairs2 = (min(pairs[j]), sum(pairs[j])-min(pairs[j]))
                v1 = min(pairs1[0], pairs2[0])
                v2 = pairs1[0] + pairs2[0] - v1
                pairs3 = (v1, v2)
                v1 = min(pairs1[1], pairs2[1])
                v2 = pairs1[1] + pairs2[1] - v1
                pairs4 = (v1, v2)
                v1 = dic.get(pairs1, [])
                v2 = dic.get(pairs2, [])

                if pairs3 in v1 or pairs3 in v2:
                    pass
                else:
                    ans += 2
                if pairs4 in v1 or pairs4 in v2:
                    pass
                else:
                    ans += 2

        return ans


ret = Solution().unhappyFriends(n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]])
ret1 = Solution().unhappyFriends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]])

ret2 = Solution().unhappyFriends(4, [[1,3,2], [2,3,0], [1,0,3],[1,0,2]], [[2,1],[3,0]])
print(ret)
print(ret1)
print(ret2)






