'''
207. 课程表
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？



示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
'''

from queue import Queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 入度表
        intable = [0] * numCourses
        # 临接数组
        nexttable = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            intable[cur] += 1
            nexttable[pre].append(cur)

        q = Queue()
        for index, item in enumerate(intable):
            if item == 0:
                q.put(index)
        while not q.empty():
            node = q.get()
            numCourses -= 1
            for cur in nexttable[node]:
                intable[cur] -= 1
                if intable[cur] == 0:
                    q.put(cur)
        return not numCourses
