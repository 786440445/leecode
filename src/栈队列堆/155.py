'''
155. 最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.min_stack = []
        self.stack = []

    def push(self, x: int):
        if not self.stack:
            self.min = x
        else:
            if x < self.min:
                self.min = x
        self.min_stack.append(self.min)
        self.stack.append(x)

    def pop(self):
        self.min_stack.pop()
        if self.min_stack:
            self.min = self.min_stack[-1]
        else:
            self.min = None
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None

# ["MinStack","push","push","getMin","getMin","push","getMin","getMin","top","getMin","pop","push","push","getMin","push","pop","top","getMin","pop"]
# [[],[-10],[14],[],[],[-20],[],[],[],[],[],[10],[-7],[],[-7],[],[],[],[]]
# Your MinStack object will be instantiated and called as such:
obj = MinStack() # [-10, 14]
obj.push(-10)
obj.push(14)
print(obj.getMin())
print(obj.getMin())
obj.push(-20)  # [-10, 14, -20]
print(obj.getMin())
print(obj.getMin())
print(obj.top())
print(obj.getMin())
print(obj.pop()) # [-10, 14]
obj.push(10)  # [-10, 14, 10]
obj.push(-7)
print(obj.getMin())
obj.push(-7)
print(obj.pop())
print(obj.top())
print(obj.getMin())
print(obj.pop())
