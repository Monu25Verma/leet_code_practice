# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        queue = collections.deque([(root, root.val)])
        while queue:
            node, val = queue.popleft()
            if node.left is None and node.right is None:
                if val == targetSum:
                    return True
                else:
                    continue
            if node.left:
                queue.append((node.left, val + node.left.val))
            if node.right:
                queue.append((node.right, val + node.right.val))
        return False
print(Solution.hasPathSum([1,2,3],5))





