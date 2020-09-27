'''
617. 合并二叉树
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dps(root, node1, node2):
            value = 0
            if not node1 and not node2:
                return

            if node1:
                value += node1.val
            if node2:
                value += node2.val

            root.val = value
            if node1:
                left1 = node1.left
                right1 = node1.right
            else:
                left1 = None
                right1 = None

            if node2:
                left2 = node2.left
                right2 = node2.right
            else:
                left2 = None
                right2 = None

            root.left = dps(TreeNode(None), left1, left2)
            root.right = dps(TreeNode(None), right1, right2)

            return root

        root = TreeNode(None)
        root = dps(root, t1, t2)
        return root

class Solution2:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2:
            return t1 or t2
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1



from utils import create_tree, print_tree
a = create_tree([1, 3, 2, 5])
b = create_tree([2, 1, 3, 4])
root = Solution().mergeTrees(a, b)
print_tree(root)





