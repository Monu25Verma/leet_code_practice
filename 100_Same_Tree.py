# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from binary_tree_path import TreeNode


class Solution:
    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None:
            return p == q
        return(p.val == q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


print(Solution.isSameTree([1,2,3], [1,2,3]))

