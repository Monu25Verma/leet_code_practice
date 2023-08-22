# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height_Bal(root) >= 0

    def height_Bal(self, root):
        if root is None:
            return 0
        leftheight, rightheight = self.height_Bal(root.left), self.height_Bal(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1
        return max(leftheight, rightheight) + 1




print(Solution.height_Bal(TreeNode()))
