# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        count=0
        stack=[(root , str(root.val))]
        while stack:
            node, strvalue = stack.pop()

            if not node.left and not node.right:
                count += int(strvalue)
            
            if node.left:
                stack.append((node.left , strvalue + str(node.left.val)))
            
            if node.right:
                stack.append((node.right , strvalue + str(node.right.val)))

        return count
