# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        queue = collections.deque()
        queue.append(p)
        queue.append(q)
        while queue:
            pNode, qNode = queue.popleft(), queue.popleft()
            if not pNode and not qNode:
                continue
            if not (pNode and qNode) or pNode.val != qNode.val:
                return False
            
            queue.append(pNode.left)
            queue.append(qNode.left)
            queue.append(pNode.right)
            queue.append(qNode.right)
        return True

