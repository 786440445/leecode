'''
根据先序序列，中序序列构造二叉树
递归方法解决
'''
from utils import TreeNode, print_tree
def create_tree_by_preorder(pre_list, mid_list):
    if not pre_list:
        return None
    if not mid_list:
        return None
    tree_val = pre_list[0]
    root = TreeNode(tree_val)
    left_index = mid_list.index(tree_val)
    root.left = create_tree_by_preorder(pre_list[1:left_index+1], mid_list[:left_index])
    root.right = create_tree_by_preorder(pre_list[left_index+1:], mid_list[left_index+1:])
    return root

'''
根据先序序列，中序序列构造二叉树
队列解决
'''
import queue
def create_tree_by_preorder1(pre_list, mid_list):
    q = queue.Queue()
    root = pre_list[0]
    q.put(root)
    while not q.empty():
        root = q.get()
        left_index = mid_list.index(root.val)
        pre_list = pre_list[1:left_index+1]
        mid_list = mid_list[left_index:]

'''
根据后序序列，中序序列构造二叉树
递归方法解决
'''
from utils import TreeNode, print_tree


def buildTree(postorder, inorder):
    if not postorder or not inorder:
        return None
    tree_val = postorder[-1]
    root = TreeNode(tree_val)
    left_index = inorder.index(tree_val)
    root.left = buildTree(postorder[:left_index], inorder[:left_index])
    root.right = buildTree(postorder[left_index:-1], inorder[left_index+1:])
    return root


root = buildTree([4, 5, 2, 6, 7, 3, 1], [4, 2, 5, 1, 6, 3, 7])
print_tree(root)