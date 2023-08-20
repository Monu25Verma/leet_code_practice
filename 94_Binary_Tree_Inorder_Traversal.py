# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from binary_tree_path import TreeNode


class Solution:
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        l = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            l.append(current_node.val)
            if current_node.right:
                traverse(current_node.right)

        if root:
            traverse(root)
        return l


tree = TreeNode(1, None, (TreeNode(2, TreeNode(3, None, None)), None))
print(Solution.inorderTraversal(tree))
