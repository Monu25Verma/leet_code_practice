# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List


class Solution:
    def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
        l = []
        def traverse(current_node):
            if current_node is None:
                return
            traverse(current_node.left)
            traverse(current_node.right)
            l.append(current_node.val)
            return l
        return traverse(root)


print(Solution.postorderTraversal([1,null,2,3]))