#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：leecode -> 622
@IDE    ：PyCharm
@Author ：chengli
@Date   ：2020/6/6 6:03 PM
@Desc   ：
=================================================='''


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k
        self.queue_list = [0] * k
        self.count = 0
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count < self.k:
            self.queue_list[self.tail] = value
            self.tail = (self.tail + 1) % self.k
            self.count += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count > 0:
            self.queue_list[self.head] = 0
            self.head = (self.head + 1) % self.k
            self.count -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count > 0:
            return self.queue_list[self.head]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.count > 0:
            return self.queue_list[self.tail]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.k




# Your MyCircularQueue object will be instantiated and called as such:
circularQueue = MyCircularQueue(3)
circularQueue.enQueue(1)

circularQueue.enQueue(2)

circularQueue.enQueue(3)

circularQueue.enQueue(4)

circularQueue.Rear()

circularQueue.isFull()

circularQueue.deQueue()

circularQueue.enQueue(4)

circularQueue.Rear()