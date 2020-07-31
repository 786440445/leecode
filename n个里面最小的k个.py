class Solution():
    def min_k_in_n(self, list1, k):
        for i in range(len(list1)):
            for j in range(i+1, len(list1)):
                if list1[i] < list1[j]:
                    self.swap(i, j, list1)
        return list1[-k:]

    def swap(self, i, j, list1):
        list1[i] = list1[i] + list1[j]
        list1[j] = list1[i] - list1[j]
        list1[i] = list1[i] - list1[j]


cli = Solution()
ret = cli.min_k_in_n([5, 2, 1, 3, 4], 3)
print(ret)
