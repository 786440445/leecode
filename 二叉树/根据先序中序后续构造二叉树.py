# 根据先序序列，中序序列构造二叉树

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


root = create_tree_by_preorder([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])
print_tree(root)