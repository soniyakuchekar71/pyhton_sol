# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def getLeaves(root):
            if root is None:
               return[]
            if root.left is None and root.right is None:
                return[root.val]
            return getLeaves(root.left)+getLeaves(root.right)
        return getLeaves(root1)==getLeaves(root2)