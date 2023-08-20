# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import null as null


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.isSame(root.left, root.right)

    def isSame(leftroot, rightroot):
        if leftroot == None and rightroot == None:
            return True
        if leftroot == None or rightroot == None:
            return False
        if leftroot.val != rightroot.val:
            return False

        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)


print(Solution.isSame([1,2,2,null,3,null,3]))


