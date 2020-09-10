'''
295. 数据流的中位数
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
'''

import heapq
from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        a = heappushpop(self.maxheap, -num)  # 将值插入到堆中同时弹出堆中的最小值。
        heappush(self.minheap, -a)
        if len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, -heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        return (self.minheap[0] - self.maxheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())