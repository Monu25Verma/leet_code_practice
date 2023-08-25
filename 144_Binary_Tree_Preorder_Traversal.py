# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
        l = []
        def traverse(current_node):
            if current_node is None:
                return
            l.append(current_node.val)
            traverse(current_node.left)
            traverse(current_node.right)
            return l
        return traverse(root)

print(Solution.preorderTraversal([1,null,2,3]))