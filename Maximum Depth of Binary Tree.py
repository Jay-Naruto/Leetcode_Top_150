# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def bfs(node:TreeNode):
            q=deque()
            q.append(node)
            k=0
            while q:
                depth = len(q)
                for _ in range(depth):
                    node = q.popleft()
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                k+=1
            return k
                
        
        return bfs(root)
        