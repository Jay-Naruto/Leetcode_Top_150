# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(x,y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            if x.val!=y.val:
                return False
            return check(x.left,y.left) and check(x.right,y.right)
        q=deque([root])
        while q:
            node = q.popleft()
            ans = check(node,subRoot)
            if ans: return True
            else:
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return False
            
                
        