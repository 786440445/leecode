'''
剑指 Offer 26. 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
'''
from utils import *
import queue

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A == None or B == None: return False
        return self.judge(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def judge(self, A, B):
        if A == None or B == None:
            return bool(B == None)
        else:
            return (A.val == B.val) and self.judge(A.left, B.left) and self.judge(A.right, B.right)


A = create_tree([[3,5,0,3,4]])
B = create_tree([1,-4,2,-1,3,-3,-4,0,-3,-1])
ret = Solution().isSubStructure(A, B)
print(ret)