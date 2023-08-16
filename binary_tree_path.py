# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
print(Solution.binaryTreePaths([6,2,9,1,7,0])