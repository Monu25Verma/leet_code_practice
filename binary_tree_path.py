# 257. Binary Tree Paths

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:

        result = []  # ["", ""]

        def DFS(root, s):
            s = s + str(root.val)
            if not root.left and not root.right:
                result.append(s)
                return
            if root.left:
                DFS(root.left, s + "->")
            if root.right:
                DFS(root.right, s + "->")

        DFS(root, "")
        return result

tree = TreeNode(1,TreeNode(2, None,TreeNode(5,None, None)),TreeNode(3,None, None))
print(Solution.binaryTreePaths(tree))