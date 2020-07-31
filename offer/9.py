'''
剑指 Offer 09. 用两个栈实现队列
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )



示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
'''
class CQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int):
        self.stack1.append(value)

    def deleteHead(self):
        if self.stack2:
            return self.stack2.pop()
        if self.stack1 == []:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


op_list = ["CQueue","deleteHead","appendTail","deleteHead","deleteHead","deleteHead","deleteHead","appendTail","deleteHead","appendTail","appendTail","deleteHead","deleteHead","deleteHead","appendTail","deleteHead","deleteHead","deleteHead","deleteHead","appendTail","appendTail","appendTail","appendTail","deleteHead","deleteHead","appendTail","appendTail","deleteHead","deleteHead","deleteHead","appendTail","appendTail","deleteHead","appendTail","deleteHead","appendTail","appendTail","appendTail","deleteHead","deleteHead","appendTail","appendTail","deleteHead","deleteHead","deleteHead","deleteHead","appendTail","appendTail","deleteHead","deleteHead","appendTail","deleteHead","appendTail","appendTail","appendTail","appendTail","deleteHead","appendTail","deleteHead","deleteHead","appendTail","appendTail","appendTail","deleteHead","deleteHead","appendTail","appendTail","appendTail","deleteHead","deleteHead","deleteHead","deleteHead","appendTail","appendTail","deleteHead","deleteHead","appendTail","deleteHead","appendTail","appendTail","deleteHead","deleteHead","appendTail","deleteHead","appendTail","appendTail","appendTail","deleteHead","appendTail","appendTail","appendTail","appendTail","deleteHead","deleteHead","deleteHead","appendTail","deleteHead","appendTail","deleteHead","appendTail","appendTail"]
value_list = [[],[],[97],[],[],[],[],[15],[],[1],[43],[],[],[],[18],[],[],[],[],[36],[69],[21],[91],[],[],[22],[40],[],[]]

cli = CQueue()
result = []
for op, value in zip(op_list, value_list):
    if op != 'CQueue':
        if op == 'deleteHead':
            item = cli.deleteHead()
            result.append(item)
        else:
            item = cli.appendTail(value[0])
            result.append(item)

print(result)