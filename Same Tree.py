# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1=[]
        arr2=[]
        
        def bfs(node:TreeNode, arr):
            if not node:
                arr.append(None)
                return 
            
            q=deque()
            q.append(node)
            
            while q:
                node = q.popleft()
                if node:
                    arr.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    arr.append(None)
        
        bfs(p, arr1)
        bfs(q, arr2)
        
        if arr1 == arr2:
            return True
        else:
            return False
        
        