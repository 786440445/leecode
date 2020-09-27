'''
40. 组合总和 II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''

class Solution:
    def combinationSum2(self, candidates, target: int):
        def calc(candidates, begin, end, ret, path, target):
            if target == 0:
                ret.append(path)
            if target < 0:
                return

            for index in range(begin, end):
                if index > begin and candidates[index] == candidates[index-1]:
                    # 去重
                    continue
                calc(candidates, index+1, end, ret, path + [candidates[index]], target - candidates[index])

        candidates.sort()
        size = len(candidates)
        if size == 0:
            return []
        paths = []
        ret = []
        calc(candidates, 0, size, ret, paths, target)
        return ret

                                                # 0 1 2 3 4 5 6
ret = Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
print(ret)
# 1 1 2 5 6 7 10
# 1 1

