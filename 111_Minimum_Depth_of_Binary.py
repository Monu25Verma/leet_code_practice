# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if root is None:
            return 0
        leftdepth = self.minDepth(root.left)
        rightdepth = self.minDepth(root.right)
        print(rightdepth, end=" ")
        print(leftdepth)

        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return 1 + rightdepth
        if root.right is None:
            return 1 + leftdepth

        return min(leftdepth, rightdepth) + 1;


print(Solution.minDepth([3,9,20,null,null,15,7]))