''''
225. 用队列实现栈
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
'''

from queue import Queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.qa = Queue()
        self.qb = Queue()
        self.top_v = None


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.qa.put(x)
        self.top_v = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        size = self.qa.qsize()
        for _ in range(size-1):
            item = self.qa.get()
            self.qb.put(item)
        ret = self.qa.get()

        while not self.qb.empty():
            self.top_v = self.qb.get()
            self.qa.put(self.top_v)
        return ret

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.empty():
            return self.top_v
        else:
            return 0

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.qa.empty()

stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
stack.push(6)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()