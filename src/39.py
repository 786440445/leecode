


class Solution:
    def combinationSum2(self, candidates, target: int):
        def calc(candidates, begin, end, ret, path, target):
            if target == 0:
                ret.append(path)
                return
            if target < 0:
                return

            for index in range(begin, size):
                calc(candidates, index, end, ret, path + [candidates[index]], target - candidates[index])


        size = len(candidates)
        if size == 0:
            return []
        paths = []
        ret = []
        calc(candidates, 0, size, ret, paths, target)
        return ret


Solution().combinationSum2([2,3,5], target = 8)
