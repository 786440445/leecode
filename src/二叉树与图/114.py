'''
114. 二叉树展开为链表
给定一个二叉树，原地将它展开为一个单链表。



例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from queue import Queue
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def func(root):
            if not root:
                return None, None
            if not root.left and not root.right:
                return root, root
            last = None
            left = root.left
            right = root.right

            if left:
                left_f, left_l = func(left)
                root.left = None
                root.right = left_f
                last = left_l
            if right:
                right_f, right_l = func(right)
                if last:
                    last.right = right_f
                last = right_l
            return root, last
        left, right_last = func(root)
        return left

from utils import create_tree
root = create_tree([1,2,3,4,5,6])

a = Solution().flatten(root)
print(a)