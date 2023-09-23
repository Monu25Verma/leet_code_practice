# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional, List


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        if root.left == 0 and root.right == 0:
            return root.val

        def chk_duplicates(root):
            if (root.val not in count):
                count[root.val] = 1

            else:
                count[root.val] += 1
            if (root.left == None and root.right == None):
                return
            if root.left != None:
                chk_duplicates(root.left)
            if root.right != None:
                chk_duplicates(root.right)

        count = {}
        chk_duplicates(root)
        result = []
        maxi = max(count.values())
        for key, val in count.items():
            if val == maxi:
                result.append(key)
        return result


print(Solution.findMode([1,null,2,2]))



