# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def mirror(n1:TreeNode, n2:TreeNode):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            
            left = mirror(n1.left, n2.right)
            right = mirror(n1.right,n2.left)
            
            return left and right
        
        return mirror(root.left, root.right)
