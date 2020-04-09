''' 交换字符串中的元素
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。

你可以 任意多次交换 在 pairs 中任意一对索引处的字符。

返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。



示例 1:

输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"
示例 2：

输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"
示例 3：

输入：s = "cba", pairs = [[0,1],[1,2]]
输出："abc"
解释：
交换 s[0] 和 s[1], s = "bca"
交换 s[1] 和 s[2], s = "bac"
交换 s[0] 和 s[1], s = "abc"


提示：

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s 中只含有小写英文字母
'''
def add_pairs(res, k, v, paris):
    if k in pairs:
        k1 = pairs[0]
        v1 = pairs[1]
        if k == k1:
            res.append([])
    return

def change_pairs(pairs):
    for item in enumerate(pairs):
        paris = unite(item[0], item[1])

def get_index(value, list):
    res = []
    for i, v in enumerate(list):
        if v == value:
            res.append(i)
    return res

def get_weight(s):
    w = []
    for i in range(len(s)):
        score = 0
        for j in range(i, len(s)):
            if s[i]>s[j]:
                score += 1
        w.append(score)
    return w

def change(s, a, b):
    res = []
    for i in range(len(s)):
        if i == a:
            res.append(s[b])
        elif i == b:
            res.append(s[a])
        else:
            res.append(s[i])
    return ''.join(res)

def change_max_score(s, pairs):
    for i in pairs:
        w = get_weight(s)
        old_score = sum(w)
        max_value = max(w)
        max_index_list = get_index(max_value, w)
        for max_index in max_index_list:
            if max_index in i:
                s1 = change(s, int(i[0]), int(i[1]))
                score = sum(get_weight(s1))
                if score < old_score:
                    s = s1
    return s

class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        pairs = change_pairs(pairs)
        s = change_max_score(s, pairs)
        return s

solution = Solution()
s = "dcab"
pairs = [[0,3],[1,2],[0,2]]
print(solution.smallestStringWithSwaps(s, pairs))