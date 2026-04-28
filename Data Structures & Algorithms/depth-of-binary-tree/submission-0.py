# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        x = self.maxDepth(root.left)
        y = self.maxDepth(root.right)
        
        if x > y:
            return 1 + x
        else:
            return 1 + y