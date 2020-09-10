'''
232. 用栈实现队列
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
 

示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
'''


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_a = []
        self.stack_b = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_a.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_b:
            for _ in range(len(self.stack_a)):
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack_b:
            for _ in range(len(self.stack_a)):
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_b and not self.stack_a


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.peek())
print(obj.empty())