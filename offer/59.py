from queue import Queue
from collections import deque

class MaxQueue:
    def __init__(self):
        self.q = Queue()
        self.max_q = deque()

    def max_value(self) -> int:
        if self.q.empty():
            return -1
        else:
            return self.max_q[-1]

    def push_back(self, value: int) -> None:
        while self.max_q and self.max_q[-1] < value:
            self.max_q.pop()
        self.max_q.append(value)
        self.q.put(value)

    def pop_front(self) -> int:
        if not self.q.empty():
            ans = self.max_q.pop()
            if ans == self.max_q[0]:
                self.max_q.popleft()
            return ans
        else:
            return -1


q = MaxQueue()
q.push_back(1)
q.push_back(3)
q.push_back(4)
q.push_back(2)

print(q.max_value())
print(q.pop_front())
print(q.max_value())
print(q.pop_front())
print(q.max_value())
print(q.pop_front())
print(q.max_value())
print(q.pop_front())
print(q.max_value())
print(q.max_value())
