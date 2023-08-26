# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        if root:
            count += 1

            if root.left:
                count = count + self.countNodes(root.left)
            if root.right:
                count = count + self.countNodes(root.right)
        return count

print(Solution.countNodes([1,2,3,4,5,6]))

